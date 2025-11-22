import time
from modules.header import *

def downstream_processing_flow(workflow_config):

    TEMP_OUTDIR = workflow_config["temp_outdir"]
    REFERENCE_GENOME = workflow_config["reference_dict"]["reference_genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    COHORT_DBNSFP_ANNOTATED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_dbnsfp_annotated_vcf_file"]
    COHORT_FINAL_VCF_FILE = workflow_config["cohort_outputs"]["cohort_final_vcf_file"]
    
    sanitize(
        input_file = COHORT_DBNSFP_ANNOTATED_VCF_FILE,
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_FINAL_VCF_FILE
        )
    os.remove(f"{TEMP_OUTDIR}/{COHORT_DBNSFP_ANNOTATED_VCF_FILE}")

    for sample_id, info in SAMPLE_INPUTS.items():
        start_time = time.time()
        log.info(f"Downstream processing sample: {sample_id}")
        SAMPLE_ID = sample_id
        TEMP_SAMPLE_OUTDIR = workflow_config["sample_outputs"][f"{sample_id}"]["temp_sample_outdir"]
        SAMPLE_VCF_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_vcf_file"]

        select_variants_by_sample_GATK(
            input_file = COHORT_FINAL_VCF_FILE, 
            sample_id = SAMPLE_ID, 
            reference_genome = REFERENCE_GENOME,
            sample_outdir = TEMP_SAMPLE_OUTDIR, 
            outdir = TEMP_OUTDIR, 
            output_file = SAMPLE_VCF_FILE
            )
        end_time = time.time()
        duration = (end_time - start_time) / 60 
        log.info(f"{sample_id} finished downstream processing in {duration:.2f} minutes")
    os.remove(f"{TEMP_OUTDIR}/{COHORT_FINAL_VCF_FILE}")
    log.info("All samples finished downstream processing step.")