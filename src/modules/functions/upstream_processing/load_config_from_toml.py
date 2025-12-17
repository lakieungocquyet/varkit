import tomllib
import os

SYSTEM_CONFIG = {}
def load_config_from_toml(config_toml_path):
    if not os.path.exists(config_toml_path):
        raise FileNotFoundError(f"Config file not found: {config_toml_path}")
    with open(config_toml_path, "rb") as f:
        config = tomllib.load(f)
        # Data
        data_rootdir = config["data"]["root_directory"]
        data_rootdir = os.path.expanduser(data_rootdir)
        data_rootdir = os.path.abspath(data_rootdir)
        # Resources
        threads = config["resources"]["threads"]
        memory_gb = config["resources"]["memory_gb"]

        SYSTEM_CONFIG = {
            "DATA_ROOTDIR": data_rootdir,
            "THREADS": threads,
            "MEMORY_GB": memory_gb
        }
    return SYSTEM_CONFIG