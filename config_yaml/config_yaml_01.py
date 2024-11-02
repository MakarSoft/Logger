import logging
import logging.config
import yaml

import os

print(os.getcwd())

# Загрузка конфигурации логирования из файла YAML
with open("config_yaml/config_01.yaml", "r") as file:
    config = yaml.safe_load(file)
    logging.config.dictConfig(config)

# Получение логгера
logger = logging.getLogger("my_logger")

# Примеры логирования
logger.debug("Это отладочное сообщение")
logger.info("Это информационное сообщение")
logger.warning("Это предупреждающее сообщение")
logger.error("Это сообщение об ошибке")
logger.critical("Это критическое сообщение")
