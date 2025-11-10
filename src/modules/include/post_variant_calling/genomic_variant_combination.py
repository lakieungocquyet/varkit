import subprocess

def combine_gvcfs(GVCF_FILE_STRING, REFERENCE, OUTDIR, COHORT_GVCF_FILE):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            gatk CombineGVCFs \
                -R {REFERENCE} \
                {GVCF_FILE_STRING} \
                -O {OUTDIR}/{COHORT_GVCF_FILE} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)