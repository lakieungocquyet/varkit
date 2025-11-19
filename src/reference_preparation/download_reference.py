import subprocess
from modules.utils.log import log

def download_reference(reference_name, reference_url, outdir, file_name):
    log.info(f"Downloading: {reference_name}")
    try:
        command = f"""
            wget -P {outdir} {reference_url} -O {outdir}/{file_name}
        """
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        log(f"Error downloading {reference_name}: {e}")
        raise

# Human Genome GRCh37.p13
download_reference(
    reference_name = "Human Genome GRCh37.p13", 
    reference_url = "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.25_GRCh37.p13/GRCh37_seqs_for_alignment_pipelines/GCA_000001405.14_GRCh37.p13_no_alt_analysis_set.fna.gz", 
    outdir = "/opt/varkit/references/genome",
    file_name = "GRCh37.p13.fna.gz"
)
# Clinvar
download_reference(
    reference_name = "Clinvar Reference Variants For GRCh37.p13", 
    reference_url = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/archive_2.0/2024/clinvar_20240716.vcf.gz", 
    outdir = "/opt/varkit/references/reference_variants",
    file_name = "clinvar.vcf.gz"
)
# dbSNP
download_reference(
    reference_name = "dbSNP Reference Variants For GRCh37.p13", 
    reference_url = "https://ftp.ncbi.nih.gov/snp/organisms/human_9606_b151_GRCh37p13/VCF/All_20180423.vcf.gz", 
    outdir = "/opt/varkit/references/reference_variants",
    file_name = "dbSNP.vcf.gz"
)
# Mills & 1000G Gold Standard Indels (hg19)
download_reference(
    reference_name = "Mills & 1000G Gold Standard Indels Reference Variants For GRCh37.p13", 
    reference_url = "", 
    outdir = "/opt/varkit/references/reference_variants",
    file_name = ""
)
# 1000G Omni 2.5 (hg19)
download_reference(
    reference_name = "1000G Omni 2.5 Reference Variants Index For hg19", 
    reference_url = "", 
    outdir = "/opt/varkit/references/reference_variants",
    file_name = "1000G_omni2.5.hg19.sites.vcf.gz"
)
# HapMap 3.3 (hg19)
download_reference(
    reference_name = "HapMap 3.3 Reference Variants For hg19", 
    reference_url = "", 
    outdir = "/opt/varkit/references/reference_variants",
    file_name = "hapmap_3.3.hg19.sites.vcf.gz"
)
# dbNSFP4.1 (hg19)
download_reference(
    reference_name = "dbNSFP4.1a Reference For hg19", 
    reference_url = "https://snpeff.blob.core.windows.net/databases/dbs/GRCh37/dbNSFP_4.1a/dbNSFP4.1a.txt.gz", 
    outdir = "/opt/varkit/references/reference_variants",
    file_name = "dbNSFP4.1a.txt.gz"
)

