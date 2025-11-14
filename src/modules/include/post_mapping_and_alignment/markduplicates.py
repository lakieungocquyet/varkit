import subprocess

def markduplicates(sample_sorted_bam_file, sample_outdir, outdir, sample_marked_bam_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            gatk MarkDuplicates \
                -I {sample_outdir}/{sample_sorted_bam_file} \
                -O {sample_outdir}/{sample_marked_bam_file} \
                -M {sample_outdir}/output.metrics.txt \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)