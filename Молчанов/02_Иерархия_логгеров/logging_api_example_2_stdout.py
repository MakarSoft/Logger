# logging_api_example_2_stdout.py
# Вывод на стандартный поток вывода
import sys
import logging

logger = logging.getLogger('My Script')
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              datefmt='%H:%M:%S')
console.setFormatter(formatter)

logger.addHandler(console)

## messages
logger.debug('Сообщение уровня debug %s', 'SOS')
logger.info('Сообщение уровня info')
logger.warning('Сообщение уровня warning')