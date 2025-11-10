from modules.header import *

def default_pipeline(INPUT_YAML):
    # [STAGE 1]: UPSTREAM PROCESSING
    OUTDIR, SAMPLE_LIST, REFERENCE_LIST, GLOBAL_GVCF_LIST, GVCF_FILE_STRING, KNOWN_SITES_STRING = upstream_processing_flow(INPUT_YAML = INPUT_YAML)
    setup_logger(outdir = OUTDIR)
    # [STAGE 2]: MAPPING AND ALIGNMENT
    mapping_and_alignment_flow(
        SAMPLE_LIST = SAMPLE_LIST, 
        REFERENCE_LIST = REFERENCE_LIST,
        OUTDIR = OUTDIR
        )
    # [STAGE 3]: POST MAPPING AND ALIGNMENT
    post_mapping_and_alignment_flow(
        SAMPLE_LIST = SAMPLE_LIST, 
        KNOWN_SITES_STRING = KNOWN_SITES_STRING, 
        OUTDIR = OUTDIR
        )
    # [STAGE 4]: VARIANT CALLING
    variant_calling_flow(
        SAMPLE_LIST = SAMPLE_LIST, 
        OUTDIR = OUTDIR
        )
    # [STAGE 5]: POST VARIANT CALLING
    post_variant_calling_flow(
        GVCF_FILE_LIST = GVCF_FILE_STRING,
        SAMPLE_LIST = SAMPLE_LIST, 
        REFERENCE_LIST = REFERENCE_LIST, 
        OUTDIR = OUTDIR,
        GLOBAL_GVCF_LIST = GLOBAL_GVCF_LIST
        )
    # [STAGE 6]: VARIANT ANNOTATION
    variant_annotation_flow(
        GLOBAL_GVCF_LIST = GLOBAL_GVCF_LIST, 
        OUTDIR = OUTDIR, 
        )
    # [STAGE 7]: DOWNSTREAM PROCESSING
    downstream_processing_flow(
        SAMPLE_LIST = SAMPLE_LIST, 
        GLOBAL_GVCF_LIST = GLOBAL_GVCF_LIST, 
        REFERENCE_LIST = REFERENCE_LIST, 
        OUTDIR = OUTDIR
    )
    return 0