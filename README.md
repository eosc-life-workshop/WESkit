# WESkit workshop
In this workshop, we are going to use the open-source software WESkit that helps researchers to execute Nextflow and Snakemake workflows locally or remote (HPC). WESkit provides extensive logging capabilities, and a user management system, and supports high data throughput, stability, and security.
Participants will be encouraged to set up their own WESkit instance and use it to submit both Nextflow and Snakemake workflows.


# Preparation

## Docker

* install docker

```console
sudo apt-get update
sudo apt-get install docker.io
sudo usermod -aG docker ubuntu
```

* setup mtu in docker
  
Sometimes the docker MTU and your network MTU show different values. 
The docker MTU should have at least the same MTU size as your network. 
Otherwise interaction with your network (e.g. internet) won't be possible

```console
ip link # check mtu
sudo echo '{"mtu": 1442}' | sudo tee -a /etc/docker/daemon.json
sudo service docker restart
```

* restart VM and re-login if needed

### setup swarm

* Before swarm initialization, gwbridge network needs to be removed and re-created

This option can be directly used to change the MTU accordingly to your network MTU

```console
docker network rm docker_gwbridge
docker network create -d bridge \
  --opt com.docker.network.bridge.name=docker_gwbridge \
  --opt com.docker.network.bridge.enable_icc=false \
  --opt com.docker.network.bridge.enable_ip_masquerade=true \
  --opt com.docker.network.driver.mtu=1442 \
  docker_gwbridge
```

* initiate swarm

```console
docker swarm init
```

## Install Conda/Mamba

```bash
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
/bin/bash Miniconda3-latest-Linux-x86_64.sh
/bin/bash
conda install -c conda-forge mamba
```


* Clone the deployment repository and install the deployment environment, which contains just a few required python packages.

```bash
git clone https://gitlab.com/one-touch-pipeline/weskit/deployment
cd deployment
mamba env create -n weskit_deployment -f environment.yaml
conda activate weskit_deployment
```

* Running the WESkit demo deployment mounts the `test/data` folder from the repository into the WESkit container.
All results will be written into this folder by a non-root user. Therefore, we need to set write access for this folder to 777.

```bash
chmod 777 tests/data
```

* The pre-configured WESkit rest server and other components require certificates for secure communication.
The repository contains a script `generateDevelopmentCerts.sh` to create respective certificates which will be stored at `certs/`. The certificates will then be integrated as secrets into the container.

```bash
./generateDevelopmentCerts.sh
```

### Start Weskit

4. Now start the stack using the python script:

```bash
python weskit_stack.py start
```

This command will start the services in your Docker swarm.

## API demo

5. Once the stack is running (~1min), you can execute a demo script that submits a Snakemake workflow to WESkit.
Per default, the service and the dashboard will be available at ["https://localhost"]("https://localhost"). It might be necessary to resolve localhost manually to 127.0.0.1 .

```bash
python weskit_stack.py test
```

The processed workflow data will be stored within the `tests/data` folder.

## Additional services

The demo stack can also be deployed together with a Keycloak service for authorization and a MinIO service to provide S3 access to the demo data.

```bash
python weskit_stack.py start --login --minio
python weskit_stack.py test --login
```
