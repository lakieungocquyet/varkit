import subprocess

def hard_filtration(cohort_vcf_file, reference_genome, outdir, cohort_filtered_vcf_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            gatk VariantFiltration \
                -R {reference_genome} \
                -V {outdir}/{cohort_vcf_file} \
                --filter-expression "vc.isSNP() && (QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0 || SOR > 3.0)" \
                --filter-name "MG_SNP_Filter" \
                --filter-expression "vc.isIndel() && (QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0)" \
                --filter-name "MG_INDEL_Filter" \
                -O {outdir}/{cohort_filtered_vcf_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)

