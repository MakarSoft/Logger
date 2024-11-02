import logging
import requests


logging.basicConfig(level="DEBUG")

logger = logging.getLogger()
print(logger)
print(f"logger_level = {logger.level}")
print(logger.handlers)
print()

# Модуль logging реализует патерн Singleton, т.е. это глобальный модуль
# для всего нашего проекта. Объекты logger-ы они глобальны и basicConfig
# создает глобальные установки для всех используемых нами модулей.
# Хоть basicConfig и создает настройки для RootLogger-а, но на самом деле
# любой logger имеет своим предком RoorLogger-а => надо настроить каждый
# logger отдельно.
# Сначала надо узнать, какие logger-ы используются в нашем проекте,
# для этого в модуле logging имеется менеджер logger-ов -
# logging.Logger.manager.loggerDict - словарь со всеми logger-ами

for key in logging.Logger.manager.loggerDict:
    print(key)
# urllib3.util.retry
# urllib3.util
# urllib3
# urllib3.connection
# urllib3.response
# urllib3.connectionpool
# urllib3.poolmanager
# charset_normalizer
# requests

# Выключаем сообщения библиотеки requests
# requests работает поверх библиотеки urllib3
# Название логгеров разделены точкой. И самым общим для них является
# логгер с название urllib3.
# Нам и нужно его получить - logging.getLogger("urllib3") и изменить
# ему уровень.
# Устанавливая уровень CRITICAL, мы фактически выключаем его.

logging.getLogger("urllib3").setLevel("CRITICAL")
# logging.getLogger(имя_логгера) - может принимать единственный
# аргумент - имя логгера. Если имя не переданно, getLogger - создает
# корневой логгер (объект класса RootLogger), если его еще нет,
# а если он есть - возвращает уже созданный объект.
# Если имя было передано getLogger создает новый объект (не корневой,
# именованный логгер), или возвращает уже существующий объект.

# Т.е. логгеры нужно настраивать!!


def main(name):
    logger.debug(f"Enter in the main() function : name = {name}")
    r = requests.get("https://www.google.com")
    print()
    print(f"Response = {r}")


if __name__ == "__main__":
    main("Hello")
