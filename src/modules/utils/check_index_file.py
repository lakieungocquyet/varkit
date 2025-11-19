from pathlib import Path
from modules.header import *

def check_bwa_index(reference_genome: str):
    prefix = str(reference_genome)
    bwa_extensions = ["amb", "ann", "bwt", "pac", "sa"]
    file_missing = []
    for extension in bwa_extensions:
        index_file_path = Path(prefix + "." + extension)
        if not index_file_path.exists():
            file_missing.append(index_file_path)

    if file_missing:
        ready = False
    else:
        ready = True
    return ready, file_missing

def check_minimap2_index(reference_genome):
    prefix = Path(reference_genome)
    index_file_path = prefix.with_suffix(prefix.suffix + ".mmi")
    ready = index_file_path.exists()
    return ready

def check_samtools_index(reference_genome):
    prefix = Path(reference_genome)
    index_file_path = prefix.with_suffix(prefix.suffix + ".fai")
    ready = index_file_path.exists()
    return ready

def check_gatk_index(reference_genome):
    prefix = Path(reference_genome)
    index_file_path = prefix.with_suffix(".dict")
    ready = index_file_path.exists()
    return ready

