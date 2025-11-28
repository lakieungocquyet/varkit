import time
from modules.header import *

def downstream_processing_flow(workflow_config):

    temp_outdir_path = workflow_config["TEMP_OUTDIR_PATH"]
    genome_path = workflow_config["REFERENCE_DICT"]["genome_path"]
    sample_inputs_dict = workflow_config["SAMPLE_INPUTS_DICT"]
    cohort_dbnsfp_annotated_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_DBNSFP_ANNOTATED_SNPS_AND_INDELS_VCF_FILE"]
    cohort_final_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_FINAL_SNPS_AND_INDELS_VCF_FILE"]
    
    sanitize(
        input_file = cohort_dbnsfp_annotated_snps_and_indels_vcf_file,
        outdir = temp_outdir_path, 
        output_file = cohort_final_snps_and_indels_vcf_file
        )
    
    os.remove(f"{temp_outdir_path}/{cohort_dbnsfp_annotated_snps_and_indels_vcf_file}")

    for sample_id, info in sample_inputs_dict.items():
        start_time = time.time()
        log.info(f"Downstream processing sample: {sample_id}")
        sample_id = sample_id
        temp_sample_outdir_path = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["TEMP_SAMPLE_OUTDIR_PATH"]
        sample_snps_and_indels_vcf_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_SNPS_AND_INDELS_VCF_FILE"]

        select_variants_by_sample_gatk(
            input_file = cohort_final_snps_and_indels_vcf_file, 
            sample_id = sample_id, 
            reference_genome = genome_path,
            sample_outdir = temp_sample_outdir_path, 
            outdir = temp_outdir_path, 
            output_file = sample_snps_and_indels_vcf_file
            )
        end_time = time.time()
        duration = (end_time - start_time) / 60 
        log.info(f"{sample_id} finished downstream processing in {duration:.2f} minutes")
    os.remove(f"{temp_outdir_path}/{cohort_final_snps_and_indels_vcf_file}")
    log.info("All samples finished downstream processing step.")