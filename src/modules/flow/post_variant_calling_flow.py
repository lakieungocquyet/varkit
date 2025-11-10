from modules.header import *

def post_variant_calling_flow(SAMPLE_LIST, REFERENCE_LIST, OUTDIR, GLOBAL_GVCF_LIST):
    GVCF_FILE_LIST = ""
    for sample_id, info in SAMPLE_LIST.items():
        GVCF_FILE_LIST += f" -V {info['sample_outdir']}/{info['raw_gvcf_file']}"    

    combine_gvcfs(
        GVCF_FILE_LIST = GVCF_FILE_LIST,
        REFERENCE = REFERENCE_LIST["genome"],
        OUTDIR = OUTDIR,
        COMBINED_GVCF_FILE = GLOBAL_GVCF_LIST["combined_gvcf_file"]
    )
    
    hard_filtration(
        COMBINED_GVCF_FILE = GLOBAL_GVCF_LIST["combined_gvcf_file"], 
        REFERENCE = REFERENCE_LIST["genome"],
        OUTDIR = OUTDIR, 
        FILTERED_GVCF_FILE = GLOBAL_GVCF_LIST["filtered_gvcf_file"]
    )
