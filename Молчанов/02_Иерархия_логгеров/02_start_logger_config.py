import logging

# Использование корневого логгера - объект класса RootLogger
# Создается он просто:
# Если в ф-цию getLogger мы не передаём аргумент (она может принимать
# максимум один аргумент - имя), то она создает корневой logger (объект
# класса RootLogger и именем root), или возвращает имеющийся, если он
# уже был создан где-то в другом месте

# logger = logging.getLogger()
# print(logger)
# # <RootLogger root (WARNING)>

# logging.basicConfig()

app_logger = logging.getLogger("app_logger")
print(app_logger)
# <Logger app_logger (WARNING)>

# app_logger - это дочерний logger, по отношению к корневому
print(app_logger.parent)
# <RootLogger root (WARNING)>

# имеется следующая иерархия логгеров:
# есть корневой логгер и есть его дочерний логгер
# root.app_logger
print("app_logger Handlers: ", app_logger.handlers)  # []

console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)
print("app_logger Handlers: ", app_logger.handlers)  # []

print()
print("Root Handlers: ", app_logger.parent.handlers)
print()


utils_logger = logging.getLogger("app_logger.utils")
print(utils_logger)
# <Logger app_logger.utils (WARNING)>
print(utils_logger.parent)
# <Logger app_logger (WARNING)>
# цепочка логгеров (иерархия)
# root.app_logger.utils_logger
print("utils_logger Handlers: ", utils_logger.handlers)  # []
# после добавления bacicConfig():
#   Root Handlers:  [<StreamHandler <stderr> (NOTSET)>]

# Если не указать явно, у вновь создаваемого логгера используется
# уровень его родителя (WARNING)

utils_logger.setLevel("DEBUG")
# utils_logger.propagate = False  #!!!


def main():
    utils_logger.debug("Hello")
    # Hello


if __name__ == "__main__":
    main()
