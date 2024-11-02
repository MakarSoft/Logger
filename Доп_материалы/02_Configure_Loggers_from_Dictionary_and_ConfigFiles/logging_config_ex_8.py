# Example 8
# logging_config_ex_8.py

import logging
from logging import config



config.fileConfig("file_config1.conf")

def addition(a, b):
    logging.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logging.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logging.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    try:
        result = float(a) + float(b)
        logging.info("Addition Function Completed Successfully")
        return result
    except Exception as e:
        logging.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
        return None


if __name__ == "__main__":
    #logging.info("Current Log Level : {}\n".format(logging.getLevel()))

    result = addition(10,20)
    logging.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logging.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition("A",20)
    logging.info("Addition of {} & {} is : {}".format("A",20, result))