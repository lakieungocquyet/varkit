import time
from modules.header import *

def variant_calling_flow(workflow_config):

    TEMP_OUTDIR = workflow_config["temp_outdir"]
    REFERENCE_GENOME = workflow_config["reference_dict"]["reference_genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]

    for sample_id, info in SAMPLE_INPUTS.items():
        SAMPLE_RECAL_BAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_recal_bam_file"]
        TEMP_SAMPLE_OUTDIR = workflow_config["sample_outputs"][f"{sample_id}"]["temp_sample_outdir"]
        SAMPLE_GVCF_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_gvcf_file"]
        
        start_time = time.time()
        log.info(f"Variant calling sample: {sample_id}")
        call_genomic_snps_and_indels__GATK(
            input_file=SAMPLE_RECAL_BAM_FILE,
            reference_genome=REFERENCE_GENOME,
            sample_outdir=TEMP_SAMPLE_OUTDIR,
            outdir=TEMP_OUTDIR,
            output_file=SAMPLE_GVCF_FILE,
        )
        end_time = time.time()
        duration = (end_time - start_time) / 60  
        log.info(f"{sample_id} finished variant calling in {duration:.2f} minutes")
    log.info("All samples finished variant calling step.")  