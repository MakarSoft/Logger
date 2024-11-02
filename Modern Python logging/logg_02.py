import logging.config


logger = logging.getLogger("my_app")

# словарь, в котором явно перечислены все
# необходимые компоненты настройки логгирования
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {},
    "formatters": {},
    "handlers": {},
    "loggers": {},
}


def main():
    logging.config.dictConfig(config=logging_config)
    logger.addHandler(logging.StreamHandler(...))

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    try:
        1 / 0
    except ZeroDivisionError:
        # print("exception message")
        logger.exception("exception message")


if __name__ == "__main__":
    main()
