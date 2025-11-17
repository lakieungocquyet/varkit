from modules.header import *

def post_variant_calling_flow(workflow_config, gvcf_file_string):

    TEMP_OUTDIR = workflow_config["temp_outdir"]
    REFERENCE_GENOME = workflow_config["reference_dict"]["reference_genome"]
    COHORT_GVCF_FILE = workflow_config["cohort_outputs"]["cohort_gvcf_file"]
    COHORT_VCF_FILE = workflow_config["cohort_outputs"]["cohort_vcf_file"]
    COHORT_FILTERED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_filtered_vcf_file"]
    COHORT_NORMALIZED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_normalized_vcf_file"]
    
    combine_gvcfs(
        gvcf_file_string = gvcf_file_string,
        reference_genome=REFERENCE_GENOME,
        outdir = TEMP_OUTDIR,
        output_file = COHORT_GVCF_FILE
    )
    genotype_gvcfs(
        input_file = COHORT_GVCF_FILE, 
        reference_genome=REFERENCE_GENOME,
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_VCF_FILE
        )
    hard_filtration(
        input_file = COHORT_VCF_FILE, 
        reference_genome=REFERENCE_GENOME,
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_FILTERED_VCF_FILE
    )
    variant_normalization(
        input_file = COHORT_FILTERED_VCF_FILE,
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_NORMALIZED_VCF_FILE
        )
