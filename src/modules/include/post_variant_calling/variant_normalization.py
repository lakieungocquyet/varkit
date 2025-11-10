import subprocess

def variant_normalization(FILTERED_GVCF_FILE, OUTDIR, NORMALIZED_GVCF_FILE):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            bcftools norm -Ov -m-any \
                --multi-overlaps . \
                {OUTDIR}/{FILTERED_GVCF_FILE} \
                -o {OUTDIR}/{NORMALIZED_GVCF_FILE} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)