import subprocess

def baserecalibrator(sample_marked_bam_file, known_sites_string, reference_genome, sample_outdir, outdir):
    command = f"""
    /usr/bin/time -v -a -o {outdir}/runtime.log \
        gatk BaseRecalibrator \
            -I {sample_outdir}/{sample_marked_bam_file} \
            -R {reference_genome} \
            {known_sites_string} \
            -O {sample_outdir}/recal_data.table \
    2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)

def applyBQSR (sample_marked_bam_file, reference_genome, sample_outdir, outdir, sample_recal_bam_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            gatk ApplyBQSR \
                -I {sample_outdir}/{sample_marked_bam_file} \
                -R {reference_genome} \
                --bqsr-recal-file {sample_outdir}/recal_data.table \
                -O {sample_outdir}/{sample_recal_bam_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)