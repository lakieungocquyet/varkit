import time
from modules.header import *
import os

def post_mapping_and_alignment_flow(workflow_config, known_sites_string):

    temp_outdir_path = workflow_config["TEMP_OUTDIR_PATH"]
    genome_path = workflow_config["REFERENCE_DICT"]["genome_path"]
    sample_inputs_dict = workflow_config["SAMPLE_INPUTS_DICT"]

    samtools_ready = check_samtools_index(
        reference_genome = genome_path
        )
    if not samtools_ready:
        log.error(f"Samtools index file missing, creating Samtools index.")
        index_reference_genome_samtools(
            reference_genome = genome_path
            )
    else:
        log.info(f"Samtools index file found, skipping indexing step.")
    
    gatk_ready = check_gatk_index(
        reference_genome = genome_path
        )
    if not gatk_ready:
        log.error(f"GATK index file missing, creating GATK index.")
        index_reference_genome_gatk(
            reference_genome = genome_path
            )
    else:
        log.info(f"GATK index file found, skipping indexing step.")

    for sample_id, info in sample_inputs_dict.items():

        sample_sam_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_SAM_FILE"]
        sample_bam_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_BAM_FILE"]
        temp_sample_outdir_path = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["TEMP_SAMPLE_OUTDIR_PATH"]
        sample_sorted_bam_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_SORTED_BAM_FILE"]
        sample_marked_bam_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_MARKED_BAM_FILE"]
        sample_recal_bam_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_RECAL_BAM_FILE"]

        start_time = time.time()
        log.info(f"Post-mapping and alignment sample: {sample_id}")
        convert_samtools(
            input_file  = sample_sam_file,
            sample_outdir = temp_sample_outdir_path, 
            outdir = temp_outdir_path, 
            output_file = sample_bam_file
            )
        os.remove(f"{temp_sample_outdir_path}/{sample_sam_file}") 
        sort_samtools(
            input_file = sample_bam_file, 
            sample_outdir = temp_sample_outdir_path, 
            outdir = temp_outdir_path, 
            output_file = sample_sorted_bam_file
            ) 
        os.remove(f"{temp_sample_outdir_path}/{sample_bam_file}") 
        markduplicates_gatk(
            input_file=sample_sorted_bam_file,
            sample_outdir=temp_sample_outdir_path,
            outdir=temp_outdir_path,
            output_file=sample_marked_bam_file,
        )
        os.remove(f"{temp_sample_outdir_path}/{sample_sorted_bam_file}")
        recalibrate_bases_gatk(
            input_file=sample_marked_bam_file,
            sample_outdir=temp_sample_outdir_path,
            known_sites_string=known_sites_string,
            reference_genome=genome_path,
            outdir=temp_outdir_path
        )
        apply_bqsr_gatk(
            input_file=sample_marked_bam_file,
            reference_genome=genome_path,
            sample_outdir=temp_sample_outdir_path,
            outdir=temp_outdir_path,
            output_file=sample_recal_bam_file,
        )  
        os.remove(f"{temp_sample_outdir_path}/{sample_marked_bam_file}")
        end_time = time.time()
        duration = (end_time - start_time) / 60  
        log.info(f"{sample_id} finished post-mapping and alignment in {duration:.2f} minutes")
    log.info("All samples finished post-mapping and alignment step.")    