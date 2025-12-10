import subprocess

def recalibrate_bases_gatk(input_file, known_sites_string, reference_genome, sample_outdir, outdir):
    input_file_path = f"{sample_outdir}/{input_file}"
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
                "gatk", "BaseRecalibrator",
                "-I", input_file_path,
                "-R", reference_genome,
                *known_sites_string,
                "-O", f"{sample_outdir}/recal_data.table"
            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
            )
        
def apply_bqsr_gatk(input_file, reference_genome, sample_outdir, outdir, output_file):
    input_file_path = f"{sample_outdir}/{input_file}"
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
                "gatk", "ApplyBQSR",
                "-I", input_file_path,
                "-R", reference_genome,
                "--bqsr-recal-file", f"{sample_outdir}/recal_data.table",
                "-O", output_file_path
            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
        )

        