# Example 7
# logging_config_ex_7.py

# В рамках этого примера мы демонстрируем, как мы можем использовать более одного фильтра с конфигурацией словаря.
# Мы определили три класса для реализации фильтров.
# DebugAndInfoOnly — этот класс фильтрует все сообщения журнала, кроме сообщений уровня DEBUG и INFO .
# WarningsOnly     — этот класс фильтрует все сообщения журнала, кроме сообщений уровня WARNING .
# ErrorsOnly       — этот класс фильтрует все сообщения журнала, кроме сообщений уровня ERROR .
# Наша конфигурация словаря начинается с определения root регистратора с тремя обработчиками (console, warnings_handler и errors_handler).
# Обработчик console  направляет сообщения журнала на стандартный вывод и использует фильтр с именем debug_&_info.
# Обработчик warnings_handler направляет log-сообщения в файл с именем 'warnings_only.log' и использует фильтр warnings_only.
# Обработчик warnings_handler направляет log-сообщения в файл с именем 'errors_only.log' и использует фильтр errors_only.
# std_out - formatter,  будет использоваться всеми обработчиками.
# Затем мы определили все три фильтра внутри раздела фильтров.
# Остальная часть нашего кода точно такая же, как и в предыдущем примере.
# Когда мы запускаем приведенный ниже код, мы можем заметить, что только сообщения INFO и DEBUG направляются на стандартный вывод.
# Мы также отобразили содержимое файла warnings_only.log , в котором хранятся все предупреждающие сообщения, и содержимое файла errors) only.log,
# в котором хранятся все сообщения об ошибках.

import logging
from logging import config

class DebugAndInfoOnly(logging.Filter): ### Filters all messages except Info and Debug
    def filter(self, record):
        if record.levelno < 21:
            return True
        else:
            return False

class WarningsOnly(logging.Filter): ### Filters all messages except Warning
    def filter(self, record):
        if record.levelno > 20 and record.levelno < 40:
            return True
        else:
            return False

class ErrorsOnly(logging.Filter): ### Filters all messages except Error
    def filter(self, record):
        if record.levelno > 30 and record.levelno < 50:
            return True
        else:
            return False

log_config = {
    "version":1,
    "root":{
        "handlers" : ["console", "warnings_handler", "errors_handler"],
        "level": "DEBUG"
    },
    "handlers":{
        "console":{
            "formatter": "std_out",
            "filters": ["debug_&_info"],
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        },
        "warnings_handler":{
            "formatter":"std_out",
            "class":"logging.FileHandler",
            "filters": ["warnings"],
            "level":"DEBUG",
            "filename":"warnings_only.log"
        },
        "errors_handler":{
            "formatter":"std_out",
            "class":"logging.FileHandler",
            "filters": ["errors"],
            "level":"DEBUG",
            "filename":"errors_only.log"
        },
    },
    "formatters":{
        "std_out": {
            "format": "%(levelname)s : %(name)s : %(funcName)s : %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S"
        }

    },
    "filters":{
        "debug_&_info":{
            "()": DebugAndInfoOnly
        },
        "warnings":{
            "()": WarningsOnly
        },
        "errors":{
            "()": ErrorsOnly
        }
    }
}

config.dictConfig(log_config)

################ Logger #################
logger = logging.getLogger("root")

def addition(a, b):
    logger.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logger.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logger.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    try:
        result = float(a) + float(b)
        logger.info("Addition Function Completed Successfully")
        return result
    except Exception as e:
        logger.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
        return None


if __name__ == "__main__":
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))


    result = addition(10,20)
    logger.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logger.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))