import subprocess

def variant_normalization(ANNOTATED_VCF_FILE, SAMPLE_OUTDIR, OUTDIR, FINAL_VCF_FILE):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            bcftools norm -Ov -m-any \
                --multi-overlaps . \
                {SAMPLE_OUTDIR}/{ANNOTATED_VCF_FILE} \
                -o {SAMPLE_OUTDIR}/{FINAL_VCF_FILE} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)