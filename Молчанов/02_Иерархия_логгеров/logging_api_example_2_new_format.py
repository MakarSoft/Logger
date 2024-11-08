# logging_api_example_2_new_format.py

import logging

logger = logging.getLogger('My Script')
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}',
                              datefmt='%H:%M:%S', style='{')
console.setFormatter(formatter)

logger.addHandler(console)

## messages
logger.debug('Сообщение уровня debug: %s', 'SOS')
logger.info('Сообщение уровня info')
logger.warning('Сообщение уровня warning')