from modules.header import *

def post_variant_calling_flow(workflow_config, gvcf_file_string):

    sample_inputs_dict = workflow_config["SAMPLE_INPUTS_DICT"]
    temp_outdir_path = workflow_config["TEMP_OUTDIR_PATH"]
    genome_path = workflow_config["REFERENCE_DICT"]["genome_path"]
    cohort_genomic_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_GENOMIC_SNPS_AND_INDELS_VCF_FILE"]
    cohort_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_SNPS_AND_INDELS_VCF_FILE"]
    cohort_filtered_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_FILTERED_SNPS_AND_INDELS_VCF_FILE"]
    cohort_normalized_snps_and_indels_vcf_file = workflow_config["COHORT_OUTPUTS_DICT"]["COHORT_NORMALIZED_SNPS_AND_INDELS_VCF_FILE"]
    
    combine_genomic_variants_gatk(
        gvcf_file_string = gvcf_file_string,
        reference_genome=genome_path,
        outdir = temp_outdir_path,
        output_file = cohort_genomic_snps_and_indels_vcf_file
    )
    for sample_id, info in sample_inputs_dict.items():
        temp_sample_outdir_path = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["TEMP_SAMPLE_OUTDIR_PATH"]
        sample_genomic_snps_and_indels_vcf_file = workflow_config["SAMPLE_OUTPUTS_DICT"][f"{sample_id}"]["SAMPLE_GENOMIC_SNPS_AND_INDELS_VCF_FILE"]
        os.remove(f"{temp_sample_outdir_path}/{sample_genomic_snps_and_indels_vcf_file}")
        
    genotype_variants_gatk(
        input_file = cohort_genomic_snps_and_indels_vcf_file, 
        reference_genome=genome_path,
        outdir = temp_outdir_path, 
        output_file = cohort_snps_and_indels_vcf_file
        )
    os.remove(f"{temp_outdir_path}/{cohort_genomic_snps_and_indels_vcf_file}")
    hard_filter_variants_gatk(
        input_file = cohort_snps_and_indels_vcf_file, 
        reference_genome=genome_path,
        outdir = temp_outdir_path, 
        output_file = cohort_filtered_snps_and_indels_vcf_file
    )
    os.remove(f"{temp_outdir_path}/{cohort_snps_and_indels_vcf_file}")
    normalize_variants_bcftools(
        input_file = cohort_filtered_snps_and_indels_vcf_file,
        outdir = temp_outdir_path, 
        output_file = cohort_normalized_snps_and_indels_vcf_file
        )
    os.remove(f"{temp_outdir_path}/{cohort_filtered_snps_and_indels_vcf_file}")