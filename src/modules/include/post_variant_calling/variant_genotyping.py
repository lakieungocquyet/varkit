import subprocess

def genotype_gvcfs(COHORT_GVCF_FILE, REFERENCE, OUTDIR, COHORT_VCF_FILE):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            gatk GenotypeGVCFs \
                -R {REFERENCE} \
                -V {OUTDIR}/{COHORT_GVCF_FILE} \
                -O {OUTDIR}/{COHORT_VCF_FILE} \
                -L /home/lknq/hg19/S07604624_Regions.bed \
                -ip 100 \
                --include-non-variant-sites false \
                --merge-input-intervals false \
                --input-is-somatic false \
                --tumor-lod-to-emit 3.5 \
                --allele-fraction-error 0.001 \
                --keep-combined-raw-annotations false \
                --use-posteriors-to-calculate-qual false \
                --use-new-qual-calculator true \
                --standard-min-confidence-threshold-for-calling 30.0 \
                --max-alternate-alleles 6 \
                --sample-ploidy 2 \
                --genotype-assignment-method USE_PLS_TO_ASSIGN \
                --call-genotypes false \
                --interval-set-rule UNION \
                --interval-merging-rule ALL \
                --read-validation-stringency SILENT \
                --verbosity INFO \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)