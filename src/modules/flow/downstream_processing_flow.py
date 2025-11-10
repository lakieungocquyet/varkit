from modules.header import *

def downstream_processing_flow(SAMPLE_LIST, GLOBAL_GVCF_LIST, REFERENCE_LIST, OUTDIR):
    for sample_id, info in SAMPLE_LIST.items():
        start_time = time.time()
        select_variant_by_sample(
            ANNOTATED_GVCF_FILE = GLOBAL_GVCF_LIST["cohort_final_gvcf_file"], 
            SAMPLE_ID = sample_id, 
            REFERENCE = REFERENCE_LIST["genome"], 
            SAMPLE_OUTDIR = info["sample_outdir"], 
            OUTDIR = OUTDIR, 
            FINAL_VCF_FILE = info["final_vcf_file"]
            )
        export_to_XLSX(
            FINAL_VCF_FILE = info["final_vcf_file"], 
            SAMPLE_OUTDIR = info["sample_outdir"], 
            XLSX_FILE = info["xlsx_file"]
            )
        
    