import glob
import logging
import logging.handlers
import os
import zlib

LOG_FILENAME = 'logging_rotatingfile_example.out'

# https://pythobyte.com/python-zlib-library-tutorial-d183dd9d/
# https://docs-python.ru/standart-library/modul-zlib-python/
def namer(name):
    return name + ".gz"

def rotator(source, dest):
    with open(source, "rb") as sf:
        data = sf.read()
        compressed = zlib.compress(data, 9)
        with open(dest, "wb") as df:
            df.write(compressed)

        # compressed_data = open(dest, 'rb').read()
        # decompressed_data = zlib.decompress(compressed_data)
        # print(decompressed_data)
        # print('-'*20)
    os.remove(source)

# Настраиваем регистратор с желаемым уровнем.
# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
rh = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=100, backupCount=10
)


rh.rotator = rotator
rh.namer = namer

my_logger.addHandler(rh)

# Log some messages
for i in range(1000):
    my_logger.debug('i = %d' % i)

# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
    print(filename)