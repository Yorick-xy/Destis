import logging


def setup_logging():
    logging.basicConfig(level=logging.INFO)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)