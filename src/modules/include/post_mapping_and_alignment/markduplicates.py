import subprocess

def markduplicates(input_file, sample_outdir, outdir, output_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            gatk MarkDuplicates \
                -I {sample_outdir}/{input_file} \
                -O {sample_outdir}/{output_file} \
                -M {sample_outdir}/output.metrics.txt \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)