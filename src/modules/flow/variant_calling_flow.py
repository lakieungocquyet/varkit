import time
from modules.header import *

def variant_calling_flow(workflow_config):

    OUTDIR = workflow_config["outdir"]
    REFERENCE_GENOME = workflow_config["reference_dict"]["reference_genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    # setup_logger(outdir = OUTDIR)
    for sample_id, info in SAMPLE_INPUTS.items():
        SAMPLE_RECAL_BAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_recal_bam_file"]
        SAMPLE_OUTDIR = workflow_config["sample_outputs"][f"{sample_id}"]["sample_outdir"]
        SAMPLE_GVCF_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_gvcf_file"]
        # start_time = time.time()
        # logging_info(f"Variant calling sample: {sample_id}")
        genomic_SNPs_and_Indels_calling_GATK(
            sample_recal_bam_file=SAMPLE_RECAL_BAM_FILE,
            reference_genome=REFERENCE_GENOME,
            sample_outdir=SAMPLE_OUTDIR,
            outdir=OUTDIR,
            sample_gvcf_file=SAMPLE_GVCF_FILE,
        )
        # end_time = time.time()
        # duration = (end_time - start_time) / 60  
        # logging_info(f"{sample_id} finished variant calling in {duration:.2f} minutes")
