# Example 5
# logging_example_05.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# -----------------------------------------------------------
# Настройка по умолчанию - logging.basicConfig() — настроит регистратор на
# запись в консоль в следующем формате:
# log_level:logger_name:log_message
# например:
# ERROR:root:This is an error message
#
# -----------------------------------------------------------
# Хотя можно передать любую переменную, которая может быть представлена ​​в
# виде строки, из вашей программы в качестве сообщения в ваши журналы,
# есть некоторые основные элементы, которые уже являются частью класса
# LogRecord и могут быть легко добавлены в выходной формат.
# Если вы хотите зарегистрировать идентификатор процесса вместе с уровнем
# и сообщением, вы можете сделать что-то вроде этого:
#        import logging
#        logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
#        logging.warning('This is a Warning')
#
#        18472-WARNING-This is a Warning
#
# параметр format может принимать строку с атрибутами LogRecord в любом порядке
# https://docs.python.org/3/library/logging.html#logrecord-attributes
#

# ------------------------------------------------------------
#  import logging
#  logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
#  logging.info('Admin logged in')
#
#  2018-07-11 20:12:06,288 - Admin logged in
#
# Формат даты можно изменить с помощью атрибута datefmt, который использует тот
# же язык форматирования, что и функции форматирования в модуле datetime,
# например time.strftime()
#
#  import logging
#  logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
#  logging.warning('Admin logged out')
#
#  12-Jul-18 20:53:19 - Admin logged out
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
#

# ------------------------------------------------------------
# В большинстве случаев вы захотите включить в журналы динамическую информацию
# из вашего приложения.
# Вы видели, что методы ведения журнала принимают строку в качестве аргумента,
# и может показаться естественным форматировать строку с переменными данными в
# отдельной строке и передавать ее методу журнала.
# Но на самом деле это можно сделать напрямую, используя строку формата для
# сообщения и добавляя переменные данные в качестве аргументов. Вот пример:
#       import logging
#       name = 'John'
#       logging.error('%s raised an error', name)
# или
#       import logging
#       name = 'John'
#       logging.error(f'{name} raised an error')

# ------------------------------------------------------------
# Модуль ведения журнала также позволяет захватывать полные трассировки стека
# в приложении.
# Информация об исключении может быть получена, если параметр exc_info
# передается как True, а функции ведения журнала вызываются следующим образом:
#
#       import logging
#       a = 5
#       b = 0
#       try:
#         c = a / b
#       except Exception as e:
#         logging.error("Exception occurred", exc_info=True)

#       ERROR:root:Exception occurred
#       Traceback (most recent call last):
#         File "exceptions.py", line 6, in <module>
#           c = a / b
#       ZeroDivisionError: division by zero
#       [Finished in 0.2s]
#
# Если exc_info не установлен в True, выходные данные вышеприведенной
# программы ничего не сообщат нам об исключении, которое в реальном
# сценарии может быть не таким простым, как файл ZeroDivisionError.
#
# если вы ведете журнал из обработчика исключений, используйте метод
# logging.exception(), который регистрирует сообщение с уровнем ERROR
# и добавляет в сообщение информацию об исключении.
# Проще говоря, вызов logging.exception() похож на вызов logging.error(exc_info=True).
# Но поскольку этот метод всегда выводит информацию об исключении,
# его следует вызывать только из обработчика исключений. Например:
#       import logging
#       a, b = 5, 0
#       try:
#         c = a / b
#       except Exception as e:
#         logging.exception("Exception occurred")

# -----------------------------------------------------------------------------
# как можно форматировать сообщения и переопределять формат сообщения журнала
# по умолчанию log_level:logger_name:log_message, установленный с помощью
# logging.
#
# Указали два новых параметра с именами format и datefmt в методе basicConfig(),
# которые позволяют форматировать сообщение и дату в сообщении.
#
# Параметр формата принимает python-формат строку в формате %(variable_name)s.
#
# Модуль logging хранит различную информацию, связанную с ведением журнала,
# такую ​​как время, имя уровня, имя модуля, имя функции, номер строки в файле,
# сведения о процессе и потоке и т. д. в соответствующей переменной.
# Мы можем отформатировать строку Python с этими именами переменных для
# создания сообщения, и этот формат будет использоваться для каждого сообщения.
#
# В этом примере сообщение разделено на две строки.
# Первая строка сообщения состоит из
#   времени журнала, имени уровня журнала, имени модуля, имени функции, номера
# строки, сведений о процессе и сведений о потоке, разделенных двоеточием.
# Вторая строка сообщения содержит фактическое сообщение журнала.
# Также предоставлен формат даты, который мы хотим использовать для
# форматирования даты с использованием параметра datefmt.
# Мы можем увидеть изменение формата сообщения журнала по умолчанию при запуске
# скрипта.
# Обратите внимание на время, имя модуля, имя функции, номер строки, сведения о
# процессе и потоке, включенные в сообщения журнала.
# Список переменных, которые мы можем включить в строку формата, и их формат
# доступен по ссылке:
# https://docs.python.org/3/library/logging.html#logrecord-attributes.

import logging
from typing import Any, Optional

logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog Message : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S",
    level=logging.INFO,
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


################################################################################

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
# 10-08-2022 10:31:22 : INFO : logging_example_05 : addition : 18 : (Process Details : (11636, MainProcess), Thread Details : (3940, MainThread))
# Log Message : Addition Function Completed Successfully
# 10 + 20 = 30.0
#
# 10-08-2022 10:31:22 : WARNING : logging_example_05 : addition : 10 : (Process Details : (11636, MainProcess), Thread Details : (3940, MainThread))
# Log Message : Warning : Parameter A is passed as String. Future versions won't support it.
# 10-08-2022 10:31:22 : INFO : logging_example_05 : addition : 18 : (Process Details : (11636, MainProcess), Thread Details : (3940, MainThread))
# Log Message : Addition Function Completed Successfully
# '20' + 20 = 40.0
#
# 10-08-2022 10:31:22 : ERROR : logging_example_05 : addition : 20 : (Process Details : (11636, MainProcess), Thread Details : (3940, MainThread))
# Log Message : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# A + 20 = None
