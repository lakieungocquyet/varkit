import time
import os
from modules.header import *

def downstream_processing_flow(workflow_config):
    temp_outdir_path = workflow_config["TEMP_OUTDIR_PATH"]
    genome_path = workflow_config["REFERENCE_DICT"]["genome_path"]
    sample_inputs_dict = workflow_config["SAMPLE_INPUTS_DICT"]
    cohort_dbnsfp_annotated_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_DBNSFP_ANNOTATED_SNPS_AND_INDELS_VCF_FILE"]

    for sample_id, info in sample_inputs_dict.items():
        start_time = time.time()
        log.info(f"Downstream processing sample: {sample_id}")
        sample_id = sample_id
        temp_sample_outdir_path = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["TEMP_SAMPLE_OUTDIR_PATH"]
        sample_snps_and_indels_vcf_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_SNPS_AND_INDELS_VCF_FILE"]
        sample_final_snps_and_indels_vcf_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_FINAL_SNPS_AND_INDELS_VCF_FILE"]
        sample_snps_and_indels_xlsx_file = workflow_config["REPORT_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_SNPS_AND_INDELS_XLSX_FILE"]
        
        log.info(f"Extract variants for sample: {sample_id}")
        select_variants_by_sample_gatk(
            input_file = cohort_dbnsfp_annotated_snps_and_indels_vcf_file, 
            sample_id = sample_id, 
            reference_genome = genome_path,
            sample_outdir = temp_sample_outdir_path, 
            outdir = temp_outdir_path, 
            output_file = sample_snps_and_indels_vcf_file
            ) 
        sanitize(
            input_file = sample_snps_and_indels_vcf_file,
            outdir = temp_outdir_path, 
            output_file = sample_final_snps_and_indels_vcf_file
        )
        os.remove(f"{temp_sample_outdir_path}/{sample_snps_and_indels_vcf_file}")
        log.info(f"Reporting sample: {sample_id}")
        generate_XLSX_report(
            input_file = sample_final_snps_and_indels_vcf_file,
            sample_outdir = temp_sample_outdir_path, 
            output_file = sample_snps_and_indels_xlsx_file
            )
        
        end_time = time.time()
        duration = (end_time - start_time) / 60 
        log.info(f"{sample_id} finished downstream processing in {duration:.2f} minutes")
    os.remove(f"{temp_outdir_path}/{cohort_dbnsfp_annotated_snps_and_indels_vcf_file}")
    log.info("Exporting")
    export_output_data(
        workflow_config = workflow_config
        )
    log.info("All samples finished downstream processing step.")