from modules.header import *

def upstream_processing_flow(input_yaml):

    KNOWN_SITES_STRING = ""
    GVCF_FILE_STRING = ""

    SAMPLES, GENOME, KNOWN_SITES, OUTDIR = initialize_from_yaml(input_yaml)

    setup_logging(
        outdir = OUTDIR
    )

    log.info("Starting sample preparation step...")
    WORKFLOW_CONFIG = initialize_samples(
        SAMPLES = SAMPLES, 
        GENOME = GENOME, 
        KNOWN_SITES = KNOWN_SITES, 
        OUTDIR = OUTDIR
        )
   
    if KNOWN_SITES:
        for site in KNOWN_SITES:
            KNOWN_SITES_STRING += f"--known-sites {site} "

    for sample_id, info in WORKFLOW_CONFIG["sample_outputs"].items():
        sample_outdir = WORKFLOW_CONFIG["sample_outputs"][sample_id]["sample_outdir"]
        sample_gvcf_file = WORKFLOW_CONFIG["sample_outputs"][sample_id]["sample_gvcf_file"]
        GVCF_FILE_STRING += f" -V {sample_outdir}/{sample_gvcf_file}"  
    
    sample_info = yaml.dump(WORKFLOW_CONFIG["sample_inputs"], sort_keys=False, default_flow_style=False).rstrip()
    log.info(f"Sample information:\n{sample_info}")

    return WORKFLOW_CONFIG, GVCF_FILE_STRING, KNOWN_SITES_STRING