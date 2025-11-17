import time
from modules.header import *

def mapping_and_alignment_flow(workflow_config):
    # Extract data
    TEMP_OUTDIR = workflow_config["temp_outdir"]
    REFERENCE_GENOME = workflow_config["reference_dict"]["reference_genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    # Function
    for sample_id, info in SAMPLE_INPUTS.items():

        SAMPLE_ID = sample_id
        READ_1 = workflow_config["sample_inputs"][f"{sample_id}"]["read_1"]
        READ_2 = workflow_config["sample_inputs"][f"{sample_id}"]["read_2"]
        PLATFORM = workflow_config["sample_inputs"][f"{sample_id}"]["platform"]
        TEMP_SAMPLE_OUTDIR = workflow_config["sample_outputs"][f"{sample_id}"]["temp_sample_outdir"]
        SAMPLE_SAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_sam_file"]

        start_time = time.time()
        log.info(f"Mapping and alignment sample: {sample_id}")
        if info["read_length_type"] == "short":
            mapping_and_alignment_BWA_mem(
                sample_id=SAMPLE_ID,
                platform=PLATFORM,
                forward=READ_1,
                reverse=READ_2,
                reference_genome=REFERENCE_GENOME,
                outdir=TEMP_OUTDIR,
                sample_outdir=TEMP_SAMPLE_OUTDIR,
                output_file=SAMPLE_SAM_FILE
            )
        else:
            mapping_and_alignment_Minimap2(
                sample_id=SAMPLE_ID,
                platform=PLATFORM,
                forward=READ_1,
                reverse=READ_2,
                reference_genome=REFERENCE_GENOME,
                outdir=TEMP_OUTDIR,
                sample_outdir=TEMP_SAMPLE_OUTDIR,
                output_file=SAMPLE_SAM_FILE
            )
        end_time = time.time()
        duration = (end_time - start_time) / 60  
        log.info(f"{sample_id} finished mapping and alignment in {duration:.2f} minutes")
    log.info("All samples finished mapping and alignment step.")