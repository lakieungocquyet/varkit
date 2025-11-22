from modules.header import *
import shutil

def fetch_input_data(workflow_config):
    SAMPLE_INPUTS_DICT = workflow_config["sample_inputs_dict"]    
    log.info("Importing input data into workflow...")
    for sample_id, sample_info in SAMPLE_INPUTS_DICT.items():
        TEMP_SAMPLE_FETCHDIR = workflow_config["sample_outputs_dict"][sample_id]["temp_sample_fetchdir"]
        READ_1_WSL_PATH = SAMPLE_INPUTS_DICT[sample_id]["read_1_wsl_path"]
        READ_2_WSL_PATH = SAMPLE_INPUTS_DICT[sample_id]["read_2_wsl_path"]
        log.info(f"Importing data for sample: {sample_id}")
        shutil.copy(READ_1_WSL_PATH, TEMP_SAMPLE_FETCHDIR)
        shutil.copy(READ_2_WSL_PATH, TEMP_SAMPLE_FETCHDIR)
    log.info("Input data import completed.")

