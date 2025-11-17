import yaml
import os
import subprocess

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

def initialize_from_yaml(input_yaml):

    SAMPLES = None
    GENOME = None
    KNOWN_SITES = None
    OUTDIR = None

    with open(f"{input_yaml}", "r") as f:
        input = yaml.safe_load(f)
        SAMPLES = input["sample"]
        GENOME = input["reference"]["genome"]
        KNOWN_SITES = input["reference"]["known_site"]
        OUTDIR = input["output"]["directory"]
    return SAMPLES, GENOME, KNOWN_SITES, OUTDIR

def init_samples(SAMPLES, GENOME, KNOWN_SITES, OUTDIR):

    ID = None
    R1 = None
    R2 = None
    FORWARD_AVERAGE_LENGTH = None
    REVERSE_AVERAGE_LENGTH = None
    AVERAGE_LENGTH = None
    READ_TYPE = None

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
            "platform": "illumina",
            "average_length": AVERAGE_LENGTH,
            "read_length_type": READ_TYPE,
            }
        SAMPLE_OUTPUTS[ID] = {
            # MAPPING/ALIGNMENT INFO
            "sample_outdir": SAMPLE_OUTDIR, 
            "sample_sam_file": f"{ID}.sam",
            "sample_sorted_bam_file": f"{ID}.sorted.bam",
            "sample_marked_bam_file": f"{ID}.marked.bam",
            "sample_recal_bam_file": f"{ID}.recal.bam",
            "sample_final_bam_file": f"{ID}.final.bam",
            # VARIANT INFO
            "sample_gvcf_file": f"{ID}.g.vcf",
            "sample_vcf_file": f"{ID}.vcf",
            "sample_final_vcf_file": f"{ID}.final.vcf",      
        }
        REPORT_OUTPUTS[ID] = {
            # REPORT INFO
            "sample_xlsx_file" : f"{ID}.xlsx"
        }
    COHORT_OUTPUTS = {
        "cohort_gvcf_file": "cohort.g.vcf",
        "cohort_vcf_file": "cohort.vcf",
        "cohort_filtered_vcf_file": f"cohort.filtered.vcf",
        "cohort_normalized_vcf_file":f"cohort.normalized.vcf",
        "cohort_genome_annotated_vcf_file": f"cohort.genome_annotated.vcf",
        "cohort_clinvar_annotated_vcf_file": f"cohort.clinvar_annotated.vcf",
        "cohort_p3_1000g_annotated_vcf_file": f"cohort.p3_1000g_annotated.vcf",
        "cohort_dbsnp_annotated_vcf_file": f"cohort.dbsnp_annotated.vcf",
        "cohort_dbnsfp_annotated_vcf_file": f"cohort.dbnsfp_annotated.vcf",
        "cohort_final_vcf_file": f"cohort.final.vcf",

    }
    REFERENCE_DICT = {
        "reference_genome": GENOME,
        "reference_known_sites": KNOWN_SITES
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