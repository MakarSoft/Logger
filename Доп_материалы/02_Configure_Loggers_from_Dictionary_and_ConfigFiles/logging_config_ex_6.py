# Example 6
# logging_config_ex_6.py

# В рамках этого примера мы демонстрируем, как мы можем включить фильтры в конфигурацию словаря.
# Мы создали класс с именем InfoAnWarningsOnly, расширив класс logging.Filter, который реализует метод filter().
# Метод filter() принимает в качестве входных данных экземпляр LogRecord. Метод проверяет, находится ли уровень журнала в диапазоне 10-30,
# затем возвращает True, иначе возвращает False. Он также изменяет сообщение журнала с уровнем 30 (WARNING), чтобы включить строку 'Error:' чтобы указать,
# что это ошибки в будущем.
# Наш словарь журналирования создает корневой регистратор с обработчиком консоли, фильтром info_&_warnings и уровнем журнала DEBUG.
# Определение обработчика консоли и средств форматирования такое же, как в наших предыдущих примерах. Мы также включили фильтр info_&_warnings в обработчик консоли.
# На этот раз мы включили в словарь конфигурации новый раздел под названием filters. Мы установили параметр () в класс фильтра InfoAnWarningsOnly,
# который мы определили ранее.
# За исключением конфигурации словаря, остальная часть нашего кода такая же, как и код из примеров 2 и 4.
# Когда мы запускаем приведенный ниже скрипт, мы можем заметить из вывода, что все сообщения, кроме INFO и WARNING , отфильтрованы.
# Кроме того, сообщения WARNING  изменены, чтобы включать строку 'Error:'.

import logging
from logging import config

class InfoAnWarningsOnly(logging.Filter):
    def filter(self, record):
        if record.levelno >10 and record.levelno < 31:
            if record.levelno == 30: ## Updating Warning messages to Error.
                record.levelno = 40
                record.msg = "Error : " + record.msg
            return True
        else:
            return False

log_config = {
    "version":1,
    "root":{
        "handlers" : ["console"],
        "filters": ["info_&_warnings"],
        "level": "DEBUG"
    },
    "handlers":{
        "console":{
            "formatter": "std_out",
            "filters": ["info_&_warnings"],
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        }
    },
    "formatters":{
        "std_out": {
            "format": "%(levelname)s : %(name)s : %(funcName)s : %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S"
        }
    },
    "filters":{
        "info_&_warnings":{
            "()": InfoAnWarningsOnly
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