# Example 2
# logging_config_ex_2.py

# В рамках этого примера мы объясним, как мы можем создать регистратор, используя конфигурацию по умолчанию.
# Наш код для этого примера точно такой же, как код для предыдущего примера с небольшими изменениями.
# Мы создали экземпляр Logger , используя метод getLogger(), и мы будем использовать этот регистратор для регистрации сообщений.
# Мы изменили код внутри метода addition() и основной части, чтобы использовать метод этого экземпляра регистратора для регистрации экземпляров.

import logging
from logging import config
from typing import Any, Optional

log_config = {
    "version":1,
    "root":{
        "handlers" : ["console"],
        "level": "DEBUG"
    },
    "handlers":{
        "console":{
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        }
    },
    "formatters":{
        "std_out": {
            "format": "%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog : %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S"
        }
    },
}

config.dictConfig(log_config)

################ Logger #################
logger = logging.getLogger(__name__)

#===============================================================================

def addition(a: Any, b: Any) -> Optional[float]:

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

################################################################################

if __name__ == "__main__":
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))


    result = addition(10,20)
    logger.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logger.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))