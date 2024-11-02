# Example 8
# logging_advanced_guide_02.py

# добавляем форматирование log-сообщений с помощью экземпляра Formatter()
# Foramtter(fmt=None,datefmt=None) — этот конструктор принимает строку форматирования сообщения и строку форматирования даты в качестве входных данных
# и создает экземпляр Formatter , который затем можно добавить в обработчик для форматирования log-сообщений, отформатированных этим обработчиком.
# Важные методы StreamHandler 
#   setFormatter(formatter) — этот метод принимает экземпляр Formatter в качестве входных данных и устанавливает его в качестве средства форматирования для этого обработчика.

import logging
from typing import Any, Optional

################ Logger #####################
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

############## Handler ######################
std_out = logging.StreamHandler()
std_out.setLevel(logging.DEBUG)

############## Formatter ####################
formatter = logging.Formatter(
    fmt="%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S"
)

std_out.setFormatter(formatter) ### Register Formatter with Handler.
logger.addHandler(std_out)      ### Register Handler with Logger.

#===============================================================================
def addition(a: Any, b: Any) -> Optional[float]:

    logger.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logger.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logger.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    result = None
    try:
        result = float(a) + float(b)
        logger.info("Addition Function Completed Successfully")
    except Exception as e:
        logger.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
    finally:
        return result

################################################################################

if __name__ == "__main__":
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))

    result = addition(10,20)
    logger.info("{} + {} = {}\n".format(10,20, result))

    result = addition("20", 20)
    print("{} + {} = {}\n".format("'20'", 20, result))

    result = addition(20, "20")
    print("{} + {} = {}\n".format(20, "'20'", result))

    result = addition("A",20)
    logger.info("{} + {} = {}".format("A",20, result))

# 10-08-2022 01:52:40 : INFO : logging_advanced_guide_02 : <module> : 41 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : Current Log Level : 10
#
# 10-08-2022 01:52:40 : DEBUG : logging_advanced_guide_02 : addition : 23 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : Inside Addition Function
# 10-08-2022 01:52:40 : INFO : logging_advanced_guide_02 : addition : 33 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : Addition Function Completed Successfully
# 10-08-2022 01:52:40 : INFO : logging_advanced_guide_02 : <module> : 44 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : 10 + 20 = 30.0
#
# 10-08-2022 01:52:40 : DEBUG : logging_advanced_guide_02 : addition : 23 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : Inside Addition Function
# 10-08-2022 01:52:40 : WARNING : logging_advanced_guide_02 : addition : 25 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : Warning : Parameter A is passed as String. Future versions won't support it.
# 10-08-2022 01:52:40 : INFO : logging_advanced_guide_02 : addition : 33 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : Addition Function Completed Successfully
# 10-08-2022 01:52:40 : INFO : logging_advanced_guide_02 : <module> : 47 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : '20' + 20 = 40.0
#
# 10-08-2022 01:52:40 : DEBUG : logging_advanced_guide_02 : addition : 23 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : Inside Addition Function
# 10-08-2022 01:52:40 : ERROR : logging_advanced_guide_02 : addition : 35 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# 10-08-2022 01:52:40 : INFO : logging_advanced_guide_02 : <module> : 50 : (Process Details : (9200, MainProcess), Thread Details : (7896, MainThread))
# Log : A + 20 = None
