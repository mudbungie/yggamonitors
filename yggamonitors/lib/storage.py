import sqlite3
from typing import Optional
from yggamonitors.fixtures.statuses import MonitorStatuses
from yggamonitors.lib.target import Target
from time import time
from os import makedirs

def ensure_dir_path(path: str) -> None:
    makedirs(path)

def get_connection(location: Optional[str] = "/opt/yggamonitors/yggamonitors.sqlite") -> sqlite3.Connection:
    directory = "/".join(location.split("/")[:-1])
    ensure_dir_path(directory)
    return sqlite3.connect(location)

def initialize_tables() -> None:
    connection = get_connection()
    connection.execute("CREATE TABLE statuses (name TEXT, status TEXT, timestamp TEXT)")
    connection.commit()


def write_check_status(target: Target, status: str, timestamp=None) -> None: 
    connection = get_connection()
    if not timestamp:
        timestamp = time()
    connection.execute(f"INSERT into statuses VALUES ('{target.name}', '{str(status)}', {timestamp})")
    connection.commit()
