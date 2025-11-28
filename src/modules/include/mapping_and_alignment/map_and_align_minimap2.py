import subprocess

def map_and_align_minimap2(read_1, read_2, sample_id, platform, reference_genome, sample_outdir, outdir, output_file):
    output_file_path = f"{sample_outdir}/{output_file}"
    runtime_log_path = f"{outdir}/runtime.log"
    monitor_log_path = f"{outdir}/monitoring.log"
    with (
        open(output_file_path, "w") as outfile,
        open(runtime_log_path, "a") as runtime_log,
        open(monitor_log_path, "a") as monitoring_log,
    ):    
        subprocess.run(
            [
                "/usr/bin/time",
                "-a",
                "-o", runtime_log_path,
                "-f", "Elapsed: %E\nMaximum resident set size (kB): %M\nExit status: %x\n",
                "minimap2",
                "-ax", "sr",
                "-R", f"@RG\tID:{sample_id}\tLB:lib1\tPL:{platform}\tPU:unit1\tSM:{sample_id}",
                f"{reference_genome}.mmi",
                read_1,
                read_2,
            ],
            stdout=outfile,
            stderr=monitoring_log, 
            shell=False, 
            check=True
        )
