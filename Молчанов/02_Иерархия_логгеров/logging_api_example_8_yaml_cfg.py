# logging_api_example_8_yaml_cfg.py

# Конфигурация logging из словаря

# https://docs-python.ru/packages/modul-pyyaml-python/zagruzka-chtenie-dokumenta-yaml/
# https://pythonist.ru/kak-chitat-fajly-yaml-v-python/

import logging
import logging.config
import yaml
from yaml.loader import SafeLoader

# create logger
logger = logging.getLogger('superscript')

#read config
with open('02_Иерархия_логгеров/log_config.yml') as f:
    log_config = yaml.load(f, Loader=SafeLoader)

logging.config.dictConfig(log_config)

## messages
logger.debug('Сообщение уровня debug %s', 'SOS')
logger.info('Сообщение уровня info')
logger.warning('Сообщение уровня warning')
