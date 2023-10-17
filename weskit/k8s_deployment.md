
```
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install docker.io
  sudo usermod -aG docker $USER
  sudo reboot

  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  sudo install minikube-linux-amd64 /usr/local/bin/minikube

  cat - <<EOF > /etc/sysctl.d/10-minikube.conf 
  fs.inotify.max_queued_events = 16384
  fs.inotify.max_user_instances = 512
  fs.inotify.max_user_watches = 262144
  user.max_inotify_instances = 512
  user.max_inotify_watches = 262144
  EOF

  
clusterIP=192.168.60.2
internalGatewayIP=192.168.60.1

export NO_PROXY="10.0.0.0/8,192.168.0.0/16"
export no_proxy="$NO_PROXY"

developmentUser="$USER"
sudo groupadd -g 35671 weskit
sudo usermod -a -G weskit $developmentUser
sudo groupadd -g 1001 bitnami
sudo usermod -a -G bitnami $developmentUser

mountPoint="/home/$USER/localVolumes"
mkdir "$mountPoint"
cd "$mountPoint"


# Pull api-repository into api/ directory ALWAYS 
git clone https://gitlab.com/one-touch-pipeline/weskit/api.git

# For the WESkit containers
mkdir data/
sudo chgrp weskit data/
sudo chgrp 0700 data/

# For the Bitnami containers
mkdir redis/ mongodb/
sudo chgrp bitnami redis/ mongodb/
sudo chgrp 0700 redis/ mongodb/ 

sudo ufw deny in from $clusterIP to  $internalGatewayIP proto tcp 
sudo ufw allow in from $clusterIP to $internalGatewayIP port 38069 proto tcp 

###
docker network create --driver=bridge --subnet=192.168.60.0/24 --gateway=192.168.60.1 -o --ip-masq -o --icc -o com.docker.network.driver.mtu=1442 --label=created_by.minikube.sigs.k8s.io=true --label=name.minikube.sigs.k8s.io=minikube minikube
minikube start --mount=true   --mount-port=38069  --mount-string="/home/$USER/localVolumes/:/localVolumes" --driver docker  --network minikube --static-ip 192.168.60.2

minikube ssh  ls /localVolumes/api

mkdir weskit
cd weskit
git clone https://gitlab.com/one-touch-pipeline/weskit/helm-deployment.git
cd helm-deployment/

./generateDevelopmentCerts.sh certs/ weskit $clusterIP

wget https://get.helm.sh/helm-v3.13.0-linux-amd64.tar.gz
tar -zxvf helm-v3.13.0-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin/helm

helm dependencies update

cp example-values.yaml your-values.yaml
helm install -f your-values.yaml weskit-devel-1 ./

curl --ipv4 https://192.168.60.2:30132/ga4gh/wes/v1/service-info --cacert /home/$USER/weskit/helm-deployment/certs/weskit.crt
```
