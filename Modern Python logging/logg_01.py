import logging


logger = logging.getLogger("my_app")


def main():
    logging.basicConfig(level="DEBUG")

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

# DEBUG:my_app:debug message
# INFO:my_app:info message
# WARNING:my_app:warning message
# ERROR:my_app:error message
# CRITICAL:my_app:critical message
# ERROR:my_app:exception message
# Traceback (most recent call last):
#   File "/home/amk/__2024__/_Logging/logg_01.py", line 17, in main
#     1 / 0
#     ~~^~~
# ZeroDivisionError: division by zero