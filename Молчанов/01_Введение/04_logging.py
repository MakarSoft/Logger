import logging

# Можно использовать и другой обработчик, если например в параметрах
# basicConfig указать имя файла логов
logging.basicConfig(level="DEBUG", filename="mylog.log")

logger = logging.getLogger()

print(logger)
# <RootLogger root (DEBUG)>
print(logger.level)
# 10
print(logger.handlers)
# [<FileHandler /home/amk/_PY/#_PY_#/_Logger/_Logging_Molchanov/mylog.log (NOTSET)>]


def main(name):
    logger.debug(f"Enter in the main() function : name = {name}")


if __name__ == "__main__":
    main("Hello")
