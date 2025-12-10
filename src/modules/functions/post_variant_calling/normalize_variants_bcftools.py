import subprocess

def normalize_variants_bcftools(input_file, outdir, output_file):
    input_file_path = f"{outdir}/{input_file}"
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
                "bcftools", "norm", "-Ov", "-m-any",
                "--multi-overlaps", ".",
                input_file_path,
                "-o", output_file_path 
            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
        )

        