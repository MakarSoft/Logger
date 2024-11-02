
# Dictionary Config to Create Multiple Loggers
# Example 3
# logging_config_ex_3.py

# В рамках нашего третьего примера мы демонстрируем, как мы можем настроить несколько регистраторов с разными конфигурациями, используя конфигурацию словаря.

# Наш словарь для этой части создает корневые регистраторы, как в предыдущем примере.
# Мы представили новый раздел с именованными регистраторами, в котором мы определили новый регистратор с именем main.
# Мы использовали обработчик, отличный от используемого корневым регистратором в качестве обработчика main регистратора.
# Мы также установили уровень main регистратора на INFO и установили propagate атрибут в False.
#
# Затем мы создали два обработчика с именами console1 и console2.
# Оба имеют одинаковую конфигурацию, но
#   console1 будет использоваться root регистратором и
#   console2 будет использоваться main регистратором.
# Затем мы создали два разных средства форматирования с именами std_out1 и std_out2 с различным строковым форматированием сообщений журнала.
# Форматтер std_out1 будет использоваться root регистратором, а форматтер std_out2 будет использоваться main регистратором.
#
# Затем мы настроили модуль ведения журнала, используя этот словарь ( config.dictConfig(log_config) ).
#
# Затем мы создали два регистратора ( logger1 и logger2 ).
# logger1 будет иметь конфигурацию root регистратора, а logger2 будет иметь конфигурацию main регистратора.
#
# Мы изменили код внутри ф-ции addition , чтобы использовать logger1 для регистрации сообщений.
# Наша основная часть кода использует logger2 для регистрации сообщений.
# Когда мы запускаем приведенный ниже скрипт, мы можем заметить из вывода на основе различных форматов сообщений журнала,
# что log-сообщения, зарегистрированные ф-цией addition, имеют тот же формат, что и для root регистратора,
# а log-сообщения, зарегистрированные основной частью кода, имеют тот же формат, что и для main регистратора.

import logging
from logging import config
from typing import Any, Optional

log_config = {
    "version":1,
    "root":{
        "handlers" : ["console1"],
        "level": "DEBUG"
    },
    "loggers":{
        "main":{
            "handlers" : ["console2"],
            "level": "INFO",
            "propagate":False
        }
    },
    "handlers":{
        "console1":{
            "formatter": "std_out1",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        },
        "console2":{
            "formatter": "std_out2",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        }
    },
    "formatters":{
        "std_out1": {
            "format": "%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog : %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S"
        },
        "std_out2": {
            "format": "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S"
        }
    },
}

config.dictConfig(log_config)

################ Logger #################
logger1 = logging.getLogger("root")
logger2 = logging.getLogger("main")

#===============================================================================

def addition(a: Any, b: Any) -> Optional[float]:

    logger1.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logger1.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logger1.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    try:
        result = float(a) + float(b)
        logger1.info("Addition Function Completed Successfully")
        return result
    except Exception as e:
        logger1.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
        return None

################################################################################

if __name__ == "__main__":
    logger2.info("Current Log Level : {}\n".format(logger2.getEffectiveLevel()))


    result = addition(10,20)
    logger2.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logger2.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition("A",20)
    logger2.info("Addition of {} & {} is : {}".format("A",20, result))