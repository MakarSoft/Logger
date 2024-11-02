# Example 14
# logging_advanced_guide_8.py 
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# В рамках этого примера мы демонстрируем, как мы можем определить более одного фильтра и прикрепить разные фильтры к разным обработчикам.
# Наш код для этого примера создал 3 разных обработчика.
# debug_info_messages — этот обработчик направляет сообщения журнала в стандартный вывод.
#                       К нему прикреплен фильтр с именем DebugAndInfoOnly, который фильтрует все сообщения, кроме INFO и WARNING.
# warnings_only       — этот обработчик направляет сообщения журнала в файл с именем warnings_only.log.
#                       К нему прикреплен фильтр с именем WarningsOnly, который фильтрует все сообщения журнала, кроме WARNING.
# errors_only         — этот обработчик направляет сообщения журнала в файл с именем errors_only.log.
#                       К нему прикреплен фильтр с именем ErrorsOnly, который фильтрует все сообщения журнала, кроме ERROR.
# Остальная часть нашего кода такая же, как в наших предыдущих примерах, которые мы использовали повторно.
# Когда мы запускаем приведенный ниже скрипт, мы можем заметить, что в стандартный вывод выводятся только сообщения INFO и WARNING.
# Сообщения журнала WARNING  регистрируются в файле warnings_only.log. Сообщения ERROR регистрируются в файле errors_only.log.
# Мы также отобразили содержимое файлов warnings_only.log и errors_only.log ниже.

import logging
from typing import Any, Optional

################ Logger ################################################################################
logger = logging.getLogger("Main")
logger.setLevel(logging.DEBUG)

####### Handler 1 : Info & Debug Messages ##############################################################
debug_info_messages = logging.StreamHandler()
debug_info_messages.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt="%(levelname)s : %(module)s : %(funcName)s : %(lineno)d : %(message)s")
debug_info_messages.setFormatter(formatter)
logger.addHandler(debug_info_messages)

class DebugAndInfoOnly(logging.Filter): ### Filters all messages except Info and Debug
    def filter(self, record):
        if record.levelno < 21:
            return True
        else:
            return False

debug_info_messages.addFilter(DebugAndInfoOnly()) ## Filter at Handler Level

#### Handler 2 : Warnings Messages ######################################################################
warnings_only = logging.FileHandler("warnings_only.log")
warnings_only.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt="%(levelname)s : %(module)s : %(funcName)s : %(lineno)d : %(message)s")
warnings_only.setFormatter(formatter)
logger.addHandler(warnings_only)

class WarningsOnly(logging.Filter): ### Filters all messages except Warning
    def filter(self, record):
        if 20 < record.levelno < 40: #record.levelno > 20 and record.levelno < 40:
            return True
        else:
            return False

warnings_only.addFilter(WarningsOnly())      ## Filter at Handler Level

###### Handler 3 : Errors Only ##########################################################################
errors_only = logging.FileHandler("errors_only.log")
errors_only.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt="%(levelname)s : %(module)s : %(funcName)s : %(lineno)d : %(message)s")
errors_only.setFormatter(formatter)
logger.addHandler(errors_only)

class ErrorsOnly(logging.Filter): ### Filters all messages except Error
    def filter(self, record):
        if 30 < record.levelno < 50: #record.levelno > 30 and record.levelno < 50:
            return True
        else:
            return False

errors_only.addFilter(ErrorsOnly())     ## Filter at Handler Level


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

    result = addition(20, "20")
    logger.info("Addition of {} & {} is : {}\n".format(20, "'20'", result))

    result = addition("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))

# StreamHandler ==========================================================
# INFO : logging_advanced_guide_08 : <module> : 98 : Current Log Level : 1
#
# DEBUG : logging_advanced_guide_08 : addition : 78 : Inside Addition Function
# INFO : logging_advanced_guide_08 : addition : 88 : Addition Function Completed Successfully
# INFO : logging_advanced_guide_08 : <module> : 101 : Addition of 10 & 20 is : 30.0
#
# DEBUG : logging_advanced_guide_08 : addition : 78 : Inside Addition Function
# INFO : logging_advanced_guide_08 : addition : 88 : Addition Function Completed Successfully
# INFO : logging_advanced_guide_08 : <module> : 104 : Addition of '20' & 20 is : 40.0
#
# DEBUG : logging_advanced_guide_08 : addition : 78 : Inside Addition Function
# INFO : logging_advanced_guide_08 : addition : 88 : Addition Function Completed Successfully
# INFO : logging_advanced_guide_08 : <module> : 107 : Addition of 20 & '20' is : 40.0
#
# DEBUG : logging_advanced_guide_08 : addition : 78 : Inside Addition Function
# INFO : logging_advanced_guide_08 : <module> : 110 : Addition of A & 20 is : None


# errors_only.log ========================================================
# ERROR : logging_advanced_guide_08 : addition : 91 : Error Type : ValueError, Error Message : could not convert string to float: 'A'

# warnings_only.log ======================================================
# WARNING : logging_advanced_guide_08 : addition : 81 : Warning : Parameter A is passed as String. Future versions won't support it.
# WARNING : logging_advanced_guide_08 : addition : 84 : Warning : Parameter B is passed as String. Future versions won't support it.


