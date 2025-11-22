import yaml
import os
import subprocess
import pathlib
from datetime import datetime
from modules.utils.translate_path import translate_path
import uuid

SAMPLE_INPUTS_DICT = {}
REFERENCE_DICT = {}
SAMPLE_OUTPUTS_DICT = {}
COHORT_OUTPUTS_DICT = {}
REPORT_OUTPUTS_DICT = {}

WORKFLOW_CONFIG = {}

def create_temp_outdir(root):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    unique_id = uuid.uuid4().hex[:8]
    path = pathlib.Path(root) / f"{timestamp}_{unique_id}"
    path.mkdir(parents=True, exist_ok=True)
    return path

def check_average_read_length(fastq):
    command = f'seqtk seq -A "{fastq}" | awk \'{{if(NR%2==0){{sum+=length($0);n++}}}} END{{if(n>0) print sum/n; else print 0}}\''
    average_length = subprocess.run(command, shell=True, capture_output=True, text=True)
    return float(average_length.stdout.strip() or 0)

def initialize_from_yaml(input_yaml):
    with open(f"{input_yaml}", "r") as f:
        input = yaml.safe_load(f)
        SAMPLE_LIST = input["input_paths"]["sample"]
        GENOME_PATH = input["input_paths"]["reference"]["genome"]
        KNOWN_SITES_LIST = input["input_paths"]["reference"]["known_site"]
        OUTDIR_PATH = input["input_paths"]["output"]["directory"]
    return SAMPLE_LIST, GENOME_PATH, KNOWN_SITES_LIST, OUTDIR_PATH

def initialize_samples(SAMPLE_LIST, GENOME_PATH, KNOWN_SITES_LIST, OUTDIR_PATH):
    TEMP_OUTDIR_PATH = create_temp_outdir(
        root = "/otp/varkit/jobspace"
    )
    for SAMPLE in SAMPLE_LIST:
        SAMPLE_ID = SAMPLE["id"]
        READ_1_PATH = SAMPLE["read1"]
        READ_2_PATH = SAMPLE["read2"]
        READ_1_WSL_PATH = translate_path(READ_1_PATH)
        READ_2_WSL_PATH = translate_path(READ_2_PATH)
        FORWARD_AVERAGE_LENGTH = check_average_read_length(READ_1_WSL_PATH)
        REVERSE_AVERAGE_LENGTH = check_average_read_length(READ_2_WSL_PATH)
        AVERAGE_LENGTH = (FORWARD_AVERAGE_LENGTH + REVERSE_AVERAGE_LENGTH) / 2   
        if AVERAGE_LENGTH >= 200:
            READ_TYPE = "long"
        else:
            READ_TYPE = "short"

        SAMPLE_OUTDIR_PATH = os.path.join(OUTDIR_PATH, SAMPLE_ID)
        TEMP_SAMPLE_OUTDIR_PATH = os.path.join(TEMP_OUTDIR_PATH, SAMPLE_ID)
        TEMP_SAMPLE_FETCHDIR_PATH = os.path.join(TEMP_SAMPLE_OUTDIR_PATH, "Input")

        os.makedirs(SAMPLE_OUTDIR_PATH, exist_ok=True)
        os.makedirs(TEMP_SAMPLE_OUTDIR_PATH, exist_ok=True)
        os.makedirs(TEMP_SAMPLE_FETCHDIR_PATH, exist_ok=True)

        SAMPLE_INPUTS_DICT[SAMPLE_ID] = {
            # INPUT INFO
            "read_1_path": READ_1_PATH,
            "read_2_path": READ_2_PATH,
            "read_1_wsl_path": READ_1_WSL_PATH,
            "read_2_wsl_path": READ_2_WSL_PATH,
            "platform": "illumina",
            "average_length": AVERAGE_LENGTH,
            "read_length_type": READ_TYPE,
            }
        SAMPLE_OUTPUTS_DICT[SAMPLE_ID] = {
            "temp_read_1_path": os.path.join(TEMP_SAMPLE_FETCHDIR_PATH, os.path.basename(READ_1_WSL_PATH)),
            "temp_read_2_path": os.path.join(TEMP_SAMPLE_FETCHDIR_PATH, os.path.basename(READ_2_WSL_PATH)),
            # DIRECTORIES
            "temp_sample_fetchdir_path": TEMP_SAMPLE_FETCHDIR_PATH,
            "sample_outdir_path": SAMPLE_OUTDIR_PATH, 
            "temp_sample_outdir_path": TEMP_SAMPLE_FETCHDIR_PATH,
            # MAPPING/ALIGNMENT INFO
            "sample_sam_file": f"{SAMPLE_ID}.sam",
            "sample_sorted_bam_file": f"{SAMPLE_ID}.sorted.bam",
            "sample_marked_bam_file": f"{SAMPLE_ID}.marked.bam",
            "sample_recal_bam_file": f"{SAMPLE_ID}.recal.bam",
            "sample_final_bam_file": f"{SAMPLE_ID}.final.bam",
            # VARIANT INFO
            "sample_gvcf_file": f"{SAMPLE_ID}.g.vcf",
            "sample_vcf_file": f"{SAMPLE_ID}.vcf",
            "sample_final_vcf_file": f"{SAMPLE_ID}.final.vcf",      
        }
        REPORT_OUTPUTS_DICT[SAMPLE_ID] = {
            # REPORT INFO
            "sample_xlsx_file" : f"{SAMPLE_ID}.xlsx"
        }

    COHORT_OUTPUTS_DICT = {
        "cohort_gvcf_file": "cohort.g.vcf",
        "cohort_vcf_file": "cohort.vcf",
        "cohort_filtered_vcf_file": f"cohort.filtered.vcf",
        "cohort_normalized_vcf_file":f"cohort.normalized.vcf",
        # ANNOTAION
        "cohort_genome_annotated_vcf_file": f"cohort.genome_annotated.vcf",
        "cohort_vartype_annotated_vcf_file": f"cohort.vartype_annotated.vcf",
        "cohort_clinvar_annotated_vcf_file": f"cohort.clinvar_annotated.vcf",
        "cohort_p3_1000g_annotated_vcf_file": f"cohort.p3_1000g_annotated.vcf",
        "cohort_dbsnp_annotated_vcf_file": f"cohort.dbsnp_annotated.vcf",
        "cohort_dbnsfp_annotated_vcf_file": f"cohort.dbnsfp_annotated.vcf",
        "cohort_final_vcf_file": f"cohort.final.vcf",

    }
    REFERENCE_DICT = {
        "reference_genome_path": GENOME_PATH,
        "reference_known_sites_list": KNOWN_SITES_LIST
    }

    WORKFLOW_CONFIG = {
        "sample_inputs_dict": SAMPLE_INPUTS_DICT, 
        "reference_dict": REFERENCE_DICT,
        "sample_outputs_dict": SAMPLE_OUTPUTS_DICT, 
        "cohort_outputs_dict": COHORT_OUTPUTS_DICT, 
        "report_outputs_dict": REPORT_OUTPUTS_DICT,
        "outdir_path": OUTDIR_PATH,
        "temp_outdir": TEMP_OUTDIR_PATH
        }

    return WORKFLOW_CONFIG