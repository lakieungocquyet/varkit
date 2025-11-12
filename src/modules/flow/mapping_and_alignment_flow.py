import time
from modules.header import *

def mapping_and_alignment_flow(SAMPLE_LIST, REFERENCE_LIST, OUTDIR):
    setup_logger(outdir = OUTDIR)
    for sample_id, info in SAMPLE_LIST.items():
        start_time = time.time()
        logging_info(f"Mapping and alignment sample: {sample_id}")
        if info["read_length_type"] == "short":
            mapping_and_alignment_BWA_mem(
                SAMPLE_ID=sample_id,
                PLATFORM=info["platform"],
                FORWARD=info["read1"],
                REVERSE=info["read2"],
                REFERENCE=REFERENCE_LIST["genome"],
                OUTDIR=OUTDIR,
                SAMPLE_OUTDIR=info["sample_outdir"],
                SAM_FILE=info["sam_file"]
            )
        else:
            mapping_and_alignment_Minimap2(
                SAMPLE_ID=sample_id,
                PLATFORM=info["platform"],
                FORWARD=info["read1"],
                REVERSE=info["read2"],
                REFERENCE=REFERENCE_LIST["genome"],
                OUTDIR=OUTDIR,
                SAMPLE_OUTDIR=info["sample_outdir"],
                SAM_FILE=info["sam_file"]
            )
        end_time = time.time()
        duration = (end_time - start_time) / 60  
        logging_info(f"{sample_id} finished mapping and alignment in {duration:.2f} minutes")
    logging_info("All samples finished mapping and alignment step.")