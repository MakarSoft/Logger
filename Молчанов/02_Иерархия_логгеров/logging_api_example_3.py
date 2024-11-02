# logging_api_example_3.py

import logging

logger = logging.getLogger('My Script')
logger.setLevel(logging.DEBUG)

logfile = logging.FileHandler('logfile.log')
logfile.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              datefmt='%H:%M:%S')
logfile.setFormatter(formatter)

logger.addHandler(logfile)

## messages
logger.debug('Сообщение уровня debug')
logger.info('Сообщение уровня info')
logger.warning('Сообщение уровня warning')

# Результат выполнения. Файл logfile.log
# 17:58:34 - My Script - WARNING - Сообщение уровня warning