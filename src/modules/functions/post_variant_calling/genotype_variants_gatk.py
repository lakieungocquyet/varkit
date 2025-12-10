import subprocess

def genotype_variants_gatk(input_file, reference_genome, outdir, output_file):
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
                "gatk", "GenotypeGVCFs",
                "-R", reference_genome,
                "-V", input_file_path,
                "-O", output_file_path,
                "-L", "/home/lknq/hg19/S07604624_Regions.bed",
                "-ip", "100",
                "--include-non-variant-sites", "false",
                "--merge-input-intervals", "false",
                "--input-is-somatic", "false",
                "--tumor-lod-to-emit", "3.5",
                "--allele-fraction-error", "0.001",
                "--keep-combined-raw-annotations", "false",
                "--use-posteriors-to-calculate-qual", "false",
                "--use-new-qual-calculator", "true",
                "--standard-min-confidence-threshold-for-calling", "30.0",
                "--max-alternate-alleles", "6",
                "--sample-ploidy", "2",
                "--genotype-assignment-method", "USE_PLS_TO_ASSIGN",
                "--call-genotypes", "false",
                "--interval-set-rule", "UNION",
                "--interval-merging-rule", "ALL",
                "--read-validation-stringency", "SILENT",
                "--verbosity", "INFO"
            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
        )