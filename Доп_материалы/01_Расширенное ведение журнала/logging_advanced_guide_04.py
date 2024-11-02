# Example 10
# logging_advanced_guide_4.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# В рамках этог примера демонстрируется, как мы можем прикрепить имя к уровню журнала и как мы можем регистрировать сообщения,
# используя метод log() экземпляра Logger .

# addLevelName(log_level, name) — этот метод прикрепляет указанное имя, к указанному уровню журнала.
# Все сообщения журнала, которые затем регистрируются на этом уровне, будут печатать имя, определенное с помощью этого метода для имени уровня.
# Код этого примера точно такой же, как наш код для 'Example 8' с небольшими изменениями.
# Мы определили новый уровень журнала с именем INFORMATION для сообщений, регистрируемых на уровне 15.
# Помимо этого, на этот раз мы записывали сообщения с использованием метода log() экземпляра Logger.


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
    datefmt="%d-%m-%Y %I:%M:%S")

std_out.setFormatter(formatter) ### Register Formatter with Handler.
logger.addHandler(std_out)      ### Register Handler with Logger.

######## Define Logging Level Name ######
logging.addLevelName(15, "INFORMATION")

def addition(a: Any, b: Any) -> Optional[float]:

    logger.log(10, "Inside Addition Function")
    
    if isinstance(a, str) and a.isdigit():
        logger.log(30, "Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logger.log(30, "Warning : Parameter B is passed as String. Future versions won't support it.")

    try:
        result = float(a) + float(b)
        logger.log(15, "Addition Function Completed Successfully")
        return result
    except Exception as e:
        logger.log(40, "Error Type : {}, Error Message : {}".format(type(e).__name__, e))
        return None

################################################################################

if __name__ == "__main__":
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))

    result = addition(10,20)
    logger.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logger.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition(20,"20")
    logger.info("Addition of {} & {} is : {}\n".format(20, "'20'", result))

    result = addition("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))

# 10-08-2022 03:04:26 : INFO : logging_advanced_guide_04 : <module> : 52 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Current Log Level : 10
#
# 10-08-2022 03:04:26 : DEBUG : logging_advanced_guide_04 : addition : 35 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Inside Addition Function
# 10-08-2022 03:04:26 : INFORMATION : logging_advanced_guide_04 : addition : 44 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Addition Function Completed Successfully
# 10-08-2022 03:04:26 : INFO : logging_advanced_guide_04 : <module> : 55 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Addition of 10 & 20 is : 30.0
#
# 10-08-2022 03:04:26 : DEBUG : logging_advanced_guide_04 : addition : 35 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Inside Addition Function
# 10-08-2022 03:04:26 : WARNING : logging_advanced_guide_04 : addition : 37 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Warning : Parameter A is passed as String. Future versions won't support it.
# 10-08-2022 03:04:26 : INFORMATION : logging_advanced_guide_04 : addition : 44 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Addition Function Completed Successfully
# 10-08-2022 03:04:26 : INFO : logging_advanced_guide_04 : <module> : 58 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Addition of '20' & 20 is : 40.0
#
# 10-08-2022 03:04:26 : DEBUG : logging_advanced_guide_04 : addition : 35 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Inside Addition Function
# 10-08-2022 03:04:26 : ERROR : logging_advanced_guide_04 : addition : 47 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# 10-08-2022 03:04:26 : INFO : logging_advanced_guide_04 : <module> : 61 : (Process Details : (8048, MainProcess), Thread Details : (4640, MainThread))
# Log : Addition of A & 20 is : None
