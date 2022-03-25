import enum

class Status(enum.Enum):
    OK = 0
    WARNING = 1
    CRITICAL = 2
    UNKNOWN = 3