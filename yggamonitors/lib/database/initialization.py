from os import makedirs
from typing import Optional
import sqlite3


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
