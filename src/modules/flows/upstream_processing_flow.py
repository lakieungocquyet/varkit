import yaml
from modules.header import *

def upstream_processing_flow(input_yaml_path, system_config):

    KNOWN_SITES_STRING = ""
    GVCF_FILE_STRING = ""
    sample_list, genome_path, known_sites_list, outdir_path = load_paths_from_yaml(input_yaml_path)
    setup_logging(
        outdir = outdir_path
    )
    log.info(f"Total samples: {len(sample_list)}")
    log.info(f"Output directory: {outdir_path}")
    log.info("Initializing sample structure...")
    WORKFLOW_CONFIG = initialize_samples(
        sample_list = sample_list, 
        genome_path = genome_path, 
        known_sites_list = known_sites_list, 
        outdir_path = outdir_path
        )
    log.info("Sample initialization completed")
    if known_sites_list:
        log.info(f"Found {len(known_sites_list)} known sites")
        for site in known_sites_list:
            KNOWN_SITES_STRING += f"--known-sites {site} "
            log.debug(f"Added known site: {site}")
    else:
        log.warning("No known sites provided")
    
    for sample_id, info in WORKFLOW_CONFIG["SAMPLE_OUTPUTS_DICT"].items():
        temp_sample_outdir_path = WORKFLOW_CONFIG["SAMPLE_OUTPUTS_DICT"][sample_id]["TEMP_SAMPLE_OUTDIR_PATH"]
        sample_genomic_snps_and_indels_vcf_file = WORKFLOW_CONFIG["SAMPLE_OUTPUTS_DICT"][sample_id]["SAMPLE_GENOMIC_SNPS_AND_INDELS_VCF_FILE"]
        GVCF_FILE_STRING += f" -V {temp_sample_outdir_path}/{sample_genomic_snps_and_indels_vcf_file}"  
    
    sample_info = yaml.dump(
        WORKFLOW_CONFIG["SAMPLE_INPUTS_DICT"], 
        sort_keys=False, 
        default_flow_style=False
        ).rstrip()
    
    log.info(f"Sample information:\n{sample_info}")

    log.info("Fetching input data...")
    fetch_input_data(
        workflow_config = WORKFLOW_CONFIG
    )
    log.info("Input data fetching completed")
    
    return WORKFLOW_CONFIG, GVCF_FILE_STRING, KNOWN_SITES_STRING