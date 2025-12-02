import argparse
import tomllib
import os
import sys
sys.dont_write_bytecode = True
from modules.header import *
from pipelines.default_pipeline import *

SYSTEM_CONFIG = {}
def load_config_toml(config_toml_path):
    if not os.path.exists(config_toml_path):
        raise FileNotFoundError(f"Config file not found: {config_toml_path}")

    if not config_toml_path.endswith(".toml"):
        raise ValueError("Config file must be a .toml file")

    with open(config_toml_path, "rb") as f:
        config = tomllib.load(f)
        # Reference
        reference_rootdir = config["reference"]["root_directory"]
        reference_rootdir = os.path.expanduser(reference_rootdir)
        reference_rootdir = os.path.abspath(reference_rootdir)
        # Resources
        threads = config["resources"]["threads"]
        memory_gb = config["resources"]["memory_gb"]

        SYSTEM_CONFIG = {
            "REFERENCE_ROOTDIR": reference_rootdir,
            "THREADS": threads,
            "MEMORY_GB": memory_gb
        }
    return SYSTEM_CONFIG

def main():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_toml_path = os.path.join(base_dir, "varkit.config.toml")
    SYSTEM_CONFIG = load_config_toml(config_toml_path)

    parser = argparse.ArgumentParser(
        description = "Run variant calling pipeline"
    )
    parser.add_argument(
        "-I", "--input",
        required = True, 
        type = str, 
        help = "Path to workflow YAML configuration file"
    )
    args = parser.parse_args()

    input_yaml_path = args.input

    WORKFLOW_CONFIG, GVCF_FILE_STRING, KNOWN_SITES_STRING = upstream_processing_flow(input_yaml_path = input_yaml_path)

    default_pipeline(
        workflow_config = WORKFLOW_CONFIG, 
        gvcf_file_string = GVCF_FILE_STRING, 
        known_sites_string = KNOWN_SITES_STRING
        )

if __name__ == "__main__":
    main()