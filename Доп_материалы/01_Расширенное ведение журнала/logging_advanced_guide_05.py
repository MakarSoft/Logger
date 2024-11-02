# Example 11
# logging_advanced_guide_05.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# В рамках этого примера демонстрируется, как мы можем направлять сообщения журнала в разные места назначения,
# используя разные обработчики, прикрепленные к одному и тому же экземпляру регистратора.
#
# FileHandler(filename, mode='a') — этот конструктор принимает в качестве входного имени файла и создает экземпляр FileHandler,
# который затем будет использоваться для направления регистратором log-сообщений в файл, к которому он прикреплен.
# Большая часть нашего кода для этого примера такая же, как наш код для 'Example 8', с добавлением строк, связанных с обработчиком файлов.
# Мы определили обработчик файла с именем Main.log . Мы установили уровень журнала обработчика файлов на WARNING , поэтому он будет
# обрабатывать только сообщения журнала с уровнем предупреждения и выше. Мы также прикрепили этот обработчик к нашему регистратору.
# Это выдаст предупреждение, и вышеуказанные сообщения будут сохранены в файле Main.log .

# Когда мы запускаем приведенный ниже код, вывод точно такой же, как и в примере 8.
# Мы также отобразили содержимое файла Main.log, в котором есть сообщения журнала с уровнем WARNING и выше.


import logging
from typing import Any, Optional

################ Logger ####################
logger = logging.getLogger("Main")
logger.setLevel(logging.DEBUG)

################ Handler 1 #################
std_out = logging.StreamHandler()
std_out.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    fmt="%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S")

std_out.setFormatter(formatter) ### Register Formatter with Handler.
logger.addHandler(std_out)      ### Register Handler with Logger.

################ Handler 2 #################
file_handler = logging.FileHandler("{}.log".format("Main"))
file_handler.setLevel(logging.WARNING)
formatter = logging.Formatter(
    fmt="%(asctime)s : %(name)s : %(levelname)s : %(funcName)s : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S")

file_handler.setFormatter(formatter) ### Register Formatter with Handler.
logger.addHandler(file_handler)      ### Register Handler with Logger.

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

    result = addition("20", 20)
    logger.info("Addition of {} & {} is : {}\n".format("'20'", 20, result))

    result = addition(20, "20")
    logger.info("Addition of {} & {} is : {}\n".format(20, "'20'", result))

    result = addition("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))

# 20-09-2022 04:32:47 : INFO : logging_advanced_guide_05 : <module> : Current Log Level : 1
#
# 20-09-2022 04:32:47 : DEBUG : logging_advanced_guide_05 : addition : Inside Addition Function
# 20-09-2022 04:32:47 : INFO : logging_advanced_guide_05 : addition : Addition Function Completed Successfully
# 20-09-2022 04:32:47 : INFO : logging_advanced_guide_05 : <module> : Addition of 10 & 20 is : 30.0
#
# 20-09-2022 04:32:47 : DEBUG : logging_advanced_guide_05 : addition : Inside Addition Function
# 20-09-2022 04:32:48 : WARNING : logging_advanced_guide_05 : addition : Warning : Parameter A is passed as String. Future versions won't support it.
# 20-09-2022 04:32:48 : INFO : logging_advanced_guide_05 : addition : Addition Function Completed Successfully
# 20-09-2022 04:32:48 : INFO : logging_advanced_guide_05 : <module> : Addition of '20' & 20 is : 40.0
#
# 20-09-2022 04:32:48 : DEBUG : logging_advanced_guide_05 : addition : Inside Addition Function
# 20-09-2022 04:32:48 : WARNING : logging_advanced_guide_05 : addition : Warning : Parameter B is passed as String. Future versions won't support it.
# 20-09-2022 04:32:48 : INFO : logging_advanced_guide_05 : addition : Addition Function Completed Successfully
# 20-09-2022 04:32:48 : INFO : logging_advanced_guide_05 : <module> : Addition of 20 & '20' is : 40.0
#
# 20-09-2022 04:32:48 : DEBUG : logging_advanced_guide_05 : addition : Inside Addition Function
# 20-09-2022 04:32:48 : ERROR : logging_advanced_guide_05 : addition : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# 20-09-2022 04:32:48 : INFO : logging_advanced_guide_05 : <module> : Addition of A & 20 is : None

#------------------------------------
# это попало в файл....
# 20-09-2022 04:32:48 : Main : WARNING : addition : Warning : Parameter A is passed as String. Future versions won't support it.
# 20-09-2022 04:32:48 : Main : WARNING : addition : Warning : Parameter B is passed as String. Future versions won't support it.
# 20-09-2022 04:32:48 : Main : ERROR : addition : Error Type : ValueError, Error Message : could not convert string to float: 'A'

