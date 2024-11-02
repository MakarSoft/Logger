# logging_api_example_1.py

import logging

logger = logging.getLogger(__name__)

## messages
logger.debug('Сообщение уровня debug')
logger.info('Сообщение уровня info')
logger.warning('Сообщение уровня warning')