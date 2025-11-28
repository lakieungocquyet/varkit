import subprocess

def markduplicates_gatk(input_file, sample_outdir, outdir, output_file):
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
                "gatk", "MarkDuplicates",
                "-I", input_file_path,
                "-O", output_file_path,
                "-M", f"{sample_outdir}/output.metrics.txt"
            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
        )
