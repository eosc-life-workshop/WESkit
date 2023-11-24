# Snakemake & workflow

## Environment activation

First, we use the tutorial data from the official Snakemake repository. Completion of the tutorial is very recommended for advanced learning!
We will create a Snakefile (workflow file) and copy the rules into it.

Please execute the following lines in the terminal
``` bash
conda activate snakemake_training
cd /home/ubuntu/deNBI_workshop/snakemake
touch Snakefile
```

##  A simple workflow 

1. The first rule of the workflow maps reads of a given sample to a reference genome. For this task we will use the tool `bwa mem`.

Please copy the following rule into the empty Snakefile.
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

Please execute the Snakemake workflow using the following command in the terminal:

```bash
snakemake --snakefile Snakefile --cores 1 mapped_reads/A.bam
```

2. The previous rule mapped only one sample (`A.fastq`) to the reference genome. 
   Snakemake uses wildcards for generalization; here `{sample}` is used to generalize input reads:
   
Please replace the previous rule with the following code.

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

3. Run updated workflow using one of the commands below. 
   Both commands do the same although the second one uses shell expansion.

Please execute one of the commands in the terminal.

```bash
snakemake --snakefile Snakefile --cores 1 mapped_reads/A.bam mapped_reads/B.bam
```

4. Sorting read alignments using samtools. 

Please append the following rule to the Snakefile.
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

Please execute the following command in the terminal.
```bash
snakemake --snakefile Snakefile --cores 1 sorted_reads/{A,B}.bam
```

5. The last call of Snakemake executed only the two sorting steps because the initial alignment files already existed.
   Please remove all alignment files and re execute the Snakemake call.

```bash
rm -r mapped_reads
rm -r sorted_reads
snakemake --snakefile Snakefile --cores 1 sorted_reads/{A,B}.bam
```

6. Create an alignment index file.

Please append the following rule to the Snakefile.
```python
rule samtools_index:
    input:
        bam="sorted_reads/{sample}.bam"
    output:
        bai="sorted_reads/{sample}.bam.bai"
    shell:
        "samtools index {input.bam}"
```

Please execute the following command in the terminal.
```bash
snakemake --snakefile Snakefile --cores 1 sorted_reads/{A,B}.bam.bai
```

7. Calling genomic variants.

Please append the following rule to the Snakefile.
```python
SAMPLES = ["A", "B"] # define variables allways at the top of the Snakefile

rule bcftools_call:
    input:
        fa="data/genome.fa",
        bams=expand("sorted_reads/{sample}.bam", sample=SAMPLES),
        bais=expand("sorted_reads/{sample}.bam.bai", sample=SAMPLES)
    output:
        vcf="calls/all.vcf"
    shell:
        "bcftools mpileup -f {input.fa} {input.bams} | "
        "bcftools call -mv - > {output.vcf}"
```

Please execute the following command in the terminal.
```bash
snakemake --snakefile Snakefile --cores 1 calls/all.vcf
```

8. Apply a custom script to visualize the results.

Please append the following rule to the Snakefile.
```python
rule plot_quals:
    input:
        vcf="calls/all.vcf"
    output:
        svg="plots/quals.svg"
    script:
        "scripts/plot-quals.py"
```

Please execute the following command in the terminal.
```bash
snakemake --snakefile Snakefile --cores 1 plots/quals.svg
```

9. If nothing  is specified Snakemake will use the first rule as target rule. 
   That is why we define a target rule called "all".

Please append the following rule as the first rule to the Snakefile.
```python
rule all:
    input:
        "plots/quals.svg"
```

Please execute the following command in the terminal.
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
