import subprocess

def mapping_and_alignment_BWA_mem(forward, reverse, sample_id, platform, reference, sample_outdir, outdir, sam_file):

    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            bwa mem -t 8 \
                -R "@RG\\tID:{sample_id}\\tLB:lib1\\tPL:{platform}\\tPU:unit1\\tSM:{sample_id}" \
                {reference} \
                {forward} \
                {reverse} \
            > {sample_outdir}/{sam_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)