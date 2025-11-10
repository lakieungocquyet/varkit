from modules.header import *

def post_mapping_and_alignment_flow(SAMPLE_LIST, known_sites_string, OUTDIR):
    for sample_id, info in SAMPLE_LIST.items():
        start_time = time.time()
        logging.info(f"Post-mapping and alignment sample: {sample_id}")
        convert_and_sort(
            SAMPLE_OUTDIR=info["sample_outdir"],
            SAM_FILE=info["sam_file"],
            SORTED_BAM_FILE=info["sorted_bam_file"],
            OUTDIR=OUTDIR
        )
        markduplicates(
            SORTED_BAM_FILE=info["sorted_bam_file"],
            SAMPLE_OUTDIR=info["sample_outdir"],
            OUTDIR=OUTDIR,
            MARKED_BAM_FILE=info["marked_bam_file"],
        )
        baserecalibrator(
            MARKED_BAM_FILE=info["marked_bam_file"],
            SAMPLE_OUTDIR=info["sample_outdir"],
            KNOWN_SITES=known_sites_string,
            REFERENCE=REFERENCE_LIST["genome"],
            OUTDIR=OUTDIR
        )
        applyBQSR(
            MARKED_BAM_FILE=info["marked_bam_file"],
            REFERENCE=REFERENCE_LIST["genome"],
            SAMPLE_OUTDIR=info["sample_outdir"],
            OUTDIR=OUTDIR,
            RECAL_BAM_FILE=info["recal_bam_file"],
        )  
        end_time = time.time()
        duration = (end_time - start_time) / 60  
        logging.info(f"{sample_id} finished post-mapping and alignment in {duration:.2f} minutes")
logging.info("All samples finished post-mapping and alignment step.")    