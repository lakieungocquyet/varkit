import time
from modules.header import *

def downstream_processing_flow(workflow_config):

    OUTDIR = workflow_config["outdir"]
    REFERENCE = workflow_config["reference_dict"]["genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    COHORT_SNPEFF_AND_SNPSIFT_ANNOTATED_GVCF_FILE = workflow_config["cohort_outputs"]["cohort_snpEff_and_snpSift_annotated_gvcf_file"]
    
    setup_logger(outdir = OUTDIR)
    for sample_id, info in SAMPLE_INPUTS.items():

        SAMPLE_ID = sample_id
        SAMPLE_OUTDIR = workflow_config["sample_inputs"][f"{sample_id}"]["sample_outdir"]
        VCF_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["vcf_file"]
        FINAL_VCF_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["final_vcf_file"]
        XLSX_FILE = workflow_config["report_outputs"][f"{sample_id}"]["xlsx_file"]

        select_variant_by_sample(
            cohort_snpEff_and_snpSift_annotated_gvcf_file = COHORT_SNPEFF_AND_SNPSIFT_ANNOTATED_GVCF_FILE, 
            sample_id = SAMPLE_ID, 
            reference = REFERENCE, 
            sample_outdir = SAMPLE_OUTDIR, 
            outdir = OUTDIR, 
            vcf_file = VCF_FILE
            )
        sanitization_vcf_file(
            vcf_file = VCF_FILE, 
            sample_outdir = SAMPLE_OUTDIR, 
            outdir = OUTDIR, 
            final_vcf_file = FINAL_VCF_FILE
            )
        export_to_XLSX(
            final_vcf_file = FINAL_VCF_FILE, 
            sample_outdir = SAMPLE_OUTDIR, 
            xlsx_file = XLSX_FILE
            )
        
    