# app_logger.py
# https://habr.com/ru/post/513966/

import logging

_log_file = "x.log"
_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

def get_file_handler(
    file: str = _log_file,
    level: int = logging.WARNING,
    format: str =_log_format
) -> logging.Handler:
    
    file_handler = logging.FileHandler(file)
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(format))

    return file_handler


def get_stream_handler(
    level: int = logging.INFO,
    format: str =_log_format
) -> logging.Handler:
    
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))

    return stream_handler


def get_logger(
    name: str,
    level: int = logging.INFO
) -> logging.Logger:

    logger = logging.getLogger(name)

    logger.setLevel(level)

    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())

    return logger
