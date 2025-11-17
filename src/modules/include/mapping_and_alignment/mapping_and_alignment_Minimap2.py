import subprocess

def mapping_and_alignment_Minimap2(forward, reverse, sample_id, platform, reference_genome, sample_outdir, outdir, output_file):
    command = f"""
        /usr/bin/time -v -o {outdir}/runtime.log \
            minimap2 -x -a \
                {reference_genome}.mmi \
                -R "@RG\\tID:{sample_id}\\tLB:lib1\\tPL:{platform}\\tPU:unit1\\tSM:{sample_id}" \
                {forward} \
                {reverse} \
                > {sample_outdir}/{output_file} \
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)