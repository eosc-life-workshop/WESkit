# WESkit Setup

## Step 1: Install docker

install docker

```bash
sudo apt-get update
sudo apt-get install docker.io
sudo usermod -aG docker ubuntu
```
### Step 2: Setup docker network and swarm

Before swarm initialization, gwbridge network needs to be removed and re-created

This option can be directly used to change the MTU accordingly to your network MTU

```bash
docker network rm docker_gwbridge
docker network create -d bridge \
  --opt com.docker.network.bridge.name=docker_gwbridge \
  --opt com.docker.network.bridge.enable_icc=false \
  --opt com.docker.network.bridge.enable_ip_masquerade=true \
  --opt com.docker.network.driver.mtu=1442 \
  docker_gwbridge
```

initiate swarm

```bash
docker swarm init
```

## Step 3: Install Conda/Mamba

```bash
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
/bin/bash Miniconda3-latest-Linux-x86_64.sh
/bin/bash
conda install -c conda-forge mamba
```

## Step 4: Setup of the deployment environment

Clone the deployment repository and install the deployment environment, which contains just a few required python packages.

```bash
git clone https://gitlab.com/one-touch-pipeline/weskit/deployment
cd deployment
mamba env create -n weskit_deployment -f environment.yaml
conda activate weskit_deployment
```

Running the WESkit demo deployment mounts the `test/data` folder from the repository into the WESkit container.
All results will be written into this folder by a non-root user. Therefore, we need to set write access for this folder to 777.

```bash
chmod 777 tests/data
```

The pre-configured WESkit rest server and other components require certificates for secure communication.
The repository contains a script `generateDevelopmentCerts.sh` to create respective certificates which will be stored at `certs/`. The certificates will then be integrated as secrets into the container.

```bash
./generateDevelopmentCerts.sh
```

### Step 5: Start WESkit

Now start the stack using the python script:

```bash
python weskit_stack.py start
```

This command will start the services in your Docker swarm.

## Step 6: API demo

Once the stack is running (~1min), you can execute a demo script that submits a Snakemake workflow to WESkit.
Per default, the service and the dashboard will be available at ["https://localhost"]("https://localhost"). It might be necessary to resolve localhost manually to 127.0.0.1 .

```bash
python weskit_stack.py test
```

The processed workflow data will be stored within the `tests/data` folder.

## Step 7: Demo workflow submission 

The following describes the submission of a workflow. This example uses python 3.10.8 but curl or any other language that can submit a request is possible.

## Step 8: Example 1 (curl)
Please pay attention that you may need to install "jq". 

```bash
curl --ipv4 --cacert  /home/$USER/weskit/deployment/certs/weskit.crt -X GET  https://localhost:443/ga4gh/wes/v1/service-info

run_id=$(curl \
--ipv4 \
--cacert /home/$USER/weskit/deployment/certs/weskit.crt \
--request POST\
--header 'Content-Type: multipart/form-data' \
--header 'Accept: application/json' \
-F workflow_params='{"text": "hello world"}' \
-F workflow_type="SMK" \
-F workflow_type_version="6.10.0" \
-F workflow_url="tests/workflows/wf1/Snakefile" \
"https://localhost/ga4gh/wes/v1/runs" \
| jq -r .run_id)
echo $run_id

curl --ipv4 --cacert /home/$USER/weskit/deployment/certs/weskit.crt https://localhost/ga4gh/wes/v1/runs/$run_id
```

## Step 9: Example 2
This example can be used to send a workflow to our WESkit demo instance at the deNBI cloud.
Please use the dashboard to obtain your access token: https://weskit.bihealth.org

start python and execute the following command in chunks

```python
import os
import requests
import json
import yaml
import pprint

pp = pprint.PrettyPrinter(indent=2)

WES_URL="https://weskit.bihealth.org"
     
# provide your access token here from the web page
admin_token={"access_token":"XXX"}
header=dict(Authorization="Bearer " + admin_token["access_token"])

# 1.) Get service info
info = requests.get("{}/ga4gh/wes/v1/service-info".format(WES_URL))
pp.pprint(info.json())

   # read workflow params
with open("tests/workflows/wf1/config.yaml") as file:
   workflow_params = json.dumps(yaml.load(file, Loader=yaml.FullLoader))

# create data object for request
data = {
   "workflow_params": workflow_params,
   "workflow_type": "SMK",
   "workflow_type_version": "6.10.0",
   "workflow_url": "wf1/Snakefile"
}

# 2.) Send request to server
response = requests.post("{}/ga4gh/wes/v1/runs".format(WES_URL), data=data,  headers=header)
response.json()
# 3.) Get information about single run
results = requests.get("{}/ga4gh/wes/v1/runs/{}".format(WES_URL, response.json()["run_id"]), 
                           verify=False, headers=header)
 pp.pprint(results.json())

# 4.) Finally, lets get all runs
info = requests.get("{}/ga4gh/wes/v1/runs".format(WES_URL),  headers=header)
pp.pprint(info.json())
```

## Step 10: Demo stack with Keycloak 


```bash
docker stack rm weskit
```

The demo stack can also be deployed together with a Keycloak service for authorization.

```bash
python weskit_stack.py start --login
python weskit_stack.py test --login
```

## Step 11: Example 3

Our next example is going to download a small Snakemake workflow which maps reads to the reference genome.

But before you can execute the next example some configs needs to be adjusted. 

We start with deployment/weskit_config/config_login.yaml file. 
Please set "engine-environment" and "use-conda" to "api:true". This is needed to activate the parameter otherwise we want be able to execute the conda env on the compute side.

In case you deploy WESkit without Keycloak deployment/weskit_config/config.yaml needs to be adjusted. 

Note after each change of the config file WESkit needs to be redeployed.

Download fastqs and reference genome for mapping

```bash
wget https://github.com/snakemake/snakemake-tutorial-data/archive/v5.24.1.tar.gz
tar --wildcards -xf v5.24.1.tar.gz --strip 1 "*/data" "*/environment.yaml"
```

```bash
https://github.com/eosc-life-workshop/deNBI_workshop
```

configure the location of the data accordingly

Please note that the path to the file needs to be absolute (compute perspective) or relative so the WESkit is able to see the from the working directory.


You can also check the logs of the worker /rest container for better debugging.

' docker logs containerID'

```python
import os
import requests
import json
import yaml
import pprint
   
pp = pprint.PrettyPrinter(indent=2)
   
WES_URL="https://localhost"
   
keycloak_host = "http://localhost:8080/auth/realms/WESkit/protocol/openid-connect/token"
credentials = dict(username="test",
                       password="test",
                       client_id="OTP",
                       client_secret="7670fd00-9318-44c2-bda3-1a1d2743492d",
                       grant_type="password")
token = requests.post(url=keycloak_host, data=credentials, verify=False).json()
header = dict(Authorization="Bearer " + token["access_token"])
   
# 1.) Get service info
info = requests.get("{}/ga4gh/wes/v1/service-info".format(WES_URL), verify=False)
pp.pprint(info.json())
   
   
## create data object for request
data = {
     "workflow_params":'{}',
     "workflow_engine_parameters": '{"use-conda":"T", "engine-environment":"workshop_wf/environment.sh"}',
     "workflow_type": "SMK",
     "workflow_type_version": "6.10.0",
     "workflow_url": "workshop_wf/Snakefile"
}
 
 
## send request to server
response = requests.post("{}/ga4gh/wes/v1/runs".format(WES_URL), data=data, files=files, verify=False, headers=header)
response.json()


## get information about single run
results = requests.get("{}/ga4gh/wes/v1/runs/{}".format(WES_URL, response.json()["run_id"]), verify=False, headers=header)
pp.pprint(results.json())
   
# 3.) Finally, lets get all runs
info = requests.get("{}/ga4gh/wes/v1/runs".format(WES_URL), verify=False, headers=header)
pp.pprint(info.json())
```

## Step 12: Remote compute infrastructure configuration

Depending on the desired setup weskit_config/config{_login}.yaml may require some adjustments, such the configuration of the remote compute infrastructure

Note that there are six executors which define where the workflow engine is executed: 
"ssh", "ssh_lsf", "ssh_slurm", "local", "local_lsf", and "local_slurm".
For this examle we assume a cluster with a SLURM scheduling system.

The remote folders need to be mounted into you local machine with e.g. sshfs

```bash
executor:
  type: "ssh_slurm"
  remote_data_dir: "/home/user/path/to/remote/data_dir"
  remote_workflows_dir: "/home/user/path/to/remote/workflows_dir"
  login:
    username: "user"
    hostname: "slurm_cluster"
    port: 22
    knownhosts_file: "~/.ssh/known_hosts"
    keyfile: "~/.ssh/weskit_cluster_test_rsa"
    keyfile_passphrase: ""

```

Depending on the desired workflow engine parameters, some need activation within the config file.
e.g. activation of a conda environment:

```bash
  - name: "use-conda"
    api: true
    type: "bool"
    value: "true"
```

## Step 13: Deploy WESkit using minikube & helm charts -> K8s
Please note that the switch to Kubernetes is an ongoing process and once it is finished 
the user support will move to the newest deplyoment strategy. 

```bash
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

  mkdir /home/$USER/weskit
  cd /home/$USER/weskit/
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



