import time
from modules.header import *

def downstream_processing_flow(workflow_config):

    OUTDIR = workflow_config["outdir"]
    REFERENCE_GENOME = workflow_config["reference_dict"]["reference_genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    COHORT_SNPEFF_AND_SNPSIFT_ANNOTATED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_snpEff_and_snpSift_annotated_vcf_file"]
    
    for sample_id, info in SAMPLE_INPUTS.items():
        start_time = time.time()
        log.info(f"Downstream processing sample: {sample_id}")
        SAMPLE_ID = sample_id
        SAMPLE_OUTDIR = workflow_config["sample_outputs"][f"{sample_id}"]["sample_outdir"]
        SAMPLE_VCF_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_vcf_file"]
        SAMPLE_FINAL_VCF_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_final_vcf_file"]
        SAMPLE_XLSX_FILE = workflow_config["report_outputs"][f"{sample_id}"]["sample_xlsx_file"]

        select_variant_by_sample(
            cohort_snpEff_and_snpSift_annotated_vcf_file = COHORT_SNPEFF_AND_SNPSIFT_ANNOTATED_VCF_FILE, 
            sample_id = SAMPLE_ID, 
            reference_genome=REFERENCE_GENOME,
            sample_outdir = SAMPLE_OUTDIR, 
            outdir = OUTDIR, 
            sample_vcf_file = SAMPLE_VCF_FILE
            )
        sanitization(
            sample_vcf_file = SAMPLE_VCF_FILE,
            sample_outdir = SAMPLE_OUTDIR, 
            outdir = OUTDIR, 
            sample_final_vcf_file = SAMPLE_FINAL_VCF_FILE
            )
        export_to_XLSX(
            sample_final_vcf_file = SAMPLE_FINAL_VCF_FILE,
            sample_outdir = SAMPLE_OUTDIR, 
            sample_xlsx_file = SAMPLE_XLSX_FILE
            )
        end_time = time.time()
        duration = (end_time - start_time) / 60 
        log.info(f"{sample_id} finished downstream processing in {duration:.2f} minutes")

    log.info("All samples finished downstream processing step.")