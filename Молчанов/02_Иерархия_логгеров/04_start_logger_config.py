# задвоенность обработки сообщения на разных уровнях
import logging

logging.basicConfig()

app_logger = logging.getLogger("app_logger")
console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)

f = logging.Formatter(fmt="%(levelname)s - %(name)s - %(message)s")
console_handler.setFormatter(f)

utils_logger = logging.getLogger("app_logger.utils")
utils_logger.setLevel("DEBUG")
utils_logger.addHandler(logging.StreamHandler())


def main():
    utils_logger.debug("Hello")
    # Hello # вывод сообщения на уровне utils_logger
    # DEBUG - app_logger.utils - Hello  # это на уровне app_logger
    # DEBUG:app_logger.utils:Hello      # это на уровне корневого логгера


# ====================================================================
if __name__ == "__main__":
    main()
