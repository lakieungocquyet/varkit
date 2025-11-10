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

default_pipeline(INPUT_YAML = INPUT_YAML)

