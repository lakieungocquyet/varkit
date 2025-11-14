import subprocess

def mapping_and_alignment_BWA_mem(forward, reverse, sample_id, platform, reference_genome, sample_outdir, outdir, sample_sam_file):

    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            bwa mem -t 8 \
                -R "@RG\\tID:{sample_id}\\tLB:lib1\\tPL:{platform}\\tPU:unit1\\tSM:{sample_id}" \
                {reference_genome} \
                {forward} \
                {reverse} \
            > {sample_outdir}/{sample_sam_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)