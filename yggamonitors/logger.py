import logging
import json
import arrow
import sys

from logging import getLogger

MODULE_NAME = "yggamonitors"


class LocalFormatter(logging.Formatter):
    def __init__(self, source) -> None:
        super().__init__()
        ### Throw any global config items in here as arguments to init
        self.source = source

    def format(self, record: logging.LogRecord) -> str:
        now = arrow.utcnow().isoformat()
        structured_log = {
            "levelname": record.levelname,
            "source": self.source,
            "timestamp": now,
            "message": record.getMessage(),
        }
        return json.dumps(structured_log)


def get_logger(source, level=logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(f"{MODULE_NAME}-{__name__}")
    logger.setLevel(level)

    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = LocalFormatter(source=source)
    handler.setFormatter(fmt=formatter)
    logger.addHandler(handler)

    return logger
