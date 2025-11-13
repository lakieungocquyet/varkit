import time
from modules.header import *

def variant_calling_flow(workflow_config):

    OUTDIR = workflow_config["outdir"]
    REFERENCE = workflow_config["reference_dict"]["genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    # setup_logger(outdir = OUTDIR)
    for sample_id, info in SAMPLE_INPUTS.items():

        RECAL_BAM_FILE = workflow_config["sample_inputs"][f"{sample_id}"]["recal_bam_file"]
        SAMPLE_OUTDIR = workflow_config["sample_inputs"][f"{sample_id}"]["sample_outdir"]
        GVCF_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["gvcf_file"]
        # start_time = time.time()
        # logging_info(f"Variant calling sample: {sample_id}")
        genomic_SNPs_and_Indels_calling_GATK(
            recal_bam_file=RECAL_BAM_FILE,
            reference=REFERENCE,
            sample_outdir=SAMPLE_OUTDIR,
            outdir=OUTDIR,
            gvcf_file=GVCF_FILE,
        )
        # end_time = time.time()
        # duration = (end_time - start_time) / 60  
        # logging_info(f"{sample_id} finished variant calling in {duration:.2f} minutes")
