import subprocess

def sanitization_vcf_file(vcf_file, sample_outdir, outdir, final_vcf_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            grep -vE \
                '##source=|##bcftools_normVersion=|##SnpEffVersion=|##SnpSiftVersion=|##SnpEffCmd=|##SnpSiftCmd=|##GATKCommandLine=|##bcftools_normCommand=' \
                {sample_outdir}/{vcf_file} \
                > {sample_outdir}/{final_vcf_file}
        2>> {outdir}/monitoring.log
        """
    subprocess.run(command, shell=True, check=True)