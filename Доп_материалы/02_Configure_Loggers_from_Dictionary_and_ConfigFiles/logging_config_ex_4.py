# Dictionary Config to Direct Logs to File and Console

# Example 4
# logging_config_ex_4.py

# В рамках нашего четвертого примера мы демонстрируем, как мы можем направлять сообщения журнала на консоль и в файл, используя конфигурацию словаря.

# Наш словарь конфигурации для этой части создает корневой регистратор с двумя обработчиками (консольным и файловым).
# В разделе обработчиков определены два обработчика.
# Обработчик консоли такой же, как в наших предыдущих примерах.
# Обработчик файла определяется с помощью класса logging.FileHandler.
# Для него установлен уровень ведения журнала INFO, а имя файла журнала — all_message.log, в который будут направляться сообщения журнала.
# Мы изменили формат нашего средства форматирования std_out, чтобы включить несколько деталей, в отличие от наших предыдущих примеров.
# Этот форматер будет использоваться обоими нашими обработчиками для регистрации сообщений.

# Наш код для этого примера точно такой же, как наш код для второго примера. Он создал единый регистратор и использовал его для регистрации всех сообщений.

# Когда мы запускаем приведенный ниже скрипт, мы можем заметить из вывода, что все сообщения журнала с уровнем DEBUG и выше направляются на стандартный вывод.
# Мы также отобразили содержимое файла all_messages.log, куда направляются все сообщения журнала с уровнем INFO и выше.

import logging
from logging import config
from typing import Any, Optional

log_config = {
    "version":1,
    "root":{
        "handlers" : ["console", "file"],
        "level": "DEBUG"
    },
    "handlers":{
        "console":{
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        },
        "file":{
            "formatter":"std_out",
            "class":"logging.FileHandler",
            "level":"INFO",
            "filename":"all_messages.log"
        }
    },
    "formatters":{
        "std_out": {
            "format": "%(levelname)s : %(module)s : %(funcName)s : %(message)s",
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