from modules.header import *

def variant_annotation_flow(workflow_config):

    TEMP_OUTDIR = workflow_config["temp_outdir"]
    COHORT_NORMALIZED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_normalized_vcf_file"]
    COHORT_GENOME_ANNOTATED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_genome_annotated_vcf_file"]
    COHORT_VARTYPE_ANNOTATED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_vartype_annotated_vcf_file"]
    COHORT_CLINVAR_ANNOTATED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_clinvar_annotated_vcf_file"]
    COHORT_P3_1000G_ANNOTATED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_p3_1000g_annotated_vcf_file"]
    COHORT_DBSNP_ANNOTATED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_dbsnp_annotated_vcf_file"]
    COHORT_DBNSFP_ANNOTATED_VCF_FILE = workflow_config["cohort_outputs"]["cohort_dbnsfp_annotated_vcf_file"]
    annotate_genome_SnpEff(
        input_file = COHORT_NORMALIZED_VCF_FILE, 
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_GENOME_ANNOTATED_VCF_FILE
    )

    annotate_variant_type_SnpSift(
        input_file = COHORT_GENOME_ANNOTATED_VCF_FILE, 
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_VARTYPE_ANNOTATED_VCF_FILE
    )
    
    annotate_clinvar_SnpSift(
        input_file = COHORT_VARTYPE_ANNOTATED_VCF_FILE, 
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_CLINVAR_ANNOTATED_VCF_FILE
    )
    
    annotate_p3_1000g_SnpSift(
        input_file = COHORT_CLINVAR_ANNOTATED_VCF_FILE, 
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_P3_1000G_ANNOTATED_VCF_FILE
    )
    
    annotate_dbsnp_SnpSift(
        input_file = COHORT_P3_1000G_ANNOTATED_VCF_FILE, 
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_DBSNP_ANNOTATED_VCF_FILE 
    )

    annotate_dbnsfp_SnpSift(
        input_file = COHORT_DBSNP_ANNOTATED_VCF_FILE, 
        outdir = TEMP_OUTDIR, 
        output_file = COHORT_DBNSFP_ANNOTATED_VCF_FILE
    )