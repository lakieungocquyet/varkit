import subprocess

def combine_genomic_variants_gatk(gvcf_file_string, reference_genome, outdir, output_file):
    output_file_path = f"{outdir}/{output_file}"
    runtime_log_path = f"{outdir}/runtime.log"
    monitor_log_path = f"{outdir}/monitoring.log"
    with (
        open(monitor_log_path, "a") as monitoring_log,
    ):
        subprocess.run(
            [
                "/usr/bin/time",
                "-a",
                "-o", runtime_log_path,
                "-f", "Elapsed: %E\nMaximum resident set size (kB): %M\nExit status: %x\n",       
                "gatk", "CombineGVCFs",
                "-R", reference_genome,
                *gvcf_file_string,
                "-O", output_file_path
            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
        )
