# Initialization

## 0 Prerequisites

- You need to have a deNBI account to  become a member of our training project at the de.NBI cloud in Bielefeld
- Your public ssh must be added at the de.NBI portal: https://cloud.denbi.de/portal/ to able to connect.

## 1 Deploy a VM in training project

1. Login with LifeScience Login at de.NBI cloud Bielefeld horizon dashboard (OpenStack graphical interface): https://denbi-cloud.bihealth.org/
2. First time users need to add their public ssh key to the horizon dashboard, to be able to inject your public key when you create a new VM:
Project --> Compute --> Key Pairs --> Import Public Key

3. Create a virtual machine using a pre-build snapshot: Project --> Compute --> Instances --> Launch Instance

4. Assign a floating ip to get ssh access: Project --> Compute --> Instances --> choose your instance --> assign floating VM
 
    - Assign floating IP  129.70.51.x

## 2 Connect to your personal instance via Theia link 
## The following point were already executed by the host of the workshop


1. Download and install conda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
/bin/bash Miniconda3-latest-Linux-x86_64.sh
/bin/bash
conda install -c conda-forge mamba
```

2. Install conda environment

```bash
cd deNBI_workshop/init
mamba env create --file environment.yaml
conda activate snakemake_training
cd ../snakemake/
```
