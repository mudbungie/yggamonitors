import logging
import json
import arrow
import sys

from logging import getLogger

MODULE_NAME = "yggamonitors"


class LocalFormatter(logging.Formatter):
    def __init__(self) -> None:
        super().__init__()
        ### Throw any global config items in here as arguments to init

    def format(self, record: logging.LogRecord) -> str:
        now = arrow.utcnow().isoformat()
        structured_log = {
            "levelname": record.levelname,
            "timestamp": now,
            "message": record.getMessage(),
        }
        return json.dumps(structured_log)


def configure_logger(
    level: int = logging.DEBUG,
) -> None:
    module_logger = logging.getLogger(MODULE_NAME)
    module_logger.setLevel(level)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(fmt=LocalFormatter())
    module_logger.addHandler(handler)
