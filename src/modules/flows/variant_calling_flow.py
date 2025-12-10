import time
from modules.header import *

def variant_calling_flow(workflow_config):

    temp_outdir_path = workflow_config["TEMP_OUTDIR_PATH"]
    genome_path = workflow_config["REFERENCE_DICT"]["genome_path"]
    sample_inputs_dict = workflow_config["SAMPLE_INPUTS_DICT"]

    for sample_id, info in sample_inputs_dict.items():
        sample_recal_bam_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_RECAL_BAM_FILE"]
        temp_sample_outdir_path = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["TEMP_SAMPLE_OUTDIR_PATH"]
        sample_genomic_snps_and_indels_vcf_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_GENOMIC_SNPS_AND_INDELS_VCF_FILE"]
        
        start_time = time.time()
        log.info(f"Variant calling sample: {sample_id}")
        call_genomic_snps_and_indels_gatk(
            input_file=sample_recal_bam_file,
            reference_genome=genome_path,
            sample_outdir=temp_sample_outdir_path,
            outdir=temp_outdir_path,
            output_file=sample_genomic_snps_and_indels_vcf_file,
        )
        end_time = time.time()
        duration = (end_time - start_time) / 60  
        log.info(f"{sample_id} finished variant calling in {duration:.2f} minutes")
    log.info("All samples finished variant calling step.")  