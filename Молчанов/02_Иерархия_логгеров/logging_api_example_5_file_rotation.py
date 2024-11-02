# logging_api_example_5_file_rotation.py

# RotatingFileHandler

import logging
import logging.handlers

logger = logging.getLogger('My Script')
logger.setLevel(logging.DEBUG)

logfile = logging.handlers.RotatingFileHandler(
    'logfile_with_rotation.log', maxBytes=10, backupCount=3)
logfile.setLevel(logging.DEBUG)
formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}',
                              datefmt='%H:%M:%S', style='{')
logfile.setFormatter(formatter)

logger.addHandler(logfile)

## messages
logger.debug('Сообщение уровня debug')
logger.info('Сообщение уровня info')
logger.warning('Сообщение уровня warning')

# Результат выполнения
#
# $ ls -1 logfile_with_rotation*
# logfile_with_rotation.log
# logfile_with_rotation.log.1
# logfile_with_rotation.log.2
# logfile_with_rotation.log.3
# logfile_with_rotation.log
#
# logfile_with_rotation.log - это самый свежий файл, затем идет logfile_with_rotation.log.1,
#                             logfile_with_rotation.log.2 и тд.