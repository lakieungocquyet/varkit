#! /bin/bash

gatk LiftoverVcf \
  -I /home/lknq/anotation/1000G.phase3.integrated.sites_only.no_MATCHED_REV.hg38.vcf \
  -O /home/lknq/anotation/1000G.phase3.integrated.sites_only.no_MATCHED_REV.hg19.vcf \
  -CHAIN /home/lknq/hg38ToHg19.over.chain \
  -REJECT /home/lknq/anotation/rejected_variants.vcf \
  -R /home/lknq/hg19/hg19.p13.plusMT.no_alt_analysis_set.fa

# EVS

