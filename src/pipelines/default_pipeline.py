from modules.header import *

def default_pipeline(INPUT_YAML):

    SAMPLES, GENOME, KNOWN_SITES, OUTDIR = initialize_from_yaml(
        INPUT_YAML = INPUT_YAML
        )
    known_sites_string = ""
    if KNOWN_SITES:
        for site in KNOWN_SITES:
            known_sites_string += f"--known-sites {site} "
    SAMPLE_LIST, REFERENCE_LIST, GLOBAL_GVCF_LIST = init_samples(
        SAMPLES = SAMPLES, 
        GENOME = GENOME, 
        KNOWN_SITES = KNOWN_SITES, 
        OUTDIR = OUTDIR
        )
    
    setup_logger(outdir = OUTDIR)
    # [STAGE 1]: MAPPING AND ALIGNMENT
    mapping_and_alignment_flow(
        SAMPLE_LIST = SAMPLE_LIST, 
        REFERENCE_LIST = REFERENCE_LIST,
        OUTDIR = OUTDIR
        )
    # [STAGE 2]: POST MAPPING AND ALIGNMENT
    post_mapping_and_alignment_flow(
        SAMPLE_LIST = SAMPLE_LIST, 
        known_sites_string = known_sites_string, 
        OUTDIR = OUTDIR
        )
    # [STAGE 3]: VARIANT CALLING
    variant_calling_flow(
        SAMPLE_LIST = SAMPLE_LIST, 
        OUTDIR = OUTDIR
        )
    # [STAGE 4]: POST VARIANT CALLING
    post_variant_calling_flow(
        SAMPLE_LIST = SAMPLE_LIST, 
        REFERENCE_LIST = REFERENCE_LIST, 
        OUTDIR = OUTDIR,
        GLOBAL_GVCF_LIST = GLOBAL_GVCF_LIST
        )
    # [STAGE 5]: VARIANT ANNOTATION
    variant_annotation_flow(
        GLOBAL_GVCF_LIST = GLOBAL_GVCF_LIST, 
        OUTDIR = OUTDIR, 
        )

    return 0