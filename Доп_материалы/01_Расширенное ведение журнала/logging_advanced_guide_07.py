# Example 13
# logging_advanced_guide_07.py 
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python


# В этого примера мы покажем, как мы можем создавать фильтры для фильтрации/изменения сообщений журнала.
#
# Мы создали фильтр, определив класс с именем InfoAnWarningOnly, расширив класс logging.Filter.
# В классе мы реализовали (переопределили) метод filter() родительскогокласса logging.Filter.
# Метод filter принимает в качестве входного экземпляра LogRecord и возвращает True , если мы хотим сохранить эти log-сообщения, или иначе False.
# Внутри нашего метода filter() есть условие, которое возвращает True для сообщений с уровнем логирования между 10-31 ( INFO и WARNING ) и False для всех остальных сообщений.
# Это отфильтрует все сообщения, кроме INFO и WARNING.
# Затем у нас есть еще одно условие, которое проверяет уровень журнала 30 ( WARNING ) и изменяет сообщение журнала для этого уровня, добавляя перед ним строку Error : .
# Мы сделали это, чтобы показать, что предупреждающие сообщения теперь являются сообщениями об ошибках. Мы прикрепили этот фильтр к нашему регистратору с помощью
# метода addFilter().
# Наш остальной код почти такой же, как и в предыдущих примерах.
# Когда мы запускаем приведенный ниже скрипт, мы можем заметить, что регистрируются только сообщения журнала с уровнем INFO и WARNING.
# Все остальные сообщения фильтруются. Мы также можем заметить из предупреждающих сообщений, что к ним прикреплена строка Error:


import logging
from typing import Any, Optional

################ Logger ##############################
logger = logging.getLogger("Main")
logger.setLevel(logging.DEBUG)

####### Handler 1 : Info & Debug Messages ############
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt="%(levelname)s : %(module)s : %(funcName)s : %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class InfoAnWarningOnly(logging.Filter):
    def filter(self, record):
        if 10 < record.levelno < 31: # record.levelno > 10 and record.levelno < 31:
            if record.levelno == 30: ## Updating Warning messages to Error.
                record.levelno = 40
                record.msg = "Error : " + record.msg
            return True
        else:
            return False

logger.addFilter(InfoAnWarningOnly()) ## Filter at Logger Level

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

# INFO : logging_advanced_guide_07 : <module> : Current Log Level : 1
#
# INFO : logging_advanced_guide_07 : addition : Addition Function Completed Successfully
# INFO : logging_advanced_guide_07 : <module> : Addition of 10 & 20 is : 30.0
#
# WARNING : logging_advanced_guide_07 : addition : Error : Warning : Parameter A is passed as String. Future versions won't support it.
# INFO : logging_advanced_guide_07 : addition : Addition Function Completed Successfully
# INFO : logging_advanced_guide_07 : <module> : Addition of '20' & 20 is : 40.0
#
# INFO : logging_advanced_guide_07 : <module> : Addition of A & 20 is : None
