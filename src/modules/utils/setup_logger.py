import logging
import sys

def setup_logger(outdir: str):
    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.INFO)

    # Xóa handler cũ 
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(f"{outdir}/runtime.log", mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

def logging_info(msg):
    logger = logging.getLogger("pipeline")
    logger.info(msg)