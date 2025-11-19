import subprocess

def index_reference_genome_bwa(reference_genome):
    command = f"""
        bwa index {reference_genome}
    """
    subprocess.run(command, shell=True, check=True)

def index_reference_genome_minimap2(reference_genome):
    command = f"""
        minimap2 -d \
            {reference_genome}.mmi \
            {reference_genome} \
    """
    subprocess.run(command, shell=True, check=True)

def index_reference_genome_samtools(reference_genome):
    command = f"""
        samtools faidx {reference_genome}
    """
    subprocess.run(command, shell=True, check=True)

def index_reference_genome_gatk(reference_genome):
    reference_genome_dict = reference_genome.with_suffix(".dict")
    command = f"""
        gatk CreateSequenceDictionary \
            -R {reference_genome} \
            -O {reference_genome_dict}
    """
    subprocess.run(command, shell=True, check=True)

