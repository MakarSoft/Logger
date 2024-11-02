# https://realpython.com/python-logging/

# Вы можете настроить ведение журнала, используя функции модуля и класса или создав файл конфигурации или словарь
# и загрузив его с помощью fileConfig() или dictConfig() соответственно.
# Это полезно, если вы хотите изменить конфигурацию ведения журнала в работающем приложении.
#
# Вот пример конфигурации файла:
#
# [loggers]
# keys=root,sampleLogger
#
# [handlers]
# keys=consoleHandler
#
# [formatters]
# keys=sampleFormatter
#
# [logger_root]
# level=DEBUG
# handlers=consoleHandler
#
# [logger_sampleLogger]
# level=DEBUG
# handlers=consoleHandler
# qualname=sampleLogger
# propagate=0
#
# [handler_consoleHandler]
# class=StreamHandler
# level=DEBUG
# formatter=sampleFormatter
# args=(sys.stdout,)
#
# [formatter_sampleFormatter]
# format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
#
# В приведенном выше файле есть два регистратора, один обработчик и один форматтер.
# После того, как их имена определены, они настраиваются путем добавления слов logger, handler и formatter перед их именами, разделенными символом подчеркивания.
#
# Чтобы загрузить этот файл конфигурации, вы должны использовать fileConfig():
# Путь к конфигурационному файлу передается методу fileConfig()  в качестве параметра, и параметр disable_existing_loggers используется для сохранения или
# отключения регистраторов, присутствующих при вызове функции. По умолчанию используется, True если не указано.

import logging
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')