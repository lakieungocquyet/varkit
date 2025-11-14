import time
from modules.header import *

def post_mapping_and_alignment_flow(workflow_config, known_sites_string):

    OUTDIR = workflow_config["outdir"]
    REFERENCE_GENOME = workflow_config["reference_dict"]["reference_genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    # setup_logger(outdir = OUTDIR)

    for sample_id, info in SAMPLE_INPUTS.items():

        SAMPLE_SAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_sam_file"]
        SAMPLE_OUTDIR = workflow_config["sample_outputs"][f"{sample_id}"]["sample_outdir"]
        SAMPLE_SORTED_BAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_sorted_bam_file"]
        SAMPLE_MARKED_BAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_marked_bam_file"]
        SAMPLE_RECAL_BAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_recal_bam_file"]
        # start_time = time.time()
        # logging_info(f"Post-mapping and alignment sample: {sample_id}")

        convert_and_sort(
            sample_outdir=SAMPLE_OUTDIR,
            sample_sam_file=SAMPLE_SAM_FILE,
            sample_sorted_bam_file=SAMPLE_SORTED_BAM_FILE,
            outdir=OUTDIR
        )
        markduplicates(
            sample_sorted_bam_file=SAMPLE_SORTED_BAM_FILE,
            sample_outdir=SAMPLE_OUTDIR,
            outdir=OUTDIR,
            sample_marked_bam_file=SAMPLE_MARKED_BAM_FILE,
        )
        baserecalibrator(
            sample_marked_bam_file=SAMPLE_MARKED_BAM_FILE,
            sample_outdir=SAMPLE_OUTDIR,
            known_sites_string=known_sites_string,
            reference_genome=REFERENCE_GENOME,
            outdir=OUTDIR
        )
        applyBQSR(
            sample_marked_bam_file=SAMPLE_MARKED_BAM_FILE,
            reference_genome=REFERENCE_GENOME,
            sample_outdir=SAMPLE_OUTDIR,
            outdir=OUTDIR,
            sample_recal_bam_file=SAMPLE_RECAL_BAM_FILE,
        )  
    #     end_time = time.time()
    #     duration = (end_time - start_time) / 60  
    #     logging_info(f"{sample_id} finished post-mapping and alignment in {duration:.2f} minutes")
    # logging_info("All samples finished post-mapping and alignment step.")    