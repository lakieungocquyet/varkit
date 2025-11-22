import logging
import sys

def setup_logging(outdir):
    log = logging.getLogger("pipeline")
    log.setLevel(logging.INFO)
    
    if log.hasHandlers():
        log.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )
    file_handler = logging.FileHandler(f"{outdir}/runtime.log", mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    log.addHandler(file_handler)
    log.addHandler(stream_handler)
    return log


