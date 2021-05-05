import enum


class MonitorStatuses(enum.Enum):
    HEALTHY = "healthy"
    IMPAIRED = "impaired"
    DOWN = "down"