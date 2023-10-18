# Initialization

## 0 Prerequisites

- You need to have a deNBI account to  become a member of our training project at the de.NBI cloud in Bielefeld
- Your public ssh must be added at the de.NBI portal: https://cloud.denbi.de/portal/ to able to connect.

## 1 Deploy a VM in training project

1. Login with LifeScience Login at de.NBI cloud Bielefeld horizon dashboard (OpenStack graphical interface): https://denbi-cloud.bihealth.org/
2. First time users need to add their public ssh key to the horizon dashboard, to be able to inject your public key when you create a new VM:
Project --> Compute --> Key Pairs --> Import Public Key

3. Create a virtual machine: Project --> Compute --> Instances --> Launch Instance

    - Details: set an **Instance Name with your zoomname** in it
    - Source: set **Create new volume** to **no** and choose "Ubuntu 22.04 LTS (2023-09-28)" image
    - Flavor:  **de.NBI default**
    - Networks: select **CPBielefeld**
    - Key pair: choose **YOURKEY**
    - Launch instance

4. Assign a floating ip to get ssh access: Project --> Compute --> Instances --> choose your instance --> assign floating VM
 
    - Assign floating IP  129.70.51.x

## 2 Connect to instance via ssh

Connection to OpenStack vm at de.NBI cloud site Bielefeld.

**A)** 

1. Connect from your client: 

```bash
PATH_TO_KEY=/path/to/id_rsa.pub
ssh yourUserName@129.70.51.x -i PATH_TO_KEY
```


**B)** Setup ssh-config under .ssh/config

  - Windows(C:\Users\user\\.ssh\config) & Linux(~/.ssh/config) :

```bash

Host training_snakemake
  HostName 129.70.51.x
  IdentityFile PATH_TO_KEY
  User ubuntu
```

## 3. Setup project 

Connect to instance via ssh 

1. Clone this repository

```bash
cd 
git clone https://github.com/eosc-life-workshop/WESkit.git
```

2. Download and install conda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
/bin/bash Miniconda3-latest-Linux-x86_64.sh
/bin/bash
```

3. Install conda environment

```bash
cd 
mamba env create --file environment.yaml
conda activate snakemake_training
```
