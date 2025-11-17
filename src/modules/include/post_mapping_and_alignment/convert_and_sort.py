import subprocess
def convert_and_sort(input_file, sample_outdir, outdir, output_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log bash -c '\
            samtools view -@ 8 -Sb {sample_outdir}/{input_file} | \
            samtools sort -@ 8 -o {sample_outdir}/{output_file}' \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)