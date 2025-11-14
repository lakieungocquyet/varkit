from modules.header import *

def post_variant_calling_flow(workflow_config, gvcf_file_string):

    OUTDIR = workflow_config["outdir"]
    REFERENCE_GENOME = workflow_config["reference_dict"]["reference_genome"]
    COHORT_GVCF_FILE = workflow_config["cohort_outputs"]["cohort_gvcf_file"]
    COHORT_VCF_FILE = workflow_config["cohort_outputs"]["cohort_vcf_file"]
    COHORT_FILTERED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_filtered_vcf_file"]
    COHORT_NORMALIZED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_normalized_vcf_file"]
    
    # setup_logger(outdir = OUTDIR)
    combine_gvcfs(
        gvcf_file_string = gvcf_file_string,
        reference_genome=REFERENCE_GENOME,
        outdir = OUTDIR,
        cohort_gvcf_file = COHORT_GVCF_FILE
    )
    genotype_gvcfs(
        cohort_gvcf_file = COHORT_GVCF_FILE, 
        reference_genome=REFERENCE_GENOME,
        outdir = OUTDIR, 
        cohort_vcf_file = COHORT_VCF_FILE
        )
    hard_filtration(
        cohort_vcf_file = COHORT_VCF_FILE, 
        reference_genome=REFERENCE_GENOME,
        outdir = OUTDIR, 
        cohort_filtered_vcf_file = COHORT_FILTERED_VCF_FILE
    )
    variant_normalization(
        cohort_filtered_vcf_file = COHORT_FILTERED_VCF_FILE,
        outdir = OUTDIR, 
        cohort_normalized_vcf_file = COHORT_NORMALIZED_VCF_FILE
        )
