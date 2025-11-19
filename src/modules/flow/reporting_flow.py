import time
from modules.header import *

def downstream_processing_flow(workflow_config):

    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    
    for sample_id, info in SAMPLE_INPUTS.items():

        start_time = time.time()
        log.info(f"Downstream processing sample: {sample_id}")

        TEMP_SAMPLE_OUTDIR = workflow_config["sample_outputs"][f"{sample_id}"]["temp_sample_outdir"]
        SAMPLE_VCF_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_vcf_file"]
        SAMPLE_XLSX_FILE = workflow_config["report_outputs"][f"{sample_id}"]["sample_xlsx_file"]

        generate_XLSX_report(
            input_file = SAMPLE_VCF_FILE,
            sample_outdir = TEMP_SAMPLE_OUTDIR, 
            output_file = SAMPLE_XLSX_FILE
            )
        
        end_time = time.time()
        duration = (end_time - start_time) / 60 
        log.info(f"{sample_id} finished downstream processing in {duration:.2f} minutes")

    log.info("All samples finished downstream processing step.")