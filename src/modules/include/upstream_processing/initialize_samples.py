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

def initialize_from_yaml(input_yaml_path):
    with open(f"{input_yaml_path}", "r") as f:
        input = yaml.safe_load(f)
        sample_list = input["input_paths"]["sample"]
        genome_path = input["input_paths"]["reference"]["genome"]
        known_sites_list = input["input_paths"]["reference"]["known_site"]
        outdir_path = input["input_paths"]["output"]["directory"]
    return sample_list, genome_path, known_sites_list, outdir_path

def initialize_samples(sample_list, genome_path, known_sites_list, outdir_path):
    temp_outdir_path = create_temp_outdir(
        root = "/opt/varkit/jobspace"
    )
    for sample in sample_list:
        sample_id = sample["id"]
        read_1_path = sample["read1"]
        read_2_path = sample["read2"]
        platform = sample["platform"] if sample.get("platform") else "undefined"
        read_1_wsl_path = translate_path(read_1_path)
        read_2_wsl_path = translate_path(read_2_path)
        forward_average_length = check_average_read_length(read_1_wsl_path)
        reverse_average_length = check_average_read_length(read_2_wsl_path)
        average_length = (forward_average_length + reverse_average_length) / 2   
        if average_length >= 200:
            read_type = "long"
        else:
            read_type = "short"

        sample_outdir_path = os.path.join(outdir_path, sample_id)
        temp_sample_outdir_path = os.path.join(temp_outdir_path, sample_id)
        temp_sample_fetchdir_path = os.path.join(temp_sample_outdir_path, "Input")

        os.makedirs(sample_outdir_path, exist_ok=True)
        os.makedirs(temp_sample_outdir_path, exist_ok=True)
        os.makedirs(temp_sample_fetchdir_path, exist_ok=True)

        SAMPLE_INPUTS_DICT[sample_id] = {
            # INPUT INFO
            "READ_1_PATH": read_1_path,
            "READ_2_PATH": read_2_path,
            "READ_1_WSL_PATH": read_1_wsl_path,
            "READ_2_WSL_PATH": read_2_wsl_path,
            "TEMP_READ_1_PATH": os.path.join(temp_sample_fetchdir_path, os.path.basename(read_1_wsl_path)),
            "TEMP_READ_2_PATH": os.path.join(temp_sample_fetchdir_path, os.path.basename(read_2_wsl_path)),
            "PLATFORM": platform,
            "AVERAGE_LENGTH": average_length,
            "READ_LENGTH_TYPE": read_type,
            }
        SAMPLE_OUTPUTS_DICT[sample_id] = {
            # DIRECTORIES
            "TEMP_SAMPLE_FETCHDIR_PATH": temp_sample_fetchdir_path,
            "SAMPLE_OUTDIR_PATH": sample_outdir_path, 
            "TEMP_SAMPLE_OUTDIR_PATH": temp_sample_outdir_path,
            # MAPPING/ALIGNMENT INFO
            "SAMPLE_SAM_FILE": f"{sample_id}.sam",
            "SAMPLE_BAM_FILE": f"{sample_id}.bam",
            "SAMPLE_SORTED_BAM_FILE": f"{sample_id}.sorted.bam",
            "SAMPLE_MARKED_BAM_FILE": f"{sample_id}.marked.bam",
            "SAMPLE_RECAL_BAM_FILE": f"{sample_id}.recal.bam",
            "SAMPLE_FINAL_BAM_FILE": f"{sample_id}.final.bam",
            # VARIANT INFO
                # SNPS AND INDELS
            "SAMPLE_GENOMIC_SNPS_AND_INDELS_VCF_FILE": f"{sample_id}.snps_and_indels.g.vcf",
            "SAMPLE_SNPS_AND_INDELS_VCF_FILE": f"{sample_id}.snps_and_indels.vcf",
            "SAMPLE_FINAL_SNPS_AND_INDELS_VCF_FILE": f"{sample_id}.snps_and_indels.final.vcf",      
                # 
        }
        REPORT_OUTPUTS_DICT[sample_id] = {
            # REPORT INFO
            "SAMPLE_SNPS_AND_INDELS_XLSX_FILE" : f"{sample_id}.snps_and_indels.xlsx"
        }

    COHORT_OUTPUTS_DICT = {
        "COHORT_GENOMIC_SNPS_AND_INDELS_VCF_FILE": "cohort.snps_and_indels.g.vcf",
        "COHORT_SNPS_AND_INDELS_VCF_FILE": "cohort.snps_and_indels.vcf",
        "COHORT_FILTERED_SNPS_AND_INDELS_VCF_FILE": f"cohort.snps_and_indels.filtered.vcf",
        "COHORT_NORMALIZED_SNPS_AND_INDELS_VCF_FILE":f"cohort.snps_and_indels.normalized.vcf",
        # ANNOTAION
        "COHORT_GENOME_ANNOTATED_SNPS_AND_INDELS_VCF_FILE": f"cohort.snps_and_indels.genome_annotated.vcf",
        "COHORT_VARTYPE_ANNOTATED_SNPS_AND_INDELS_VCF_FILE": f"cohort.snps_and_indels.vartype_annotated.vcf",
        "COHORT_CLINVAR_ANNOTATED_SNPS_AND_INDELS_VCF_FILE": f"cohort.snps_and_indels.clinvar_annotated.vcf",
        "COHORT_P3_1000G_ANNOTATED_SNPS_AND_INDELS_VCF_FILE": f"cohort.snps_and_indels.p3_1000g_annotated.vcf",
        "COHORT_DBSNP_ANNOTATED_SNPS_AND_INDELS_VCF_FILE": f"cohort.snps_and_indels.dbsnp_annotated.vcf",
        "COHORT_DBNSFP_ANNOTATED_SNPS_AND_INDELS_VCF_FILE": f"cohort.snps_and_indels.dbnsfp_annotated.vcf",
        "COHORT_FINAL_SNPS_AND_INDELS_VCF_FILE": f"cohort.snps_and_indels.final.vcf",

    }
    REFERENCE_DICT = {
        "REFERENCE_GENOME_PATH": genome_path,
        "REFERENCE_KNOWN_SITES_LIST": known_sites_list
    }

    WORKFLOW_CONFIG = {
        "SAMPLE_INPUTS_DICT": SAMPLE_INPUTS_DICT, 
        "REFERENCE_DICT": REFERENCE_DICT,
        "SAMPLE_OUTPUTS_DICT": SAMPLE_OUTPUTS_DICT, 
        "COHORT_OUTPUTS_DICT": COHORT_OUTPUTS_DICT, 
        "REPORT_OUTPUTS_DICT": REPORT_OUTPUTS_DICT,
        "OUTDIR_PATH": outdir_path,
        "TEMP_OUTDIR_PATH": temp_outdir_path
        }

    return WORKFLOW_CONFIG