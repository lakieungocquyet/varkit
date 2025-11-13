import subprocess

def hard_filtration(cohort_gvcf_file, reference, outdir, cohort_filtered_gvcf_file):
    command = f"""
        /usr/bin/time -v -o {outdir}/runtime.log \
            gatk VariantFiltration \
                -R {reference} \
                -V {outdir}/{cohort_gvcf_file} \
                --filter-expression "vc.isSNP() && (QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0 || SOR > 3.0)" \
                --filter-name "MG_SNP_Filter" \
                --filter-expression "vc.isIndel() && (QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0)" \
                --filter-name "MG_INDEL_Filter" \
                -O {outdir}/{cohort_filtered_gvcf_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)

