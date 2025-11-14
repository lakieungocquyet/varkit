import subprocess
def convert_and_sort(sample_sam_file, sample_outdir, outdir, sample_sorted_bam_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log bash -c '\
            samtools view -@ 8 -Sb {sample_outdir}/{sample_sam_file} | \
            samtools sort -@ 8 -o {sample_outdir}/{sample_sorted_bam_file}' \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)