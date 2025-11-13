import subprocess

def combine_gvcfs(gvcf_file_string, reference, outdir, combination_gvcf_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            gatk CombineGVCFs \
                -R {reference} \
                {gvcf_file_string} \
                -O {outdir}/{combination_gvcf_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)