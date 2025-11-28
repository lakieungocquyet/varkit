import time
from modules.header import *

def mapping_and_alignment_flow(workflow_config):
    temp_outdir_path = workflow_config["TEMP_OUTDIR_PATH"]
    genome_path = workflow_config["REFERENCE_DICT"]["genome_path"]
    sample_inputs_dict = workflow_config["SAMPLE_INPUTS_DICT"]

    for sample_id, info in sample_inputs_dict.items():

        sample_id = sample_id
        temp_read_1_path = workflow_config["SAMPLE_INPUTS_DICT"][f"{sample_id}"]["TEMP_READ_1_PATH"]
        temp_read_2_path = workflow_config["SAMPLE_INPUTS_DICT"][f"{sample_id}"]["TEMP_READ_2_PATH"]
        platform = workflow_config["SAMPLE_INPUTS_DICT"][f"{sample_id}"]["PLATFORM"]
        temp_sample_outdir_path = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["TEMP_SAMPLE_OUTDIR_PATH"]
        sample_sam_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_SAM_FILE"]

        start_time = time.time()
        log.info(f"Mapping and alignment sample: {sample_id}")
        if info["READ_LENGTH_TYPE"] == "short":

            bwa_ready , missing_files = check_bwa_index(
                reference_genome = genome_path
            )

            if not bwa_ready:
                log.info(f"BWA index files missing: {missing_files}")
                index_reference_genome_bwa(
                    reference_genome = genome_path
                )
            else:
                log.info(f"BWA index files found, skipping indexing step.")

            map_and_align_bwa_mem(
                sample_id=sample_id,
                platform=platform,
                read_1=temp_read_1_path,
                read_2=temp_read_2_path,
                reference_genome=genome_path,
                outdir=temp_outdir_path,
                sample_outdir=temp_sample_outdir_path,
                output_file=sample_sam_file
            )
        else:
            minimap2_ready = check_minimap2_index(
                reference_genome = genome_path
            )
            if not minimap2_ready:
                log.info(f"Minimap2 index file missing, creating Minimap2 index.")
                index_reference_genome_minimap2(
                    reference_genome = genome_path
                )
            else:
                log.info(f"Minimap2 index file found, skipping indexing step.")
            map_and_align_minimap2(
                sample_id=sample_id,
                platform=platform,
                read_1=temp_read_1_path,
                read_2=temp_read_2_path,
                reference_genome=genome_path,
                outdir=temp_outdir_path,
                sample_outdir=temp_sample_outdir_path,
                output_file=sample_sam_file
            )
        end_time = time.time()
        duration = (end_time - start_time) / 60  
        log.info(f"{sample_id} finished mapping and alignment in {duration:.2f} minutes")
    log.info("All samples finished mapping and alignment step.")