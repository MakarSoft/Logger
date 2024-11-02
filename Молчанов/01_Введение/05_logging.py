import logging
import requests

logging.basicConfig(level="DEBUG")

logger = logging.getLogger()
print(logger)
# <RootLogger root (DEBUG)>

print(f"logger_level = {logger.level}")
# logger_level = 10

print(logger.handlers)
# [<StreamHandler <stderr> (NOTSET)>]

print()


def main(name):
    logger.debug(f"Enter in the main() function : name = {name}")
    r = requests.get("https://www.google.com")
    # DEBUG:root:Enter in the main() function : name = Hello
    # DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.google.com:443
    # DEBUG:urllib3.connectionpool:https://www.google.com:443 "GET / HTTP/1.1" 200 None

    print()
    print(f"Response = {r}")
    # <Response [200]>


if __name__ == "__main__":
    main("Hello")
