import logging


logging.basicConfig(level="DEBUG")

logger = logging.getLogger()


def main(name: str) -> None:
    print(logger.level)  # 10
    logger.debug(f"Enter in the main function: name = {name}")
    # DEBUG:root:Enter in the main function: name = Hello

    print(logger.handlers)  # [<StreamHandler <stderr> (NOTSET)>]
    # т.е. StreamHandler будет писать вообще все сообщения, т.к. установлен
    # минимальный возможный уровень (NOTSET)


# Как работает basicConfig - он проверяет у RootLogger-а наличие
# закрепленных за ним обоаботчиков. Если обработчиков нет - то basicConfig
# создает обработчик класса StreamHandler и закрепляет его за RootLogger
# ( просто добавляет его в список logger.handlers) Дефолтный обработчик
# StreamHandler имеет уровень NOTSET, т.е. выводить все сообщения
# Но можно использовать и другой обработчик, например если в параметрах
# basicConfig указать имя файла логов

# NEXT ...

if __name__ == "__main__":
    main("Hello")
