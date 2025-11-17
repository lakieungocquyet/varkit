import subprocess

def variant_normalization(input_file, outdir, output_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            bcftools norm -Ov -m-any \
                --multi-overlaps . \
                {outdir}/{input_file} \
                -o {outdir}/{output_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)