import logging.config

from settings import logger_config


logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')


words = ['new house', 'apple', 'ice cream', 3]

def main():
    for item in words:
        try:
            print(item.split(' '))
        except:
            logger.debug(f'Exception here, item = {item}', exc_info=True)
            # 2023-10-12 09:13:15,906 - DEBUG - app_logger - main:main:18- Exception here, item = 3
            # Traceback (most recent call last):
            #   File "/home/amk/_PY/#_PY_#/_Logger/_Logging_Molchanov/4_Логгирование исключений/main.py", line 16, in main
            #     print(item.split(' '))
            #           ^^^^^^^^^^
            # AttributeError: 'int' object has no attribute 'split'

            logger.exception(f'Exception here, item = {item}')
            # 2023-10-12 09:13:15,911 - ERROR - app_logger - main:main:19- Exception here, item = 3
            # Traceback (most recent call last):
            #   File "/home/amk/_PY/#_PY_#/_Logger/_Logging_Molchanov/4_Логгирование исключений/main.py", line 16, in main
            #     print(item.split(' '))
            #           ^^^^^^^^^^
            # AttributeError: 'int' object has no attribute 'split'            

            pass


if __name__ == '__main__':
    main()
