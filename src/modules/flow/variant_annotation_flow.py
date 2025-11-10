from modules.header import *

def variant_annotation_flow(GLOBAL_GVCF_LIST, OUTDIR):
    snpEff_and_snpSift_annotation(
        NORMALIZED_GVCF_FILE = GLOBAL_GVCF_LIST["normalized_gvcf_file"], 
        OUTDIR = OUTDIR, 
        ANNOTATED_GVCF_FILE = GLOBAL_GVCF_LIST["snpEff_and_snpSift_annotated_gvcf_file"]
        )