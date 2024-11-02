# Example 6
# logging_example_06.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# Отличия от logging_example_05.py:
# - переместили функцию addition в файл add_operations.py
# - изменили формат даты в нашем лог-сообщении ("%d-%m-%Y %I:%M:%S" -> "%d-%B,%Y %I:%M:%S %p"): (10-08-2022 10:31:22 -> 10-August,2022 10:31:22 AM)

import logging
from arithmetic_operations import addition

logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog Message : %(message)s",
    datefmt="%d-%B,%Y %I:%M:%S %p",
    level=logging.INFO,
)

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
# 10-August,2022 11:44:47 AM : INFO : arithmetic_operations : addition : 17 : (Process Details : (3596, MainProcess), Thread Details : (13696, MainThread))
# Log Message : Addition Function Completed Successfully
# 10 + 20 = 30.0
#
# 10-August,2022 11:44:47 AM : WARNING : arithmetic_operations : addition : 9 : (Process Details : (3596, MainProcess), Thread Details : (13696, MainThread))
# Log Message : Warning : Parameter A is passed as String. Future versions won't support it.
# 10-August,2022 11:44:47 AM : INFO : arithmetic_operations : addition : 17 : (Process Details : (3596, MainProcess), Thread Details : (13696, MainThread))
# Log Message : Addition Function Completed Successfully
# '20' + 20 = 40.0
#
# 10-August,2022 11:44:47 AM : ERROR : arithmetic_operations : addition : 19 : (Process Details : (3596, MainProcess), Thread Details : (13696, MainThread))
# Log Message : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# A + 20 = None
