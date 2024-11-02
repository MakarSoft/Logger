# Example 3
# logging_example_03.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# В этом примере демонстрируется, как мы можем переопределить уровень ведения
# журнала по умолчанию (WARNING), установленный с помощью logging.
#
# Код этого примера точно такой же, как и в примере logging_example_02.py, с
# добавлением только двух строк, которые связаны с переопределением уровня
# журнала по умолчанию.
#
# В модуле logging есть метод с именем basicConfig(), позволяющий
# переопределить настройки журнала по умолчанию, такие как уровень журнала,
# формат журнала, формат даты, местоположение журнала и т.д.
#
# Мы установили уровень журнала DEBUG, что приведет к печати всех сообщений
# журнала с уровнем DEBUG и выше.
# При запуске скрипта, мы можем заметить, что он распечатывает сообщения
# журнала всех уровней.
# Обратите внимание, что по умолчанию уровни журнала внутренне представлены
# целочисленным значением.
#
# !!! Мы можем указать значение уровня как целое число, и все сообщения с
# уровнем выше и выше будут напечатаны.

import logging
from typing import Any, Optional

logging.basicConfig(level=logging.DEBUG)  #


def addition(a: Any, b: Any) -> Optional[float]:

    logging.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logging.warning(
            "Warning : Parameter A is passed as String. Future versions won't support it."
        )

    if isinstance(b, str) and b.isdigit():
        logging.warning(
            "Warning : Parameter B is passed as String. Future versions won't support it."
        )

    result = None
    try:
        result = float(a) + float(b)
        logging.info("Addition Function Completed Successfully")
    except Exception as e:
        logging.error(
            "Error Type : {}, Error Message : {}".format(type(e).__name__, e)
        )
    finally:
        return result


# ##############################################################################

if __name__ == "__main__":
    print("Current Log Level : {}\n".format(logging.DEBUG))

    result = addition(10, 20)
    print("{} + {} = {}\n".format(10, 20, result))

    result = addition("20", 20)
    print("{} + {} = {}\n".format("'20'", 20, result))

    result = addition(20, "20")
    print("{} + {} = {}\n".format(20, "'20'", result))

    result = addition("A", 20)
    print("{} + {} = {}".format("A", 20, result))

# Current Log Level : 10
#
# DEBUG:root:Inside Addition Function
# INFO:root:Addition Function Completed Successfully
# 10 + 20 = 30.0
#
# DEBUG:root:Inside Addition Function
# WARNING:root:Warning : Parameter A is passed as String. Future versions won't support it.
# INFO:root:Addition Function Completed Successfully
# '20' + 20 = 40.0
#
# DEBUG:root:Inside Addition Function
# ERROR:root:Error Type : ValueError, Error Message : could not convert string to float: 'A'
# A + 20 = None
