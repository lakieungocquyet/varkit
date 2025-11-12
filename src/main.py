import yaml
import argparse
import sys
import subprocess
import os
import logging
import time
sys.dont_write_bytecode = True
from modules.header import *
from pipelines.default_pipeline import *

parser = argparse.ArgumentParser(description="None")
parser.add_argument("-I", "--input",required=True, type=str, help="None")
args = parser.parse_args()
INPUT_YAML = args.input

OUTDIR, SAMPLE_LIST, REFERENCE_LIST, GLOBAL_GVCF_LIST, GVCF_FILE_STRING, KNOWN_SITES_STRING = upstream_processing_flow(INPUT_YAML = INPUT_YAML)


default_pipeline(
    OUTDIR = OUTDIR, 
    SAMPLE_LIST = SAMPLE_LIST, 
    REFERENCE_LIST = REFERENCE_LIST, 
    GLOBAL_GVCF_LIST = GLOBAL_GVCF_LIST, 
    GVCF_FILE_STRING = GVCF_FILE_STRING, 
    KNOWN_SITES_STRING = KNOWN_SITES_STRING
    )

