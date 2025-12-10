import subprocess

def call_genomic_snps_and_indels_gatk(input_file, threads, reference_genome, sample_outdir, outdir, output_file):
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
                "gatk", "HaplotypeCaller",
                "-I", input_file_path,
                "-R", reference_genome,
                "-O", output_file_path,
                "--native-pair-hmm-threads", threads,
                "-ERC", "GVCF",
                "-L", "/home/lknq/hg19/S07604624_Regions.bed",
                "-ip", "100",
                "--use-posteriors-to-calculate-qual", "false",
                "--dont-use-dragstr-priors", "false",
                "--use-new-qual-calculator", "true",
                "--annotate-with-num-discovered-alleles", "false",
                "--heterozygosity", "0.001",
                "--indel-heterozygosity", "1.25E-4",
                "--heterozygosity-stdev", "0.01",
                "--standard-min-confidence-threshold-for-calling", "30.0",
                "--max-alternate-alleles", "6",
                "--max-genotype-count", "1024",
                "--sample-ploidy", "2",
                "--num-reference-samples-if-no-call", "0",
                "--genotype-assignment-method", "USE_PLS_TO_ASSIGN",
                "--contamination-fraction-to-filter", "0.0",
                "--output-mode", "EMIT_VARIANTS_ONLY",
                "--minimum-mapping-quality", "20",
                "--base-quality-score-threshold", "18",
                "--pcr-indel-model", "CONSERVATIVE",
                "--likelihood-calculation-engine", "PairHMM",
                "--gvcf-gq-bands", "1", "--gvcf-gq-bands", "2", "--gvcf-gq-bands", "3", "--gvcf-gq-bands", "4",
                "--gvcf-gq-bands", "5", "--gvcf-gq-bands", "6", "--gvcf-gq-bands", "7", "--gvcf-gq-bands", "8",
                "--gvcf-gq-bands", "9", "--gvcf-gq-bands", "10", "--gvcf-gq-bands", "11", "--gvcf-gq-bands", "12",
                "--gvcf-gq-bands", "13", "--gvcf-gq-bands", "14", "--gvcf-gq-bands", "15", "--gvcf-gq-bands", "16",
                "--gvcf-gq-bands", "17", "--gvcf-gq-bands", "18", "--gvcf-gq-bands", "19", "--gvcf-gq-bands", "20",
                "--gvcf-gq-bands", "21", "--gvcf-gq-bands", "22", "--gvcf-gq-bands", "23", "--gvcf-gq-bands", "24",
                "--gvcf-gq-bands", "25", "--gvcf-gq-bands", "26", "--gvcf-gq-bands", "27", "--gvcf-gq-bands", "28",
                "--gvcf-gq-bands", "29", "--gvcf-gq-bands", "30", "--gvcf-gq-bands", "31", "--gvcf-gq-bands", "32",
                "--gvcf-gq-bands", "33", "--gvcf-gq-bands", "34", "--gvcf-gq-bands", "35", "--gvcf-gq-bands", "36",
                "--gvcf-gq-bands", "37", "--gvcf-gq-bands", "38", "--gvcf-gq-bands", "39", "--gvcf-gq-bands", "40",
                "--gvcf-gq-bands", "41", "--gvcf-gq-bands", "42", "--gvcf-gq-bands", "43", "--gvcf-gq-bands", "44",
                "--gvcf-gq-bands", "45", "--gvcf-gq-bands", "46", "--gvcf-gq-bands", "47", "--gvcf-gq-bands", "48",
                "--gvcf-gq-bands", "49", "--gvcf-gq-bands", "50", "--gvcf-gq-bands", "51", "--gvcf-gq-bands", "52",
                "--gvcf-gq-bands", "53", "--gvcf-gq-bands", "54", "--gvcf-gq-bands", "55", "--gvcf-gq-bands", "56",
                "--gvcf-gq-bands", "57", "--gvcf-gq-bands", "58", "--gvcf-gq-bands", "59", "--gvcf-gq-bands", "60",
                "--gvcf-gq-bands", "70", "--gvcf-gq-bands", "80", "--gvcf-gq-bands", "90", "--gvcf-gq-bands", "99",
                "--read-validation-stringency", "SILENT",
                "--verbosity", "INFO"
            ], 
            stdout=subprocess.DEVNULL,
            stderr=monitoring_log,
            shell=False, 
            check=True
        )
        
