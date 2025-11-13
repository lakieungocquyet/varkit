import yaml
import os
import subprocess

SAMPLES = None
GENOME = None
KNOWN_SITES = None
OUTDIR = None
ID = None
R1 = None
R2 = None
FORWARD_AVERAGE_LENGTH = None
REVERSE_AVERAGE_LENGTH = None
AVERAGE_LENGTH = None
READ_TYPE = None

SAMPLE_INPUTS = {}
REFERENCE_DICT = {}
SAMPLE_OUTPUTS = {}
COHORT_OUTPUTS = {}
REPORT_OUTPUTS = {}

WORKFLOW_CONFIG = {}

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
        if AVERAGE_LENGTH >= 200:
            READ_TYPE = "long"
        else:
            READ_TYPE = "short"
        SAMPLE_OUTDIR = os.path.join(OUTDIR, ID)
        os.makedirs(SAMPLE_OUTDIR, exist_ok=True)
        SAMPLE_INPUTS[ID] = {
            # INPUT INFO
            "read_1": R1,
            "read_2": R2,
            "sample_outdir": SAMPLE_OUTDIR, 
            "platform": "illumina",
            "average_length": AVERAGE_LENGTH,
            "read_length_type": READ_TYPE,
            }
        SAMPLE_OUTPUTS[ID] = {
            # MAPPING/ALIGNMENT INFO
            "sam_file": f"{ID}.sam",
            "sorted_bam_file": f"{ID}.sorted.bam",
            "marked_bam_file": f"{ID}.marked.bam",
            "recal_bam_file": f"{ID}.recal.bam",
            "final_bam_file": f"{ID}.final.bam",
            # VARIANT INFO
            "gvcf_file": f"{ID}.g.vcf",
            "vcf_file": f"{ID}.vcf",
            "final_vcf_file": f"{ID}.final.vcf",      
        }
        REPORT_OUTPUTS[ID] = {
            # REPORT INFO
            "xlsx_file" : f"{ID}.xlsx"
        }
    COHORT_OUTPUTS = {
        "combination_gvcf_file": "combination.g.vcf",
        "cohort_gvcf_file": "cohort.g.vcf",
        "cohort_filtered_gvcf_file": f"cohort.filtered.g.vcf",
        "cohort_normalized_gvcf_file":f"cohort.normalized.g.vcf",
        "cohort_snpEff_and_snpSift_annotated_gvcf_file": f"cohort.snpEff_and_snpSift_annotated.g.vcf",
        "cohort_final_gvcf_file": f"cohort.final.g.vcf",
    }
    REFERENCE_DICT = {
        "genome": GENOME,
        "known_sites": KNOWN_SITES
    }

    WORKFLOW_CONFIG = {
        "sample_inputs": SAMPLE_INPUTS, 
        "reference_dict": REFERENCE_DICT, 
        "sample_outputs": SAMPLE_OUTPUTS, 
        "cohort_outputs": COHORT_OUTPUTS, 
        "report_outputs": REPORT_OUTPUTS,
        "outdir": OUTDIR 
        }

    return WORKFLOW_CONFIG