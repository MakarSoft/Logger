# 9.2
# logging_advanced_guide_03_2.py 
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# добавление одной строки внутри класса Addition.
# Мы установили для атрибута propagate (распространение) вспомогательного регистратора внутри класса Addition значение False.
# Это предотвратит распространение сообщений вспомогательным регистратором в родительский регистратор.
#
# Когда мы запускаем приведенный ниже скрипт, мы можем заметить, что повторяющиеся сообщения журнала теперь исчезли.

import logging
from typing import Any, Optional

################ Module Logger ############
logger = logging.getLogger("arithmetic_ops")
logger.setLevel(logging.INFO)

############## Handler ####################
std_out = logging.StreamHandler()
std_out.setLevel(logging.INFO)

############## Formatter ##################
formatter = logging.Formatter(
    fmt="%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S"
)

std_out.setFormatter(formatter) ### Register Formatter with Handler.
logger.addHandler(std_out)      ### Register Handler with Logger.    

#===============================================================================

class Addition:
    def __init__(self):

        ################ Class Logger #################
        self.logger = logging.getLogger("arithmetic_ops.Addition")
        self.logger.propagate=False # propagate (распространение) вспомогательного регистратора <- False
        self.logger.setLevel(logging.DEBUG)

        ############## Handler #######################
        std_out = logging.StreamHandler()
        std_out.setLevel(logging.DEBUG)

        ############## Formatter #####################
        formatter = logging.Formatter(
            fmt="%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s",
            datefmt="%d-%m-%Y %I:%M:%S"
        )

        std_out.setFormatter(formatter) ### Register Formatter with Handler.
        self.logger.addHandler(std_out) ### Register Handler with Logger.

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

# 10-08-2022 02:43:05 : INFO : arithmetic_ops : <module> : Current Log Level : 20
#
# 10-08-2022 02:43:05 : DEBUG : arithmetic_ops.Addition : add : Inside Addition Function
# 10-08-2022 02:43:05 : INFO : arithmetic_ops.Addition : add : Addition Function Completed Successfully
# 10-08-2022 02:43:05 : INFO : arithmetic_ops : <module> : Addition of 10 & 20 is : 30.0
#
# 10-08-2022 02:43:05 : DEBUG : arithmetic_ops.Addition : add : Inside Addition Function
# 10-08-2022 02:43:05 : WARNING : arithmetic_ops.Addition : add : Warning : Parameter A is passed as String. Future versions won't support it.
# 10-08-2022 02:43:05 : INFO : arithmetic_ops.Addition : add : Addition Function Completed Successfully
# 10-08-2022 02:43:05 : INFO : arithmetic_ops : <module> : Addition of '20' & 20 is : 40.0
#
# 10-08-2022 02:43:05 : DEBUG : arithmetic_ops.Addition : add : Inside Addition Function
# 10-08-2022 02:43:05 : ERROR : arithmetic_ops.Addition : add : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# 10-08-2022 02:43:05 : INFO : arithmetic_ops : <module> : Addition of A & 20 is : None
