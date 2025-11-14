import subprocess

def variant_normalization(cohort_filtered_vcf_file, outdir, cohort_normalized_vcf_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            bcftools norm -Ov -m-any \
                --multi-overlaps . \
                {outdir}/{cohort_filtered_vcf_file} \
                -o {outdir}/{cohort_normalized_vcf_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)