import logging


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(levelname)s:%(asctime)s:%(message)s:%(name)s")
    file_handler = logging.FileHandler(filename=__name__, mode='a',
                                       encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
