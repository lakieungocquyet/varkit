import subprocess

def genotype_variants_GATK(input_file, reference_genome, outdir, output_file):
    command = f"""
        /usr/bin/time -v -a -o {outdir}/runtime.log \
            gatk GenotypeGVCFs \
                -R {reference_genome} \
                -V {outdir}/{input_file} \
                -O {outdir}/{output_file} \
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
        2>> {outdir}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)