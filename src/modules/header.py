import os
import logging
import time
import sys
from modules.include.upstream_processing.init_samples import *
from modules.include.mapping_and_alignment.check_average_read_length import check_average_read_length
from modules.include.mapping_and_alignment.mapping_and_alignment_BWA_mem import mapping_and_alignment_BWA_mem
from modules.include.mapping_and_alignment.mapping_and_alignment_Minimap2 import mapping_and_alignment_Minimap2
from modules.include.post_mapping_and_alignment.convert_and_sort import convert_and_sort
from modules.include.post_mapping_and_alignment.markduplicates import markduplicates
from modules.include.post_mapping_and_alignment.baserecalibrator_and_applyBQSR import baserecalibrator, applyBQSR
from modules.include.variant_calling.genomic_SNPs_and_Indels_calling_GATK import genomic_SNPs_and_Indels_calling_GATK
from modules.include.post_variant_calling.genomic_variant_combination import combine_gvcfs
from modules.include.post_variant_calling.variant_normalization import variant_normalization
from modules.include.post_variant_calling.variant_filtration import hard_filtration
from modules.flow.mapping_and_alignment_flow import mapping_and_alignment_flow
from modules.flow.post_mapping_and_alignment_flow import post_mapping_and_alignment_flow
from modules.flow.variant_calling_flow import variant_calling_flow
from modules.flow.post_variant_calling_flow import post_variant_calling_flow
# Set Java options for memory management
env = os.environ.copy()
env["JAVA_OPTS"] = "-Xmx8g"

def setup_logger(outdir: str):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(f"{outdir}/runtime.log", mode="a", encoding="utf-8"),
            logging.StreamHandler(sys.stdout)
        ]
    )