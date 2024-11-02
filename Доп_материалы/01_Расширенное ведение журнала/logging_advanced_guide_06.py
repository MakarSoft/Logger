# Example 12
# logging_advanced_guide_6.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# В этого примера мы снова демонстрируем, как мы можем использовать более одного обработчика файлов для направления вывода в разные места назначения.
# Наш код для этого примера создал три обработчика файлов.
# Первый обработчик файлов записывает все сообщения на уровне DEBUG и выше в файл с именем all.log .
# Второй обработчик файлов записывает все сообщения уровня WARNING и выше в файл с именем warnings.log .
# Третий обработчик файлов записывает все сообщения уровня ERROR и выше в файл с именем errors.log .
# Остальная часть нашего кода точно такая же, как в предыдущем примере. На этот раз мы не направляем сообщения журнала в стандартный вывод,
# поэтому, когда мы запустим этот скрипт, не будет никакого вывода, поскольку все сообщения журнала направляются в разные файлы.
# Когда мы запустим приведенный ниже сценарий, будут созданы три разных файла журнала, и сообщения журнала будут направляться в них в зависимости от
# уровня.

import logging
from typing import Any, Optional

################ Logger ##################################
logger = logging.getLogger("Main")
logger.setLevel(logging.DEBUG)

#### Handler 1 : All Messages ############################
all_messages = logging.FileHandler("{}.log".format("all"))
all_messages.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    fmt="%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S"
)
all_messages.setFormatter(formatter)
logger.addHandler(all_messages)

#### Handler 2 : Warnings and Above Messages #############
warn_n_above = logging.FileHandler("{}.log".format("warnings"))
warn_n_above.setLevel(logging.WARNING)
formatter = logging.Formatter(
    fmt="%(asctime)s : %(name)s : %(levelname)s : %(funcName)s : %(lineno)d : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S"
)
warn_n_above.setFormatter(formatter)
logger.addHandler(warn_n_above)

#### Handler 3 : Errors and Above Messages ################
error_n_above = logging.FileHandler("{}.log".format("errors"))
error_n_above.setLevel(logging.ERROR)
formatter = logging.Formatter(
    fmt="%(asctime)s : %(name)s : %(levelname)s : %(funcName)s : %(lineno)d : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S"
)
error_n_above.setFormatter(formatter)
logger.addHandler(error_n_above)

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
    logger.setLevel(1)
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))

    result = addition(10,20)
    logger.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logger.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))

# all.log ===========================================================
# 10-08-2022 03:24:53 : INFO : logging_advanced_guide_06 : <module> : 64 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Current Log Level : 1
#
# 10-08-2022 03:24:53 : DEBUG : logging_advanced_guide_06 : addition : 46 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Inside Addition Function
# 10-08-2022 03:24:53 : INFO : logging_advanced_guide_06 : addition : 55 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Addition Function Completed Successfully
# 10-08-2022 03:24:53 : INFO : logging_advanced_guide_06 : <module> : 67 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Addition of 10 & 20 is : 30.0
#
# 10-08-2022 03:24:53 : DEBUG : logging_advanced_guide_06 : addition : 46 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Inside Addition Function
# 10-08-2022 03:24:53 : WARNING : logging_advanced_guide_06 : addition : 48 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Warning : Parameter A is passed as String. Future versions won't support it.
# 10-08-2022 03:24:53 : INFO : logging_advanced_guide_06 : addition : 55 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Addition Function Completed Successfully
# 10-08-2022 03:24:53 : INFO : logging_advanced_guide_06 : <module> : 70 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Addition of '20' & 20 is : 40.0
#
# 10-08-2022 03:24:53 : DEBUG : logging_advanced_guide_06 : addition : 46 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Inside Addition Function
# 10-08-2022 03:24:53 : ERROR : logging_advanced_guide_06 : addition : 58 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# 10-08-2022 03:24:53 : INFO : logging_advanced_guide_06 : <module> : 73 : (Process Details : (8220, MainProcess), Thread Details : (8284, MainThread))
# Log : Addition of A & 20 is : None


# errors.log ==========================================================
# 10-08-2022 03:24:53 : Main : ERROR : addition : 58 : Error Type : ValueError, Error Message : could not convert string to float: 'A'


# warning.log =========================================================
# 10-08-2022 03:24:53 : Main : WARNING : addition : 48 : Warning : Parameter A is passed as String. Future versions won't support it.
# 10-08-2022 03:24:53 : Main : ERROR : addition : 58 : Error Type : ValueError, Error Message : could not convert string to float: 'A'


