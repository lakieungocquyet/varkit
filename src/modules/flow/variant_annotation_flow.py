from modules.header import *

def variant_annotation_flow(workflow_config):

    OUTDIR = workflow_config["outdir"]
    COHORT_NORMALIZED_GVCF_FILE = workflow_config["cohort_outputs"]["cohort_normalized_gvcf_file"]
    COHORT_SNPEFF_AND_SNPSIFT_ANNOTATED_GVCF_FILE = workflow_config["cohort_outputs"]["cohort_snpEff_and_snpSift_annotated_gvcf_file"]
    
    # setup_logger(outdir = OUTDIR)
    snpEff_and_snpSift_annotation(
        cohort_normalized_gvcf_file = COHORT_NORMALIZED_GVCF_FILE, 
        outdir = OUTDIR, 
        cohort_snpEff_and_snpSift_annotated_gvcf_file = COHORT_SNPEFF_AND_SNPSIFT_ANNOTATED_GVCF_FILE
        )