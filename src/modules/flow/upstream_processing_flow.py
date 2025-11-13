from modules.header import *

def upstream_processing_flow(input_yaml):
    SAMPLES, GENOME, KNOWN_SITES, OUTDIR = initialize_from_yaml(input_yaml)
    # setup_logger(outdir = OUTDIR)
    KNOWN_SITES_STRING = ""

    if KNOWN_SITES:
        for site in KNOWN_SITES:
            KNOWN_SITES_STRING += f"--known-sites {site} "

    WORKFLOW_CONFIG = init_samples(
        SAMPLES = SAMPLES, 
        GENOME = GENOME, 
        KNOWN_SITES = KNOWN_SITES, 
        OUTDIR = OUTDIR
        )
    
    GVCF_FILE_STRING = ""
    for sample_id, info in WORKFLOW_CONFIG["sample_outputs"].items():
        sample_outdir = WORKFLOW_CONFIG["sample_inputs"][sample_id]["sample_outdir"]
        GVCF_FILE_STRING += f" -V {sample_outdir}/{info['gvcf_file']}"  
    
    # sample_info_str = yaml.dump(
    #     WORKFLOW_CONFIG["sample_inputs"], sort_keys=False, default_flow_style=False
    # )
    # logging_info(f"Sample information:\n{sample_info_str}")

    return WORKFLOW_CONFIG, GVCF_FILE_STRING, KNOWN_SITES_STRING