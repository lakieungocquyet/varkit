import subprocess

def sanitize(input_file, outdir, output_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            grep -vE \
                '##source=|##bcftools_normVersion=|##SnpEffVersion=|##SnpSiftVersion=|##SnpEffCmd=|##SnpSiftCmd=|##GATKCommandLine=|##bcftools_normCommand=' \
                {outdir}/{input_file} \
                > {outdir}/{output_file}
        2>> {outdir}/monitoring.log
        """
    subprocess.run(command, shell=True, check=True)