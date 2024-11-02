# Example 11
# logging_config_ex_11.py

import logging
from logging import config

config.fileConfig("file_config2.conf")

################ Module Logger #################
logger = logging.getLogger("arithmetic_ops")

class Addition:
    def __init__(self):
        ################ Class Logger #################
        self.logger = logging.getLogger("arithmetic_ops.Addition")

    def add(self, a,b):
        self.logger.debug("Inside Addition Function")
        if isinstance(a, str) and a.isdigit():
            self.logger.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

        if isinstance(b, str) and b.isdigit():
            self.logger.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

        try:
            result = float(a) + float(b)
            self.logger.info("Addition Function Completed Successfully")
            return result
        except Exception as e:
            self.logger.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
            return None


if __name__ == "__main__":
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))

    addition = Addition()
    result = addition.add(10,20)
    logger.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition.add("20",20)
    logger.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition.add("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))

    