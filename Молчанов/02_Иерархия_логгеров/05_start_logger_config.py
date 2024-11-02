# Избегаем задвоенности - свойство propagate

import logging

logging.basicConfig()

app_logger = logging.getLogger("app_logger")
console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)
app_logger.propagate = False  # !!!

f = logging.Formatter(fmt="%(levelname)s - %(name)s - %(message)s")
console_handler.setFormatter(f)

utils_logger = logging.getLogger("app_logger.utils")
utils_logger.setLevel("DEBUG")


def main():
    utils_logger.debug("Hello")
    # DEBUG - app_logger.utils - Hello  # это на уровне app_logger
    # задвоенность ушла, т.к. прервали поток распростонения LogRecord
    # вверх по цепочке наследования логгеров


# ====================================================================
if __name__ == "__main__":
    main()
