# Example 16
# logging_advanced_guide_10.py 
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python 
# https://coderzcolumn.com/tutorials/python/threading-guide-to-multithreading-in-python-with-simple-examples

# В рамках этого последнего примера мы продемонстрируем, как мы можем регистрировать сообщения в многопоточной среде.
# Наш код для этого примера почти такой же, как наш код для предыдущего примера, с той лишь разницей, что на этот раз мы используем потоки вместо процессов.
# Мы изменили формат сообщения журнала, чтобы включить сведения о цепочке (идентификатор и имя).
# Мы использовали модуль threading для создания потоков. Если вы заинтересованы в изучении многопоточности, пожалуйста, не стесняйтесь
# https://coderzcolumn.com/tutorials/python/threading-guide-to-multithreading-in-python-with-simple-examples (threading — подробное руководство по многопоточности в Python с простым примером)
# 
# Когда мы запускаем приведенный ниже сценарий, мы можем узнать из вывода, какой поток зарегистрировал какое сообщение журнала на основе сведений о потоке,
# включенных в log-сообщение.

import logging
import threading
from typing import Any, Optional

################ Logger #####################
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

############## Handler ######################
std_out = logging.StreamHandler()
std_out.setLevel(logging.DEBUG)

############## Formatter ####################
formatter = logging.Formatter(
    fmt="%(asctime)s : %(levelname)s : ((Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s)) : %(message)s",
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

#################################################################################

if __name__ == "__main__":
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))

    t1 = threading.Thread(target=addition, args=(10,20), name="Addition1")
    t1.start()

    t2 = threading.Thread(target=addition, args=("20",20), name="Addition2")
    t2.start()

    t3 = threading.Thread(target=addition, args=("A",20), name="Addition3")
    t3.start()

    t1.join()
    t2.join()
    t3.join()

# 20-09-2022 05:12:41 : INFO : ((Process Details : (13812, MainProcess), Thread Details : (13840, MainThread)) : Current Log Level : 10
#
# 20-09-2022 05:12:41 : DEBUG : ((Process Details : (13812, MainProcess), Thread Details : (11716, Addition1)) : Inside Addition Function
# 20-09-2022 05:12:41 : INFO : ((Process Details : (13812, MainProcess), Thread Details : (11716, Addition1)) : Addition Function Completed Successfully
# 20-09-2022 05:12:41 : DEBUG : ((Process Details : (13812, MainProcess), Thread Details : (4452, Addition2)) : Inside Addition Function
# 20-09-2022 05:12:41 : INFO : ((Process Details : (13812, MainProcess), Thread Details : (11716, Addition1)) : Addition of 10 & 20 is : 30.0
#
# 20-09-2022 05:12:41 : DEBUG : ((Process Details : (13812, MainProcess), Thread Details : (9792, Addition3)) : Inside Addition Function
# 20-09-2022 05:12:41 : WARNING : ((Process Details : (13812, MainProcess), Thread Details : (4452, Addition2)) : Warning : Parameter A is passed as String. Future versions won't support it.
# 20-09-2022 05:12:41 : ERROR : ((Process Details : (13812, MainProcess), Thread Details : (9792, Addition3)) : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# 20-09-2022 05:12:41 : INFO : ((Process Details : (13812, MainProcess), Thread Details : (4452, Addition2)) : Addition Function Completed Successfully
# 20-09-2022 05:12:41 : INFO : ((Process Details : (13812, MainProcess), Thread Details : (9792, Addition3)) : Addition of A & 20 is : None
#
# 20-09-2022 05:12:41 : INFO : ((Process Details : (13812, MainProcess), Thread Details : (4452, Addition2)) : Addition of 20 & 20 is : 40.0
