import subprocess

def select_variants_by_sample_gatk(input_file, sample_id, reference_genome, sample_outdir, outdir, output_file):

    input_file_path = f"{outdir}/{input_file}"
    output_file_path = f"{sample_outdir}/{output_file}"
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
                "gatk", "SelectVariants",
                "-V", input_file_path,
                "-R", reference_genome,
                "--sample-name", sample_id,
                "--exclude-non-variants",
                "-O", output_file_path,                 
            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
        )

        