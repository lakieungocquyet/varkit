from modules.header import *

def post_variant_calling_flow(GVCF_FILE_STRING, REFERENCE_LIST, OUTDIR, GLOBAL_GVCF_LIST):
    setup_logger(outdir = OUTDIR)
    combine_gvcfs(
        GVCF_FILE_STRING = GVCF_FILE_STRING,
        REFERENCE = REFERENCE_LIST["genome"],
        OUTDIR = OUTDIR,
        COMBINED_GVCF_FILE = GLOBAL_GVCF_LIST["combined_gvcf_file"]
    )
    genotype_gvcfs(
        COMBINED_GVCF_FILE = GLOBAL_GVCF_LIST["combined_gvcf_file"], 
        REFERENCE = REFERENCE_LIST["genome"], 
        OUTDIR = OUTDIR, 
        COHORT_GVCF_FILE = GLOBAL_GVCF_LIST["cohort_gvcf_file"]
        )
    hard_filtration(
        COHORT_GVCF_FILE = GLOBAL_GVCF_LIST["cohort_gvcf_file"], 
        REFERENCE = REFERENCE_LIST["genome"],
        OUTDIR = OUTDIR, 
        FILTERED_GVCF_FILE = GLOBAL_GVCF_LIST["filtered_gvcf_file"]
    )
    variant_normalization(
        FILTERED_GVCF_FILE = GLOBAL_GVCF_LIST["filtered_gvcf_file"],  
        OUTDIR = OUTDIR, 
        NORMALIZED_GVCF_FILE = GLOBAL_GVCF_LIST["normalized_gvcf_file"]
        )
