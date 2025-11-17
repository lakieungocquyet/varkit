import subprocess

def sanitization(input_file, sample_outdir, outdir, output_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            grep -vE \
                '##source=|##bcftools_normVersion=|##SnpEffVersion=|##SnpSiftVersion=|##SnpEffCmd=|##SnpSiftCmd=|##GATKCommandLine=|##bcftools_normCommand=' \
                {sample_outdir}/{input_file} \
                > {sample_outdir}/{output_file}
        2>> {outdir}/monitoring.log
        """
    subprocess.run(command, shell=True, check=True)