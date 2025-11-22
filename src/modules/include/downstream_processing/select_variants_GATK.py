import subprocess

def select_variants_by_sample_GATK(input_file, sample_id, reference_genome, sample_outdir, outdir, output_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            gatk SelectVariants \
                -V {outdir}/{input_file} \
                -R {reference_genome} \
                --sample-name {sample_id} \
                --exclude-non-variants \
                -O {sample_outdir}/{output_file} \
        2>> {outdir}/monitoring.log
        """
    subprocess.run(command, shell=True, check=True)