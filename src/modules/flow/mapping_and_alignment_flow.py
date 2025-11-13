import time
from modules.header import *

def mapping_and_alignment_flow(workflow_config):
    # Extract data
    OUTDIR = workflow_config["outdir"]
    REFERENCE = workflow_config["reference_dict"]["genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    # setup_logger(outdir = OUTDIR)
    # Function
    for sample_id, info in SAMPLE_INPUTS.items():

        SAMPLE_ID = sample_id
        SAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sam_file"]
        PLATFORM = workflow_config["sample_inputs"][f"{sample_id}"]["platform"]
        READ_1 = workflow_config["sample_inputs"][f"{sample_id}"]["read_1"]
        READ_2 = workflow_config["sample_inputs"][f"{sample_id}"]["read_2"]
        SAMPLE_OUTDIR = workflow_config["sample_inputs"][f"{sample_id}"]["sample_outdir"]

        # start_time = time.time()
        # logging_info(f"Mapping and alignment sample: {sample_id}")
        if info["read_length_type"] == "short":
            mapping_and_alignment_BWA_mem(
                sample_id=SAMPLE_ID,
                platform=PLATFORM,
                forward=READ_1,
                reverse=READ_2,
                reference=REFERENCE,
                outdir=OUTDIR,
                sample_outdir=SAMPLE_OUTDIR,
                sam_file=SAM_FILE
            )
        else:
            mapping_and_alignment_Minimap2(
                sample_id=SAMPLE_ID,
                platform=PLATFORM,
                forward=READ_1,
                reverse=READ_2,
                reference=REFERENCE,
                outdir=OUTDIR,
                sample_outdir=SAMPLE_OUTDIR,
                sam_file=SAM_FILE
            )
    #     end_time = time.time()
    #     duration = (end_time - start_time) / 60  
    #     logging_info(f"{sample_id} finished mapping and alignment in {duration:.2f} minutes")
    # logging_info("All samples finished mapping and alignment step.")