# Example 4
# logging_example_04.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python
#
# Как мы можем записывать сообщения в отдельный файл.
#
# Добавили нескольких параметров в вызове метода basicConfig().
#
# Мы получили имя файла, используя атрибут __file__, удалив расширение '.py'.
# Затем мы задали имя файла логов, добавив расширением .log, для параметра
# filename метода basicConfig().
#
# Параметр filemode задает режим файла, который будет использоваться с файлом
# журнала. Значение параметра filemode по умолчанию — 'a', что приведет к
# добавлению новых сообщений журнала к существующим сообщениям журнала каждый
# раз, когда мы запускаем приложение.
# Мы установили для этого параметра значение 'w', чтобы он перезаписывал старые
# сообщения журнала и сохранял в файле журнала только вновь созданные сообщения
# журнала. Выбор этого параметра остается за разработчиками.
#
# Когда мы запустили сценарий, мы можем заметить из вывода, что все сообщения
# журнала теперь удалены из стандартного вывода.
#
# Содержимое файла logging_example_04.log, куда переместились все сообщения
# журнала.
# INFO:root:Addition Function Completed Successfully
# WARNING:root:Warning : Parameter A is passed as String. Future versions won't support it.
# INFO:root:Addition Function Completed Successfully
# ERROR:root:Error Type : ValueError, Error Message : could not convert string to float: 'A'


import logging
from typing import Any, Optional

file_name = __file__.split(".")[0]

logging.basicConfig(
    filename="{}.log".format(file_name), filemode="w", level=logging.INFO
)


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
    print("Current Log Level : {}\n".format(logging.INFO))

    result = addition(10, 20)
    print("{} + {} = {}\n".format(10, 20, result))

    result = addition("20", 20)
    print("{} + {} = {}\n".format("'20'", 20, result))

    result = addition(20, "20")
    print("{} + {} = {}\n".format(20, "'20'", result))

    result = addition("A", 20)
    print("{} + {} = {}".format("A", 20, result))

# Current Log Level : 20
#
# 10 + 20 = 30.0
#
# '20' + 20 = 40.0
#
# A + 20 = None
