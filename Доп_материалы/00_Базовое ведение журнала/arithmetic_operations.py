# Example 6
# arithmetic_operations.py

import logging
from typing import Any, Optional

def addition(a: Any, b: Any) -> Optional[float]:
    
    logging.debug("Inside Addition Function")
    
    if isinstance(a, str) and a.isdigit():
        logging.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logging.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    result = None
    try:
        result = float(a) + float(b)
        logging.info("Addition Function Completed Successfully")
    except Exception as e:
        logging.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
    finally:
        return result
