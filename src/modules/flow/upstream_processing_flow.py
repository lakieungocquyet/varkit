from modules.header import *

def upstream_processing_flow(INPUT_YAML):
    SAMPLES, GENOME, KNOWN_SITES, OUTDIR = initialize_from_yaml(INPUT_YAML)
    setup_logger(outdir = OUTDIR)
    KNOWN_SITES_STRING = ""

    if KNOWN_SITES:
        for site in KNOWN_SITES:
            KNOWN_SITES_STRING += f"--known-sites {site} "

    SAMPLE_LIST, REFERENCE_LIST, GLOBAL_GVCF_LIST = init_samples(
        SAMPLES = SAMPLES, 
        GENOME = GENOME, 
        KNOWN_SITES = KNOWN_SITES, 
        OUTDIR = OUTDIR
        )
    
    GVCF_FILE_STRING = ""
    for sample_id, info in SAMPLE_LIST.items():
        GVCF_FILE_STRING += f" -V {info['sample_outdir']}/{info['raw_gvcf_file']}"  
    logging_info(f"Sample information:\n{yaml.dump(SAMPLE_LIST, sort_keys=False, default_flow_style=False)}")

    return OUTDIR, SAMPLE_LIST, REFERENCE_LIST, GLOBAL_GVCF_LIST, GVCF_FILE_STRING, KNOWN_SITES_STRING