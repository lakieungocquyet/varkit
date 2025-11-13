import subprocess
def convert_and_sort(sam_file, sample_outdir, outdir, sorted_bam_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log bash -c '\
            samtools view -@ 8 -Sb {sample_outdir}/{sam_file} | \
            samtools sort -@ 8 -o {sample_outdir}/{sorted_bam_file}' \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)