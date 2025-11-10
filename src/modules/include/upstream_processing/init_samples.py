import yaml
import os
import subprocess

SAMPLE_LIST = {}
REFERENCE_LIST = {}

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
        SAMPLE_LIST[ID] = {
            # INPUT INFO
            "read1": R1,
            "read2": R2,
            "sample_outdir": SAMPLE_OUTDIR,
            "platform": "illumina",
            "read_length_type": READ_TYPE,
            "average_length": AVERAGE_LENGTH,
            # MAPPING/ALIGNMENT INFO
            "sam_file": f"{ID}.sam",
            "bam_file": f"{ID}.bam",
            "sorted_bam_file": f"{ID}.temp_1.bam",
            "sorted_marked_bam_file": f"{ID}.temp_2.bam",
            "sorted_marked_recal_bam_file": f"{ID}.final.bam",
            # VARIANT INFO
            "raw_gvcf_file": f"{ID}.g.vcf",
            "final_vcf_file": f"{ID}.final.vcf",
            "xlsx_file" : f"{ID}.xlsx"
        }
    GLOBAL_GVCF_LIST = {
        "combined_gvcf_file": "combined.g.vcf",
        "cohort_gvcf_file": "cohort.g.vcf",
        "filtered_gvcf_file": f"variant.filtered.g.vcf",
        "annotated_gvcf_file": f"variant.annotated.g.vcf",
        "final_gvcf_file": f"variant.final.g.vcf",
    }
    REFERENCE_LIST = {
        "genome": GENOME,
        "known_sites": KNOWN_SITES
    }

    return SAMPLE_LIST, REFERENCE_LIST, GLOBAL_GVCF_LIST