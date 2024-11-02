# Example 2
# logging_example_02.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# Пример основан на примере logging_example_01.py.
# Добавлен вывод Warning - сообщений
#
# Введены два оператора if в addition(a, b), которые проверяют тип и
# содержимое аргументов.
# Если аргументы являются строковыми и содержат только цифры, тогда будут
# записываться предупреждающие сообщения, информирующие о том, что этого не
# должно происходить в будущем, потому что, хотя в настоящее время это
# работает нормально, в будущих версиях это не сработает.
#
# Весь оставшийся код точно такой же, как в примере logging_example_01.py.
# При запуске, мы видим, что скрипт добавляет предупреждающее сообщение в
# журнал.
# Наш второй вызов функции добавления передал 20 в виде строки, которая
# приводит к предупреждающему сообщению.
#
# В этом примере печатаются сообщения с уровнем WARNING и выше.


import logging
from typing import Any, Optional


def addition(a: Any, b: Any) -> Optional[float]:

    result: Optional[float] = None
    logging.debug("Inside Addition Function")

    if isinstance(a, str) and a.isdigit():
        logging.warning(
            "Warning : Parameter A is passed as String. Future versions won't support it."
        )

    if isinstance(b, str) and b.isdigit():
        logging.warning(
            "Warning : Parameter B is passed as String. Future versions won't support it."
        )

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
    result = addition(10, 20)
    print("{} + {} = {}\n".format(10, 20, result))

    result = addition("20", 20)
    print("{} + {} = {}\n".format("'20'", 20, result))

    result = addition(20, "20")
    print("{} + {} = {}\n".format(20, "'20'", result))

    result = addition("A", 20)
    print("{} + {} = {}".format("A", 20, result))

# 10 + 20 = 30.0
#
# WARNING:root:Warning : Parameter A is passed as String. Future versions won't support it.
# '20' + 20 = 40.0
#
# ERROR:root:Error Type : ValueError, Error Message : could not convert string to float: 'A'
# A +20 = None
