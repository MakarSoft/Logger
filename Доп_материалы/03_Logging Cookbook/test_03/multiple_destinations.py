# Допустим, вы хотите войти в консоль и файл с разными форматами сообщений и в разных обстоятельствах.
# Допустим, вы хотите записывать сообщения с уровнем DEBUG и выше в файл, а сообщения уровня INFO и выше — в консоль.
# Предположим также, что файл должен содержать временные метки, а консольные сообщения — нет. Вот как вы можете этого добиться.

import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename='myapp.log',
    filemode='w'
)

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

# tell the handler to use this format
console.setFormatter(formatter)

# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your application:
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')

# Как видите, сообщение DEBUG отображается только в файле. Остальные сообщения отправляются обоим адресатам.
# В этом примере используются обработчики консоли и файлов, но вы можете использовать любое количество и комбинацию обработчиков по вашему выбору.
