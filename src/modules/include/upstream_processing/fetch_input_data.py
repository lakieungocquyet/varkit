from modules.header import *
import shutil

def fetch_input_data(workflow_config):
    sample_inputs_dict = workflow_config["SAMPLE_INPUTS_DICT"]    
    log.info("Fetch input data into workflow...")
    for sample_id, sample_info in sample_inputs_dict.items():
        temp_sample_fetchdir = workflow_config["SAMPLE_OUTPUTS_DICT"][sample_id]["TEMP_SAMPLE_FETCHDIR"]
        read_1_wsl_path = sample_inputs_dict[sample_id]["READ_1_WSL_PATH"]
        read_2_wsl_path = sample_inputs_dict[sample_id]["READ_2_WSL_PATH"]
        
        log.info(f"Fetching data for sample: {sample_id}")
        shutil.copy(read_1_wsl_path, temp_sample_fetchdir)
        shutil.copy(read_2_wsl_path, temp_sample_fetchdir)
    log.info("Input data fetch complete.")

