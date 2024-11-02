# Example 15
# logging_advanced_guide_09.py 
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python
# https://coderzcolumn.com/tutorials/python/multiprocessing-basic

# В рамках этого примера мы демонстрируем, как ведение журнала можно использовать в многопроцессорных средах для регистрации сообщений от разных процессов.
# Код для этого примера начинается с создания экземпляра регистратора и присоединения к нему обработчика потока.
# Мы также изменили средство форматирования, чтобы включить информацию об идентификаторе и имени процесса, чтобы мы могли знать, какой процесс записал сообщение.
# Наше определение метода сложения такое же, как и в предыдущих примерах.
# Основная часть нашего кода теперь создает три процесса, каждый из которых выполняет метод add() с разными настройками параметров.
# Мы также заставили основной процесс ожидать завершения всех трех подпроцессов.
# Мы использовали многопроцессорный модуль для создания процессов. Если вам интересно узнать об этом, пожалуйста, не стесняйтесь:
# https://coderzcolumn.com/tutorials/python/multiprocessing-basic (multiprocessing — Простое руководство по созданию процессов и пула процессов в Python)
# 
# Когда мы запускаем приведенный ниже скрипт, мы можем заметить из выходных сообщений журнала, зарегистрированных различными процессами,
# на основе их идентификатора и имени.

import logging
import multiprocessing
from typing import Any, Optional

################ Logger #####################
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

############## Handler ######################
std_out = logging.StreamHandler()
std_out.setLevel(logging.DEBUG)

############## Formatter ####################
formatter = logging.Formatter(
    fmt="%(asctime)s : %(levelname)s : (Process Details : (%(process)d, %(processName)s)) : %(message)s",
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

    try:
        result = float(a) + float(b)
        logger.info("Addition Function Completed Successfully")
        logger.info("Addition of {} & {} is : {}\n".format(a,b, result))
    except Exception as e:
        logger.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
        logger.info("Addition of {} & {} is : {}\n".format(a,b, None))

################################################################################

if __name__ == "__main__":
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))

    p1 = multiprocessing.Process(target=addition, args=(10,20), name="Addition1")
    p1.start()

    p2 = multiprocessing.Process(target=addition, args=("20",20), name="Addition2")
    p2.start()

    p3 = multiprocessing.Process(target=addition, args=("A",20), name="Addition3")
    p3.start()

    p1.join()
    p2.join()
    p3.join()


# 20-09-2022 05:09:39 : INFO : (Process Details : (11400, MainProcess)) : Current Log Level : 10
#
# 20-09-2022 05:09:40 : DEBUG : (Process Details : (8744, Addition1)) : Inside Addition Function
# 20-09-2022 05:09:40 : INFO : (Process Details : (8744, Addition1)) : Addition Function Completed Successfully
# 20-09-2022 05:09:40 : INFO : (Process Details : (8744, Addition1)) : Addition of 10 & 20 is : 30.0
#
# 20-09-2022 05:09:40 : DEBUG : (Process Details : (12388, Addition3)) : Inside Addition Function
# 20-09-2022 05:09:40 : ERROR : (Process Details : (12388, Addition3)) : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# 20-09-2022 05:09:40 : DEBUG : (Process Details : (14712, Addition2)) : Inside Addition Function
# 20-09-2022 05:09:40 : INFO : (Process Details : (12388, Addition3)) : Addition of A & 20 is : None
#
# 20-09-2022 05:09:40 : WARNING : (Process Details : (14712, Addition2)) : Warning : Parameter A is passed as String. Future versions won't support it.
# 20-09-2022 05:09:40 : INFO : (Process Details : (14712, Addition2)) : Addition Function Completed Successfully
# 20-09-2022 05:09:40 : INFO : (Process Details : (14712, Addition2)) : Addition of 20 & 20 is : 40.0
#
