import logging


logger = logging.getLogger()


def main(name: str) -> None:
    # различные уровни сообщения
    # каждому стандартному уровню сообщения соответствует свой метод
    logger.debug("DEGUG")  # 10 не выводится
    logger.info("INFO")  # 20 не выводится
    logger.warning("WARNING")  # 30
    logger.error("ERROR")  # 40
    logger.critical("CRITICAL")  # 50

    # logger-ы тоже имеют уровни

    logger.debug(f"Enter in the main function: name = {name}")
    # logger с уровнем 30 - не пропускает, фильтрует сообщения с уровнем
    # debug: 10 и info:20

    print(logger.level)  # по умолчанию уровено RootLogger = 30 (warning)
    print()

    # и logger обрабатывает сообщения с уровнем не ниже своего уровня
    # т.е logger уронвя warning будет обрабатывать сообщения с уровнем
    # warning: 30, error: 40 и critical: 50

    # Изменяем уровень логгера
    # Этот метод определяет какие сообщения вообще логгер будет отправлять
    # своим обработчикам ...
    logger.setLevel("DEBUG")
    # logger.setLevel(logging.DEBUG)
    # logger.setLevel(10)
    print(logger.level)

    logger.debug(f"Enter in the main function: name = {name} попытка №2")
    # опять не получилось
    # надо изменить и уровень у обработчика
    # Одному logger-у можно повестить несколько обработчиков
    # у логеров и обработчиков свои независимые уровни!
    # Метод setLevel у обработчика будет определять какие
    # сообщения обработчик будет рассылать
    # Благодаря такой архитектуре можно сделать так, что
    # сообщения уровня Error будет уходить на почту,
    # Warning - в файл, а Debug - на консоль
    # У логгеров и обработчиков есть независимые уровни!

    print(logger.handlers)  # []
    # для несконфигурированного RootLogger-а создается обработчик класса
    # StreamHandler (запись в stderr) с уровнеь WARNING обработчик создается,
    # но не закрепляется за объектом RootLogger
    # С таким несконфигурированным логгером нельзя работать => надо настроить
    # Для настройки, логгер нам предоставляет метод logging.basicConfig(),
    # у которого может быть очень много параметров

    # NEXT...


if __name__ == "__main__":
    main("Hello")
