# Регистраторы — это простые объекты Python.
# Метод addHandler() не имеет минимальной или максимальной квоты на количество добавляемых обработчиков.
# Иногда для приложения будет полезно регистрировать все сообщения всех серьезностей в текстовом файле,
# одновременно регистрируя ошибки или выше на консоли. Чтобы настроить это, просто настройте соответствующие обработчики.
# Логирование вызовов в коде приложения останется без изменений.

# Обратите внимание, что код «приложения» не заботится о нескольких обработчиках.
# Все, что изменилось, это добавление и настройка нового обработчика с именем fh.
# Возможность создавать новые обработчики с более или менее серьезными фильтрами может оказаться очень полезной при написании
# и тестировании приложения.
# Вместо того, чтобы использовать множество операторов печати для отладки, используйте logger.debug: в отличие от операторов печати,
# которые вам придется удалить или закомментировать позже, операторы logger.debug могут оставаться нетронутыми в
# исходный код и оставаться бездействующим до тех пор, пока они вам снова не понадобятся.
# Единственное изменение, которое должно произойти, — это изменить уровень серьезности регистратора и/или обработчика для отладки.

import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')