import subprocess

def hard_filter_variants_gatk(input_file, reference_genome, outdir, output_file):
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
                "gatk", "VariantFiltration",
                "-R", reference_genome,
                "-V", input_file_path,
                "--filter-expression", "vc.isSNP() && (QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0 || SOR > 3.0)",
                "--filter-name", "MG_SNP_Filter",
                "--filter-expression", "vc.isIndel() && (QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0)",
                "--filter-name", "MG_INDEL_Filter",
                "-O", output_file_path
            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
        )
        
        

