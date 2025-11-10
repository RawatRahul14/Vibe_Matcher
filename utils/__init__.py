import logging
from datetime import datetime
import os

## === Create logs directory ===
os.makedirs(
    "logs",
    exist_ok = True
)

## === Function: setup_logger ===
def setup_logger(
        name: str,
        log_file: str,
        level = logging.INFO
):
    """
    Creates and configures an independent logger.

    Args:
        name (str): Unique name for the logger (e.g., "data_logger").
        log_file (str): Path to the file where logs will be saved.
        level (int): Logging level (default = INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """

    ## === File handler ===
    handler = logging.FileHandler(log_file)

    ## === Log message format ===
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)

    ## === Logger setup ===
    logger = logging.getLogger(name)
    logger.setLevel(level)

    ## === Attach the handler to the logger (writes logs to file) ===
    logger.addHandler(handler)

    return logger


## === Create Separate Loggers for Each Pipeline ===
data_logger = setup_logger("data_logger", "logs/data_pipeline.log")

embed_logger = setup_logger("embed_logger", "logs/embedding_pipeline.log")

match_logger = setup_logger("match_logger", "logs/matching_pipeline.log")