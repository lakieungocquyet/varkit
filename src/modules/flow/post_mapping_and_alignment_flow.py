import time
from modules.header import *
import os

def post_mapping_and_alignment_flow(workflow_config, known_sites_string):

    TEMP_OUTDIR = workflow_config["temp_outdir"]
    REFERENCE_GENOME = workflow_config["reference_dict"]["reference_genome"]
    SAMPLE_INPUTS = workflow_config["sample_inputs"]

    samtools_ready = check_samtools_index(REFERENCE_GENOME)
    if not samtools_ready:
        log.error(f"Samtools index file missing for {REFERENCE_GENOME}, creating Samtools index.")
        index_reference_genome_samtools(REFERENCE_GENOME)
    else:
        log.info(f"Samtools index file found for {REFERENCE_GENOME}, skipping indexing step.")
    
    gatk_ready = check_gatk_index(REFERENCE_GENOME)
    if not gatk_ready:
        log.error(f"GATK index file missing for {REFERENCE_GENOME}, creating GATK index.")
        index_reference_genome_gatk(REFERENCE_GENOME)
    else:
        log.info(f"GATK index file found for {REFERENCE_GENOME}, skipping indexing step.")

    for sample_id, info in SAMPLE_INPUTS.items():

        SAMPLE_SAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_sam_file"]
        TEMP_SAMPLE_OUTDIR = workflow_config["sample_outputs"][f"{sample_id}"]["temp_sample_outdir"]
        SAMPLE_SORTED_BAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_sorted_bam_file"]
        SAMPLE_MARKED_BAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_marked_bam_file"]
        SAMPLE_RECAL_BAM_FILE = workflow_config["sample_outputs"][f"{sample_id}"]["sample_recal_bam_file"]

        start_time = time.time()
        log.info(f"Post-mapping and alignment sample: {sample_id}")
        convert_and_sort_Samtools(
            sample_outdir=TEMP_SAMPLE_OUTDIR,
            input_file=SAMPLE_SAM_FILE,
            output_file=SAMPLE_SORTED_BAM_FILE,
            outdir=TEMP_OUTDIR
        )
        os.remove(f"{TEMP_SAMPLE_OUTDIR}/{SAMPLE_SAM_FILE}") 
        markduplicates_GATK(
            input_file=SAMPLE_SORTED_BAM_FILE,
            sample_outdir=TEMP_SAMPLE_OUTDIR,
            outdir=TEMP_OUTDIR,
            output_file=SAMPLE_MARKED_BAM_FILE,
        )
        os.remove(f"{TEMP_SAMPLE_OUTDIR}/{SAMPLE_SORTED_BAM_FILE}")
        recalibrate_bases_GATK(
            input_file=SAMPLE_MARKED_BAM_FILE,
            sample_outdir=TEMP_SAMPLE_OUTDIR,
            known_sites_string=known_sites_string,
            reference_genome=REFERENCE_GENOME,
            outdir=TEMP_OUTDIR
        )
        apply_BQSR_GATK(
            input_file=SAMPLE_MARKED_BAM_FILE,
            reference_genome=REFERENCE_GENOME,
            sample_outdir=TEMP_SAMPLE_OUTDIR,
            outdir=TEMP_OUTDIR,
            output_file=SAMPLE_RECAL_BAM_FILE,
        )  
        os.remove(f"{TEMP_SAMPLE_OUTDIR}/{SAMPLE_MARKED_BAM_FILE}")
        end_time = time.time()
        duration = (end_time - start_time) / 60  
        log.info(f"{sample_id} finished post-mapping and alignment in {duration:.2f} minutes")
    log.info("All samples finished post-mapping and alignment step.")    