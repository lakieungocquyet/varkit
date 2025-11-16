import argparse
import sys
sys.dont_write_bytecode = True
from modules.header import *
from pipelines.default_pipeline import *

parser = argparse.ArgumentParser(description="None")
parser.add_argument("-I", "--input",required=True, type=str, help="None")
args = parser.parse_args()
INPUT_YAML = args.input

WORKFLOW_CONFIG, GVCF_FILE_STRING, KNOWN_SITES_STRING = upstream_processing_flow(input_yaml = INPUT_YAML)

setup_logging(
    outdir = WORKFLOW_CONFIG["outdir"]
    )

default_pipeline(
    workflow_config = WORKFLOW_CONFIG, 
    gvcf_file_string = GVCF_FILE_STRING, 
    known_sites_string = KNOWN_SITES_STRING
    )

