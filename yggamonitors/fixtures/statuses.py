import enum


class MonitorStatus(enum.Enum):
    HEALTHY = "healthy"
    IMPAIRED = "impaired"
    DOWN = "down"
