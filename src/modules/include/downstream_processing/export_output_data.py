import shutil
from modules.header import *

def export_output_data(workflow_config):
    SAMPLE_OUTPUTS = workflow_config["sample_outputs"]    
    log.info("Exporting output data from workflow...")
    for sample_id, info in SAMPLE_OUTPUTS.items():
        log.info(f"Exporting data for sample: {sample_id}")
        SAMPLE_OUTDIR = SAMPLE_OUTPUTS[sample_id]["sample_outdir"]       
        TEMP_SAMPLE_OUTDIR = SAMPLE_OUTPUTS[sample_id]["temp_sample_outdir"]
    log.info("Output data export completed.")
