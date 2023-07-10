configfile: "config.yaml"

rule all:
    input:
        "plots/quals.svg"

def get_reads(wildcards):
    return config["samples"][wildcards.sample]

rule bwa_map:
    input:
        genome=config["genome"],
        reads=get_reads
    output:
        alignment="mapped_reads/{sample}.bam"
    conda:
        "bwa_samtools_bcftools.yaml"
    shell:
        "bwa mem {input.genome} {input.reads} | samtools view -Sb - > {output.alignment}"

rule samtools_sort:
    input:
        bam="mapped_reads/{sample}.bam"
    output:
        bam="sorted_reads/{sample}.bam"
    conda:
        "bwa_samtools_bcftools.yaml"
    shell:
        "samtools sort -T sorted_reads/{wildcards.sample} -O bam {input.bam} > {output.bam}"

rule samtools_index:
    input:
        bam="sorted_reads/{sample}.bam"
    output:
        bai="sorted_reads/{sample}.bam.bai"
    conda:
        "bwa_samtools_bcftools.yaml"
    shell:
        "samtools index {input.bam}"

SAMPLES = config["samples"].keys()

rule bcftools_call:
    input:
        fa=config["genome"],
        bams=expand("sorted_reads/{sample}.bam", sample=SAMPLES),
        bais=expand("sorted_reads/{sample}.bam.bai", sample=SAMPLES)
    output:
        "calls/all.vcf"
    conda:
        "bwa_samtools_bcftools.yaml"
    shell:
        "samtools mpileup -g -f {input.fa} {input.bams} | "
        "bcftools call -mv - > {output}"

rule plot_quals:
    input:
        "calls/all.vcf"
    output:
        "plots/quals.svg"
    conda:
        "py_plot.yaml"
    script:
        "plot-quals.py"
