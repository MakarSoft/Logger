# Example 12
# logging_config_ex_12.py

import logging
from logging import config


config.fileConfig("file_config3.conf")

################ Logger #################
logger1 = logging.getLogger("root")
logger2 = logging.getLogger("main")

def addition(a, b):
    logger1.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logger1.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logger1.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    try:
        result = float(a) + float(b)
        logger1.info("Addition Function Completed Successfully")
        return result
    except Exception as e:
        logger1.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
        return None


if __name__ == "__main__":
    logger2.info("Current Log Level : {}\n".format(logger2.getEffectiveLevel()))


    result = addition(10,20)
    logger2.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logger2.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition("A",20)
    logger2.info("Addition of {} & {} is : {}".format("A",20, result))
