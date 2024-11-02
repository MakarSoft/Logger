# Example 9_1
# logging_advanced_guide_03_1.py
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python


# Как работает иерархия в регистраторах.
# Создаём один корневой регистратор, а затем один подчиненный ему регистратор, чтобы объяснить использование иерархии.

# код для этого примера начинается с создания экземпляра Logger,
# создаем для него обработчик потока,
# прикрепляет средство форматирования к обработчику и
# прикрепляет обработчик к регистратору.
# Этот экземпляр регистратора будет нашим корневым регистратором.
# Мы дали ему имя arithmetic_ops. Корневой регистратор установлен на уровне INFO.

# Затем мы создали класс с именем Addition.
# Внутри него мы создали новый регистратор с именем arithmetic_ops.Addition.
# Этот регистратор будет вспомогательным регистратором нашего корневого регистратора (arithmetic_ops).
# Мы также создали обработчик и средство форматирования для этого вспомогательного регистратора.
# Этот вспомогательный регистратор будет передавать все зарегистрированные им сообщения своим родительским регистраторам.
# Вспомогательный регистратор установлен на уровне DEBUG .

# Логика, которую мы использовали внутри метода add() в наших предыдущих примерах, теперь перенесена в метод add() класса Addition.
# Мы используем вспомогательный регистратор, созданный внутри экземпляра Addition, для регистрации сообщений внутри метода add().

# Основная часть кода такая же, как и в наших предыдущих примерах, с той лишь разницей, что вместо вызова метода add() мы вызываем метод add() для экземпляра Addition.
# В этой основной части мы используем корневой регистратор для регистрации сообщений.

# Когда мы запускаем приведенный ниже скрипт, мы можем заметить, что сообщения INFO и выше уровня журнала печатаются дважды (один раз вспомогательным регистратором и
# один корневым регистратором).
# Это происходит потому, что мы также прикрепили обработчик к вспомогательному регистратору, который обрабатывает сообщения журнала,
# а затем передает их родительскому регистратору, у которого также есть обработчик для их обработки.
#
# Мы можем избежать повторения сообщений журнала, используя атрибут propagate (распространение) в дочернем регистратое, установив его значение в False (logging_advanced_guide_03_2.py)

import logging
from typing import Any, Optional

################ Module Logger #################
logger = logging.getLogger("arithmetic_ops")
logger.setLevel(logging.INFO)

############## Handler #########################
std_out = logging.StreamHandler()
std_out.setLevel(logging.INFO)

############## Formatter #######################
formatter = logging.Formatter(
    fmt="%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S"
)

std_out.setFormatter(formatter) ### Register Formatter with Handler.
logger.addHandler(std_out)      ### Register Handler with Logger.

#===============================================================================

class Addition:
    def __init__(self) -> None:

        ################ Class Logger #############
        self.logger = logging.getLogger("arithmetic_ops.Addition")
        #self.logger.propagate=False
        self.logger.setLevel(logging.DEBUG)

        ############## Handler ####################
        std_out = logging.StreamHandler()
        std_out.setLevel(logging.DEBUG)

        ############## Formatter ##################
        formatter = logging.Formatter(
            fmt="%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s",
            datefmt="%d-%m-%Y %I:%M:%S")

        std_out.setFormatter(formatter) ### Register Formatter with Handler.
        self.logger.addHandler(std_out) ### Register Handler with Logger.

    def add(self, a: Any, b: Any) -> Optional[float]:

        self.logger.debug("Inside Addition Function")

        if isinstance(a, str) and a.isdigit():
            self.logger.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

        if isinstance(b, str) and b.isdigit():
            self.logger.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

        try:
            result = float(a) + float(b)
            self.logger.info("Addition Function Completed Successfully")
            return result
        except Exception as e:
            self.logger.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
            return None

################################################################################

if __name__ == "__main__":

    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))

    addition = Addition()
    result = addition.add(10,20)
    logger.info("{} + {} = {}\n".format(10,20, result))

    result = addition.add("20",20)
    logger.info("{} + {} = {}\n".format("'20'",20, result))

    result = addition.add(20, "20")
    print("{} + {} = {}\n".format(20, "'20'", result))

    result = addition.add("A",20)
    logger.info("{} + {} = {}".format("A",20, result))

# 10-08-2022 02:30:35 : INFO : arithmetic_ops : <module> : Current Log Level : 20
#
# 10-08-2022 02:31:19 : DEBUG : arithmetic_ops.Addition : add : Inside Addition Function
# 10-08-2022 02:32:05 : INFO : arithmetic_ops.Addition : add : Addition Function Completed Successfully
# 10-08-2022 02:32:05 : INFO : arithmetic_ops.Addition : add : Addition Function Completed Successfully
# 10-08-2022 02:32:16 : INFO : arithmetic_ops : <module> : 10 + 20 = 30.0
#
# 10-08-2022 02:32:24 : DEBUG : arithmetic_ops.Addition : add : Inside Addition Function
# 10-08-2022 02:32:32 : WARNING : arithmetic_ops.Addition : add : Warning : Parameter A is passed as String. Future versions won't support it.
# 10-08-2022 02:32:32 : WARNING : arithmetic_ops.Addition : add : Warning : Parameter A is passed as String. Future versions won't support it.
# 10-08-2022 02:33:06 : INFO : arithmetic_ops.Addition : add : Addition Function Completed Successfully
# 10-08-2022 02:33:06 : INFO : arithmetic_ops.Addition : add : Addition Function Completed Successfully
# 10-08-2022 02:33:27 : INFO : arithmetic_ops : <module> : '20' + 20 = 40.0
#
# 10-08-2022 02:33:30 : DEBUG : arithmetic_ops.Addition : add : Inside Addition Function
# 10-08-2022 02:33:45 : ERROR : arithmetic_ops.Addition : add : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# 10-08-2022 02:33:45 : ERROR : arithmetic_ops.Addition : add : Error Type : ValueError, Error Message : could not convert string to float: 'A'
# 10-08-2022 02:33:55 : INFO : arithmetic_ops : <module> : A + 20 = None
