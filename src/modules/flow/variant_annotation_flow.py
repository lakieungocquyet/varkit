from modules.header import *

def variant_annotation_flow(workflow_config):

    OUTDIR = workflow_config["outdir"]
    COHORT_NORMALIZED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_normalized_vcf_file"]
    COHORT_SNPEFF_AND_SNPSIFT_ANNOTATED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_snpEff_and_snpSift_annotated_vcf_file"]
    
    # setup_logger(outdir = OUTDIR)
    snpEff_and_snpSift_annotation(
        cohort_normalized_vcf_file = COHORT_NORMALIZED_VCF_FILE, 
        outdir = OUTDIR, 
        cohort_snpEff_and_snpSift_annotated_vcf_file = COHORT_SNPEFF_AND_SNPSIFT_ANNOTATED_VCF_FILE
        )