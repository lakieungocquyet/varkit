from modules.header import *

def post_variant_calling_flow(workflow_config, gvcf_file_string):

    OUTDIR = workflow_config["outdir"]
    REFERENCE = workflow_config["reference_dict"]["genome"]
    COMBINATION_GVCF_FILE = workflow_config["cohort_outputs"]["combination_gvcf_file"]
    COHORT_GVCF_FILE = workflow_config["cohort_outputs"]["cohort_gvcf_file"]
    COHORT_FILTERED_GVCF_FILE = workflow_config["cohort_outputs"]["cohort_filtered_gvcf_file"]
    COHORT_NORMALIZED_GVCF_FILE = workflow_config["cohort_outputs"]["cohort_normalized_gvcf_file"]
    
    # setup_logger(outdir = OUTDIR)
    combine_gvcfs(
        gvcf_file_string = gvcf_file_string,
        reference = REFERENCE,
        outdir = OUTDIR,
        combination_gvcf_file = COMBINATION_GVCF_FILE
    )
    genotype_gvcfs(
        combination_gvcf_file = COMBINATION_GVCF_FILE, 
        reference = REFERENCE, 
        outdir = OUTDIR, 
        cohort_gvcf_file = COHORT_GVCF_FILE
        )
    hard_filtration(
        cohort_gvcf_file = COHORT_GVCF_FILE, 
        reference = REFERENCE,
        outdir = OUTDIR, 
        cohort_filtered_gvcf_file = COHORT_FILTERED_GVCF_FILE
    )
    variant_normalization(
        cohort_filtered_gvcf_file = COHORT_FILTERED_GVCF_FILE,  
        outdir = OUTDIR, 
        cohort_normalized_gvcf_file = COHORT_NORMALIZED_GVCF_FILE
        )
