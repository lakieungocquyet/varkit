import subprocess

def sort_samtools(input_file, threads, sample_outdir, outdir, output_file):
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
                "samtools", "sort",
                "-@", threads,
                "-o", output_file_path,
                input_file_path

            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
        )
