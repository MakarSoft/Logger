# Другой способ добавления определенных пользователем атрибутов — использование кастомного Filter.
# Фильтры предоставляют дополнительную логику для определения того, какие журнальные сообщения выводить.
# Это шаг после проверки базового уровня журналирования, но до передачи журнального сообщения обработчикам.
# В дополнение к определению, должно ли журнальное сообщение двигаться дальше, мы также можем вставить новые атрибуты в методе filter().
# В этом примере мы добавляем новый атрибут color (прим. пер.: цвет) в методе filter(), значение которого определяется
# на основе имени уровня в журнальном сообщении. В этом случае имя атрибута снова должно быть добавлено в форматировщик.

import logging

class CustomFilter(logging.Filter):

    COLOR = {
        "DEBUG": "GREEN",
        "INFO": "GREEN",
        "WARNING": "YELLOW",
        "ERROR": "RED",
        "CRITICAL": "RED",
    }

    def filter(self, record):
        record.color = CustomFilter.COLOR[record.levelname]
        return True

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - [%(color)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)
logger.addFilter(CustomFilter())

logger.debug("сообщение для отладки, цвет — зеленый")
logger.info("информационное сообщение, цвет — зеленый")
logger.warning("предупреждающее сообщение, цвет — желтый")
logger.error("сообщение об ошибке, цвет — красный")
logger.critical("сообщение о критической ошибке, цвет — красный")