from modules.header import *

def upstream_processing_flow(INPUT_YAML):
    SAMPLES, GENOME, KNOWN_SITES, OUTDIR = initialize_from_yaml(INPUT_YAML)

    KNOWN_SITES_STRING = ""

    if KNOWN_SITES:
        for site in KNOWN_SITES:
            known_sites_string += f"--known-sites {site} "

    SAMPLE_LIST, REFERENCE_LIST, GLOBAL_GVCF_LIST = init_samples(
        SAMPLES = SAMPLES, 
        GENOME = GENOME, 
        KNOWN_SITES = KNOWN_SITES, 
        OUTDIR = OUTDIR
        )
    
    GVCF_FILE_STRING = ""
    for sample_id, info in SAMPLE_LIST.items():
        GVCF_FILE_STRING += f" -V {info['sample_outdir']}/{info['raw_gvcf_file']}"  

    return OUTDIR, SAMPLE_LIST, REFERENCE_LIST, GLOBAL_GVCF_LIST, GVCF_FILE_STRING, KNOWN_SITES_STRING