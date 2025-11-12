import yaml
import os
import subprocess

WORKFLOW_CONFIG = {}
SAMPLE_METADATA = {}
SAMPLE_OUTPUTS = {}
COHORT_OUTPUTS = {}
REFERENCE_DICT = {}

def check_average_read_length(fastq):
    command = f'seqtk seq -A "{fastq}" | awk \'{{if(NR%2==0){{sum+=length($0);n++}}}} END{{if(n>0) print sum/n; else print 0}}\''
    average_length = subprocess.run(command, shell=True, capture_output=True, text=True)
    return float(average_length.stdout.strip() or 0)

def initialize_from_yaml(INPUT_YAML):
    with open(f"{INPUT_YAML}", "r") as f:
        input = yaml.safe_load(f)
        SAMPLES = input["sample"]
        GENOME = input["reference"]["genome"]
        KNOWN_SITES = input["reference"]["known_site"]
        OUTDIR = input["output"]["directory"]
    return SAMPLES, GENOME, KNOWN_SITES, OUTDIR

def init_samples(SAMPLES, GENOME, KNOWN_SITES, OUTDIR):
    for sample in SAMPLES:
        ID = sample["id"]
        R1 = sample["read1"]
        R2 = sample["read2"]
        FORWARD_AVERAGE_LENGTH = check_average_read_length(R1)
        REVERSE_AVERAGE_LENGTH = check_average_read_length(R2)
        AVERAGE_LENGTH = (FORWARD_AVERAGE_LENGTH + REVERSE_AVERAGE_LENGTH) / 2   
        if AVERAGE_LENGTH >= 250:
            READ_TYPE = "long"
        else:
            READ_TYPE = "short"
        SAMPLE_OUTDIR = os.path.join(OUTDIR, ID)
        os.makedirs(SAMPLE_OUTDIR, exist_ok=True)
        SAMPLE_METADATA[ID] = {
            # INPUT INFO
            "read1": R1,
            "read2": R2,
            "sample_outdir": SAMPLE_OUTDIR, 
            "platform": "illumina",
            "read_length_type": READ_TYPE,
            "average_length": AVERAGE_LENGTH,}
        SAMPLE_OUTPUTS[ID] = {
            # MAPPING/ALIGNMENT INFO
            "sam_file": f"{ID}.sam",
            "bam_file": f"{ID}.bam",
            "sorted_bam_file": f"{ID}.temp_1.bam",
            "sorted_marked_bam_file": f"{ID}.temp_2.bam",
            "sorted_marked_recal_bam_file": f"{ID}.final.bam",
            # VARIANT INFO
            "gvcf_file": f"{ID}.g.vcf",
            "final_vcf_file": f"{ID}.final.vcf",
            "xlsx_file" : f"{ID}.xlsx"
        }
    COHORT_OUTPUTS = {
        "combined_gvcf_file": "variant.combined.g.vcf",
        "cohort_gvcf_file": "cohort.g.vcf",
        "cohort_filtered_gvcf_file": f"cohort.filtered.g.vcf",
        "cohort_normalized_gvcf_file":f"cohort.normalized.g.vcf",
        "cohort_snpEff_and_snpSift_annotated_gvcf_file": f"cohort.snpEff_and_snpSift.annotated.g.vcf",
        "cohort_final_gvcf_file": f"cohort.final.g.vcf",
    }
    REFERENCE_LIST = {
        "genome": GENOME,
        "known_sites": KNOWN_SITES
    }

    WORKFLOW_CONFIG = {SAMPLE_METADATA, SAMPLE_OUTPUTS, COHORT_OUTPUTS, REFERENCE_LIST}

    return WORKFLOW_CONFIG