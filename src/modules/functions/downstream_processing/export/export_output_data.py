import shutil
from modules.header import *

def export_output_data(workflow_config):
    sample_outputs_dict = workflow_config["SAMPLE_OUTPUTS_DICT"]    
    log.info("Exporting output data from workflow...")
    for sample_id, info in sample_outputs_dict.items():
        log.info(f"Exporting data for sample: {sample_id}")
        sample_outdir_path = sample_outputs_dict[sample_id]["SAMPLE_OUTDIR_PATH"]
        temp_sample_outdir_path = sample_outputs_dict[sample_id]["TEMP_SAMPLE_OUTDIR_PATH"]
        shutil.copytree(temp_sample_outdir_path, sample_outdir_path, dirs_exist_ok=True)
    log.info("Output data export completed.")
