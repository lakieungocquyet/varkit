import yaml

def initialize_from_yaml(input_yaml_path):
    with open(f"{input_yaml_path}", "r") as f:
        input = yaml.safe_load(f)
        sample_list = input["input_paths"]["sample"]
        genome_path = input["input_paths"]["reference"]["genome"]
        known_sites_list = input["input_paths"]["reference"]["known_site"]
        outdir_path = input["input_paths"]["output"]["directory"]
    return sample_list, genome_path, known_sites_list, outdir_path