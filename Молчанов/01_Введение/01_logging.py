# Что такое логгер
# Лог - это журнал, протокол, в который записывается каждое ваше слово и каждое ваше действие
# Логгер - это тот кто ведет этот журнал (протокол)
# Как это все строектировано.
# 1. Есть специальный объекты Logger, которые имеют методы, вызывая которые
# мы и определяем какие события будут записаны, а какие нет.
# logger = logging.getLogger(имя_логгера) - получаем объект логгер

import logging
from pprint import pprint


logger = logging.getLogger()

print(logger)  # <RootLogger root (WARNING)>
# logger - экземляр класса RootLogger

pprint(logger.__dict__)
# {
# '_cache': {},
#  'disabled': False,
#  'filters': [],
#  'handlers': [],
#  'level': 30,
#  'name': 'root',
#  'parent': None,
#  'propagate': True
# }

pprint(dir(logger), indent=5, width=60, compact=True)
# [    '__class__', '__delattr__', '__dict__', '__dir__',
#      '__doc__', '__eq__', '__format__', '__ge__',
#      '__getattribute__', '__gt__', '__hash__', '__init__',
#      '__init_subclass__', '__le__', '__lt__', '__module__',
#      '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#      '__repr__', '__setattr__', '__sizeof__', '__str__',
#      '__subclasshook__', '__weakref__', '_cache', '_log',
#      'addFilter', 'addHandler', 'callHandlers', 'critical',
#      'debug', 'disabled', 'error', 'exception', 'fatal',
#      'filter', 'filters', 'findCaller', 'getChild',
#      'getEffectiveLevel', 'handle', 'handlers',
#      'hasHandlers', 'info', 'isEnabledFor', 'level', 'log',
#      'makeRecord', 'manager', 'name', 'parent', 'propagate',
#      'removeFilter', 'removeHandler', 'root', 'setLevel',
#      'warn', 'warning']

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")


def main(name: str) -> None:
    logger.warning(f"Enter in the main function: name = {name}")


if __name__ == "__main__":
    main("Hello")  # Enter in the main function: name = Hello


# ┌───────────┐
# │  Logger   │
# └───────────┘
#       │
#       ↓
# ┌───────────┐
# │ LogRecord │
# └───────────┘
#       │         ┌───────────┐
#       │   ┌─────│ LogRecord │─>────┐
#       ↓   │     └───────────┘      │
# ┌───────────┐                    ┌───────────┐
# │  Handler  │                    │ Formatter │
# └───────────┘                    └───────────┘
#       │   │     ┌───────────┐      │
#       │   └───<─│   string  │──────┘
#       ↓         └───────────┘
# ┌───────────┐
# │  output   │
# └───────────┘

# При вызове методов логеров Logger (напр. logger.warning() ), логеры
# создают внутри себя специальные объекты, которые являются экземплярами
# класса LogRecord и которые содержат всю необходимую информацию о
# произошедшем событии (имя ф-ции в которой мы вызвали метод логера,
# имя модуля, в котором это произошло, номер строки, время, когда
# произошло это событие и т.д)
# Полный список атрибутов можно посмотреть в документации:
# https://docs.python.org/3/library/logging.html#logrecord-attributes
# https://docs-python.ru/standart-library/paket-logging-python/obekt-logrecord-modulja-logging/
# полный список тех данных, которые записываются в LogRecord
# Собственно LogRecord и содержит все те данные, которые пишутся в лог
# Итак, в момент вызова logger.warning() - logger создал объект - экземпляр
# класса LogRecord затем, этот объект LogRecord отправляется логером в его
# обработчики (Handler).
# Обработчики фильтруют полученные сообщения (объекты LogRecord) и с нужными
# из них что-то делают (зависывают в лог-файл, на консоль, на почту и т.п.).
# Обработчиков в модуле logging достаточно много. Чаще всего используются
# обработчики записи логов в файлы, вывод в консоль и отправки по электронной
# почте. Дефолтный обработчик (используемый в данном конкретном случае)
# выводит сообщение в консоль
#
# Для записи в лог, объект LogRecord надо преобразовать в строку и эта
# строка должна иметь определенный вид (тот вид, который мы захотим).
# За это преобразование отвечают специальные объекты класса Formatter
# (и его подклассы).
# Они занимаются формированием итоговой строки по шаблону, который мы
# указываем и именно эта строка, в итоге, и будет записана в лог.
#
# Итак, есть три объекта, и все три участвуют в создании записи лога:
# - Logger - объект, который предоставляет нам API для записи сообщений в лог.
#   Логеры создают объекты LogRecord
# - Обрабтчики Handler, которые записывают сообщение туда куда нам нужно,
# но прежде чем обработчик выполнит свою задачу по записи данных в лог,
# он передает объект LogRecord в закрепленный за ним форматировщик Formatter,
# который создаст строку нужного нам вида (это третий объект)
# ------------------------------------------------------------------
