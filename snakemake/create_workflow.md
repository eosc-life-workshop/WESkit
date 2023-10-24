# Snakemake & workflow

## Data

1. First, we download tutorial data from the official Snakemake repository - complete tutorial is very recommended for advanced learning!
  - ignore the environment.yaml file as we already installed it

```bash
conda activate snakemake_training
cd $HOME/3rd_denbi_user_meeting__snakemake_cloud/2_snakemake
wget wget https://github.com/snakemake/snakemake-tutorial-data/archive/refs/tags/v7.4.3.tar.gz
tar --wildcards -xf v7.4.3.tar.gz --strip 1 "*/data"
```

##  A simple workflow 

1. The first step/rule of the workflow maps reads of a given sample to a given reference genome. We will will use bwa mem to do this.

```python
rule bwa_map:
    input:
        genome="data/genome.fa",
        reads="data/samples/A.fastq"
    output:
        alignment="mapped_reads/A.bam"
    shell:
        "bwa mem {input.genome} {input.reads} | samtools view -Sb - > {output.alignment}"
```

2. We create a Snakefile (workflow file) and copy the code into it. Run the workflow with:

```bash
snakemake --snakefile Snakefile --cores 1 mapped_reads/A.bam
```

3. The previous rule only works for one sample. 
   Snakemake uses wildcards for generalization; here {sample} is used to generalize input reads:

```python
rule bwa_map:
    input:
        genome="data/genome.fa",
        reads="data/samples/{sample}.fastq"
    output:
        alignment="mapped_reads/{sample}.bam"
    shell:
        "bwa mem {input.genome} {input.reads} | samtools view -Sb - > {output.alignment}"
```

4. Run updated workflow:

```bash
snakemake --snakefile Snakefile --cores 1 mapped_reads/A.bam mapped_reads/B.bam
snakemake --snakefile Snakefile --cores 1 mapped_reads/{A,B}.bam
```

5. Sorting read alignments using samtools:

```python
rule samtools_sort:
    input:
        bam="mapped_reads/{sample}.bam"
    output:
        bam="sorted_reads/{sample}.bam"
    shell:
        "samtools sort -T sorted_reads/{wildcards.sample} "
        "-O bam {input.bam} > {output.bam}"
```

```bash
snakemake --snakefile Snakefile --cores 1 mapped_reads/A.bam mapped_reads/B.bam
snakemake --snakefile Snakefile --cores 1 mapped_reads/{A,B}.bam
```

6. Create an alignment index file:

```python
rule samtools_index:
    input:
        bam="sorted_reads/{sample}.bam"
    output:
        bai="sorted_reads/{sample}.bam.bai"
    shell:
        "samtools index {input.bam}"
```

```bash
snakemake --snakefile Snakefile --cores 1 sorted_reads/{A,B}.bam
```

7. Calling genomic variants:

```python
SAMPLES = ["A", "B"] # allways at the top of the Snakefile

rule bcftools_call:
    input:
        fa="data/genome.fa",
        bams=expand("sorted_reads/{sample}.bam", sample=SAMPLES),
        bais=expand("sorted_reads/{sample}.bam.bai", sample=SAMPLES)
    output:
        vcf="calls/all.vcf"
    shell:
        "samtools mpileup -g -f {input.fa} {input.bams} | "
        "bcftools call -mv - > {output.vcf}"
```

```bash
snakemake --snakefile Snakefile --cores 1 calls/all.vcf
```

8. Apply a custom script to visualize the results:

```python
rule plot_quals:
    input:
        vcf="calls/all.vcf"
    output:
        svg="plots/quals.svg"
    script:
        "scripts/plot-quals.py"
```
```bash
snakemake --snakefile Snakefile --cores 1 plots/quals.svg
```

9. Adding a target rule: Snakemake also accepts rule names as targets 

```python
rule all:
    input:
        "plots/quals.svg"
```

```bash
snakemake --snakefile Snakefile --cores 1 all
```

10. The final Snakefile should look like this

```python
SAMPLES = ["A", "B"]

rule all:
    input:
        "plots/quals.svg"

rule bwa_map:
    input:
        genome="data/genome.fa",
        reads="data/samples/{sample}.fastq"
    output:
        alignment="mapped_reads/{sample}.bam"
    shell:
        "bwa mem {input.genome} {input.reads} | samtools view -Sb - > {output.alignment}"

rule samtools_sort:
    input:
        bam="mapped_reads/{sample}.bam"
    output:
        bam="sorted_reads/{sample}.bam"
    shell:
        "samtools sort -T sorted_reads/{wildcards.sample} -O bam {input.bam} > {output.bam}"

rule samtools_index:
    input:
        bam="sorted_reads/{sample}.bam"
    output:
        bai="sorted_reads/{sample}.bam.bai"
    shell:
        "samtools index {input.bam}"

rule bcftools_call:
    input:
        fa="data/genome.fa",
        bam=expand("sorted_reads/{sample}.bam", sample=SAMPLES),
        bai=expand("sorted_reads/{sample}.bam.bai", sample=SAMPLES)
    output:
        vcf="calls/all.vcf"
    shell:
        "bcftools mpileup -f {input.fa} {input.bam} | "
        "bcftools call -mv - > {output.vcf}"

rule plot_quals:
    input:
        vcf="calls/all.vcf"
    output:
        svg="plots/quals.svg"
    script:
        "scripts/plot-quals.py"
```