# Initialization

## 0 Prerequisites

- You need a deNBI account to  become a member of our training project at the de.NBI cloud in Bielefeld.

## 1 Deploy a VM in training project

1. Login with your LifeScience Login at the de.NBI Portal: https://cloud.denbi.de/portal/webapp/#/userinfo

2. As a member of the workshop you can start your personal Simple VM instance right away:
Virtual Machines --> Overviews --> Instances --> Instance Name Contains your first- and surname

3. Get the Theia IDE by clicking on following URL https://simplevm.bi.denbi.de/CPBWSW<surname_and_firstname>_100


## 2 Within your personal SimpleVM instance
### The following points were already executed by the host of the workshop


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
