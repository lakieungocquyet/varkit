import subprocess

def baserecalibrator(marked_bam_file, known_sites_string, reference, sample_outdir, outdir):
    command = f"""
    /usr/bin/time -v -a -o {outdir}/runtime.log \
        gatk BaseRecalibrator \
            -I {sample_outdir}/{marked_bam_file} \
            -R {reference} \
            {known_sites_string} \
            -O {sample_outdir}/recal_data.table \
    2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)

def applyBQSR (marked_bam_file, reference, sample_outdir, outdir, recal_bam_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            gatk ApplyBQSR \
                -I {sample_outdir}/{marked_bam_file} \
                -R {reference} \
                --bqsr-recal-file {sample_outdir}/recal_data.table \
                -O {sample_outdir}/{recal_bam_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)