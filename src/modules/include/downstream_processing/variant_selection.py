import subprocess

def select_variant_by_sample(cohort_snpEff_and_snpSift_annotated_vcf_file, sample_id, reference_genome, sample_outdir, outdir, sample_vcf_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            gatk SelectVariants \
                -V {outdir}/{cohort_snpEff_and_snpSift_annotated_vcf_file} \
                -R {reference_genome} \
                --sample-name {sample_id} \
                --exclude-non-variants \
                -O {sample_outdir}/{sample_vcf_file} \
        2>> {outdir}/monitoring.log
        """
    subprocess.run(command, shell=True, check=True)