from modules.header import *

def variant_annotation_flow(workflow_config):
    temp_outdir_path = workflow_config["TEMP_OUTDIR_PATH"]
    cohort_normalized_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_NORMALIZED_SNPS_AND_INDELS_VCF_FILE"]
    cohort_genome_annotated_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_GENOME_ANNOTATED_SNPS_AND_INDELS_VCF_FILE"]
    cohort_vartype_annotated_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_VARTYPE_ANNOTATED_SNPS_AND_INDELS_VCF_FILE"]
    cohort_clinvar_annotated_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_CLINVAR_ANNOTATED_SNPS_AND_INDELS_VCF_FILE"]
    cohort_p3_1000_g_annotated_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_P3_1000G_ANNOTATED_SNPS_AND_INDELS_VCF_FILE"]
    cohort_dbsnp_annotated_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_DBSNP_ANNOTATED_SNPS_AND_INDELS_VCF_FILE"]
    cohort_dbnsfp_annotated_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_DBNSFP_ANNOTATED_SNPS_AND_INDELS_VCF_FILE"]
    log.info(f"Annotating")
    annotate_genome_snpeff(
        input_file = cohort_normalized_snps_and_indels_vcf_file, 
        outdir = temp_outdir_path, 
        output_file = cohort_genome_annotated_snps_and_indels_vcf_file
    )

    os.remove(f"{temp_outdir_path}/{cohort_normalized_snps_and_indels_vcf_file}")

    annotate_variant_type_snpsift(
        input_file = cohort_genome_annotated_snps_and_indels_vcf_file, 
        outdir = temp_outdir_path, 
        output_file = cohort_vartype_annotated_snps_and_indels_vcf_file
    )

    os.remove(f"{temp_outdir_path}/{cohort_genome_annotated_snps_and_indels_vcf_file}")

    annotate_clinvar_snpsift(
        input_file = cohort_vartype_annotated_snps_and_indels_vcf_file, 
        outdir = temp_outdir_path, 
        output_file = cohort_clinvar_annotated_snps_and_indels_vcf_file
    )

    os.remove(f"{temp_outdir_path}/{cohort_vartype_annotated_snps_and_indels_vcf_file}")

    annotate_p3_1000g_snpsift(
        input_file = cohort_clinvar_annotated_snps_and_indels_vcf_file, 
        outdir = temp_outdir_path, 
        output_file = cohort_p3_1000_g_annotated_snps_and_indels_vcf_file
    )

    os.remove(f"{temp_outdir_path}/{cohort_clinvar_annotated_snps_and_indels_vcf_file}")

    annotate_dbsnp_snpsift(
        input_file = cohort_p3_1000_g_annotated_snps_and_indels_vcf_file, 
        outdir = temp_outdir_path, 
        output_file = cohort_dbsnp_annotated_snps_and_indels_vcf_file 
    )

    os.remove(f"{temp_outdir_path}/{cohort_p3_1000_g_annotated_snps_and_indels_vcf_file}")

    annotate_dbnsfp_snpsift(
        input_file = cohort_dbsnp_annotated_snps_and_indels_vcf_file, 
        outdir = temp_outdir_path, 
        output_file = cohort_dbnsfp_annotated_snps_and_indels_vcf_file
    )
    
    os.remove(f"{temp_outdir_path}/{cohort_dbsnp_annotated_snps_and_indels_vcf_file}")