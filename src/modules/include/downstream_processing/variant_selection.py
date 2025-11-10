import subprocess

def select_variant_by_sample(ANNOTATED_GVCF_FILE, SAMPLE_ID, REFERENCE, SAMPLE_OUTDIR, OUTDIR, FINAL_VCF_FILE):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            gatk SelectVariants \
                -V {OUTDIR}/temp_8.{ANNOTATED_GVCF_FILE} \
                -R {REFERENCE} \
                --sample-name {SAMPLE_ID} \
                --exclude-non-variants \
                -O {SAMPLE_OUTDIR}/{FINAL_VCF_FILE} \
        2>> {OUTDIR}/monitoring.log
        """
    subprocess.run(command, shell=True, check=True)