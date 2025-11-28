import time
from modules.header import *

def reporting_flow(workflow_config):

    sample_inputs_dict = workflow_config["SAMPLE_INPUTS_DICT"]
    
    for sample_id, info in sample_inputs_dict.items():

        start_time = time.time()
        log.info(f"Reporting sample: {sample_id}")

        temp_sample_outdir_path = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["TEMP_SAMPLE_OUTDIR_PATH"]

        sample_snps_and_indels_vcf_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_SNPS_AND_INDELS_VCF_FILE"]
        sample_snps_and_indels_xlsx_file = workflow_config["REPORT_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_SNPS_AND_INDELS_XLSX_FILE"]

        generate_XLSX_report(
            input_file = sample_snps_and_indels_vcf_file,
            sample_outdir = temp_sample_outdir_path, 
            output_file = sample_snps_and_indels_xlsx_file
            )
        end_time = time.time()
        duration = (end_time - start_time) / 60 
        log.info(f"{sample_id} finished reporting in {duration:.2f} minutes")

    log.info("All samples finished reporting step.")