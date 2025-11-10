from modules.header import *

def variant_calling_flow(SAMPLE_LIST, OUTDIR):
    for sample_id, info in SAMPLE_LIST.items():
        start_time = time.time()
        logging.info(f"Variant calling sample: {sample_id}")
        genomic_SNPs_and_Indels_calling_GATK(
            RECAL_BAM_FILE=info["recal_bam_file"],
            REFERENCE=REFERENCE_LIST["genome"],
            SAMPLE_OUTDIR=info["sample_outdir"],
            OUTDIR=OUTDIR,
            RAW_GVCF_FILE=info["raw_gvcf_file"],
        )
        end_time = time.time()
        duration = (end_time - start_time) / 60  
        logging.info(f"{sample_id} finished variant calling in {duration:.2f} minutes")
