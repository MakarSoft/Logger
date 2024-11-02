# logging_config.ini
# [loggers]
# keys=root

# [handlers]
# keys=stream_handler

# [formatters]
# keys=formatter

# [logger_root]
# level=DEBUG
# handlers=stream_handler

# [handler_stream_handler]
# class=StreamHandler
# level=DEBUG
# formatter=formatter
# args=(sys.stderr,)

# [formatter_formatter]
# format=%(asctime)s %(name)-12s %(levelname)-8s %(message)s

import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')
logger = logging.getLogger()
logger.debug('hello world')