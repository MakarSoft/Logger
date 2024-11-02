# Новый атрибут с динамическим значением

# В других ситуациях вам, возможно, понадобятся динамические атрибуты, например что-то вроде динамического идентификатора.
# В таком случае вы можете расширить базовый класс LoggerAdapter и создать свой собственный.
# Метод process() — то место, где дополнительные атрибуты добавляются к журнальному сообщению.
# В коде ниже я добавляю динамический атрибут id, который может быть разным в каждом журнальном сообщении.
# В этом случае вам не нужно добавлять атрибут в форматировщик.

import logging

class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        my_context = kwargs.pop('id', self.extra['id'])
        return '[%s] %s' % (my_context, msg), kwargs

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)
logger = CustomAdapter(logger, {"id": None})

logger.info('ID предоставлен', id='1234')
logger.info('ID предоставлен', id='5678')
logger.info('Отсутствует информация об ID')