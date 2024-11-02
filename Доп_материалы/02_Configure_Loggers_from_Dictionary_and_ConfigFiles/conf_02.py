# https://realpython.com/python-logging/
import logging
import logging.config
import yaml

# Вот конфигурация в формате YAML для словарного подхода:

# version: 1
# formatters:
#   simple:
#     format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# handlers:
#   console:
#     class: logging.StreamHandler
#     level: DEBUG
#     formatter: simple
#     stream: ext://sys.stdout
# loggers:
#   sampleLogger:
#     level: DEBUG
#     handlers: [console]
#     propagate: no
# root:
#   level: DEBUG
#   handlers: [console]

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')