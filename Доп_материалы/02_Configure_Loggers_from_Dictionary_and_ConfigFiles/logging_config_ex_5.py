# Dictionary Config for Hierarchy Of Loggers

# Example 5
# logging_config_ex_5.py

# В рамках этого примера мы объясняем, как мы можем создать иерархию регистраторов.
# У нас есть словарь конфигурации для этого примера, который точно такой же, как в нашем предыдущем примере, только с изменением формата сообщения.
#
# Мы переместили код метода добавления в метод add() класса Addition.
# Наша основная часть кода создает экземпляр Addition и выполняет сложение, используя его метод add().
#
# Мы создали регистратор с именем arithmetic_ops, который будет использоваться для регистрации сообщений внутри основной части нашего кода.
# Затем мы создали еще один регистратор с именем arithmetic_ops.Addition, который будет использоваться для регистрации сообщений внутри метода add().
# Регистратор, созданный внутри класса Addition, будет вспомогательным регистратором нашего основного регистратора (arithmetic_ops).
#
# Когда мы запускаем приведенный ниже код, мы можем заметить из вывода, что сообщения журнала, зарегистрированные основным регистратором, имеют имя arithmetic_ops,
# а сообщения журнала, зарегистрированные вспомогательным регистратором, имеют имя arithmetic_ops.Addition .

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
        },
    },
    "formatters":{
        "std_out": {
            "format": "%(levelname)s : %(name)s : %(funcName)s : %(message)s",
        }
    },
}

################################################################################

config.dictConfig(log_config)

################ Module Logger #################
logger = logging.getLogger("arithmetic_ops")

#===============================================================================

class Addition:

    def __init__(self) -> None:
        ################ Class Logger #################
        self.logger = logging.getLogger("arithmetic_ops.Addition")


    def add(self, a: Any, b: Any) -> Optional[float]:

        self.logger.debug("Inside Addition Function")
        if isinstance(a, str) and a.isdigit():
            self.logger.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

        if isinstance(b, str) and b.isdigit():
            self.logger.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

        try:
            result = float(a) + float(b)
            self.logger.info("Addition Function Completed Successfully")
            return result
        except Exception as e:
            self.logger.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
            return None

################################################################################

if __name__ == "__main__":
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))

    addition = Addition()
    result = addition.add(10,20)
    logger.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition.add("20",20)
    logger.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition.add("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))
