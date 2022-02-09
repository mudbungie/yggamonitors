import sqlite3
from typing import Optional, Dict
from yggamonitors.fixtures.statuses import MonitorStatus
from yggamonitors.lib.monitors.Monitor_Base import Monitor
from yggamonitors.lib.target import Target
from time import time
from os import makedirs

def ensure_dir_path(path: str) -> None:
    try:
        makedirs(path)
    except FileExistsError:
        pass

def get_connection(location: Optional[str] = "/opt/yggamonitors/yggamonitors.sqlite") -> sqlite3.Connection:
    directory = "/".join(location.split("/")[:-1])
    ensure_dir_path(directory)
    return sqlite3.connect(location)

def initialize_tables() -> None:
    connection = get_connection()
    connection.execute("CREATE TABLE statuses (name TEXT, status TEXT, timestamp TEXT)")
    connection.commit()


def write_check_status(target: Target, status: MonitorStatus, timestamp=None) -> None: 
    connection = get_connection()
    if not timestamp:
        timestamp = time()
    connection.execute(f"INSERT into statuses VALUES ('{target.name}', '{str(status)}', {timestamp})")
    connection.commit()


def get_uptime_data(target, duration) -> Dict[int, str]:
    now = time()
    start_time = now - duration
    connection = get_connection()
    records = connection.execute(f"SELECT status, timestamp from statuses WHERE name = '{target}' and timestamp > {start_time} ORDER BY timestamp")

    uptime_records = []
    for record in records:
        up = record[0] == "healthy"
        timestamp = record[1]
        uptime_records.append((up, timestamp))
    return uptime_records
