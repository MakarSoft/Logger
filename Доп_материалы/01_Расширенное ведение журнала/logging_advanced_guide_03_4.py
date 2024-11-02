# 9.4
# logging_advanced_guide_03_4.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python


# Код для этого примера точно такой же, как наш код для предыдущих примеров с несколькими удаленными строками из определения класса Addition.
# На этот раз мы только определили вспомогательный регистратор внутри класса Addition.
# Мы удалили из него всю информацию об обработчике и форматере.
# Это заставит вспомогательный регистратор направлять все сообщения в родительский регистратор, у которого есть обработчик и средство форматирования
# для обработки сообщений журнала. Так обычно логирование реализуется в больших проектах.
# Мы определяем обработчики, средства форматирования и фильтры только в корневом регистраторе один раз в модуле.
# Все вспомогательные регистраторы будут передавать сообщения своим родительским регистраторам вплоть до этого корневого регистратора,
# который затем будет их обрабатывать.

# Когда мы запускаем приведенный ниже скрипт, мы можем заметить, что вывод точно такой же, как в нашем предыдущем примере.

import logging
from typing import Any, Optional

################ Module Logger #################
logger = logging.getLogger("arithmetic_ops")
logger.setLevel(logging.INFO)

############## Handler #########################
std_out = logging.StreamHandler()
std_out.setLevel(logging.INFO)

############## Formatter #######################
formatter = logging.Formatter(
    fmt="%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S"
)

std_out.setFormatter(formatter) ### Register Formatter with Handler.
logger.addHandler(std_out)      ### Register Handler with Logger.    

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

    result = addition.add(20, "20")
    print("{} + {} = {}\n".format(20, "'20'", result))

    result = addition.add("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))

