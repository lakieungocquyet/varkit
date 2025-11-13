import time
from modules.header import *

def post_mapping_and_alignment_flow(workflow_config, known_sites_string):

    OUTDIR = workflow_config["outdir"]
    REFERENCE = workflow_config["reference_dict"]["genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]
    # setup_logger(outdir = OUTDIR)

    for sample_id, info in SAMPLE_INPUTS.items():

        SAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sam_file"]
        SAMPLE_OUTDIR = workflow_config["sample_inputs"][f"{sample_id}"]["sample_outdir"]
        SORTED_BAM_FILE = workflow_config["sample_inputs"][f"{sample_id}"]["sorted_bam_file"]
        MARKED_BAM_FILE = workflow_config["sample_inputs"][f"{sample_id}"]["marked_bam_file"]
        RECAL_BAM_FILE = workflow_config["sample_inputs"][f"{sample_id}"]["recal_bam_file"]
        # start_time = time.time()
        # logging_info(f"Post-mapping and alignment sample: {sample_id}")

        convert_and_sort(
            sample_outdir=SAMPLE_OUTDIR,
            sam_file=SAM_FILE,
            sorted_bam_file=SORTED_BAM_FILE,
            outdir=OUTDIR
        )
        markduplicates(
            sorted_bam_file=SORTED_BAM_FILE,
            sample_outdir=SAMPLE_OUTDIR,
            outdir=OUTDIR,
            marked_bam_file=MARKED_BAM_FILE,
        )
        baserecalibrator(
            marked_bam_file=MARKED_BAM_FILE,
            sample_outdir=SAMPLE_OUTDIR,
            known_sites_string=known_sites_string,
            reference=REFERENCE,
            outdir=OUTDIR
        )
        applyBQSR(
            marked_bam_file=MARKED_BAM_FILE,
            reference=REFERENCE,
            sample_outdir=SAMPLE_OUTDIR,
            outdir=OUTDIR,
            recal_bam_file=RECAL_BAM_FILE,
        )  
    #     end_time = time.time()
    #     duration = (end_time - start_time) / 60  
    #     logging_info(f"{sample_id} finished post-mapping and alignment in {duration:.2f} minutes")
    # logging_info("All samples finished post-mapping and alignment step.")    