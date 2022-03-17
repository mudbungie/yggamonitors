import sqlite3

from yggamonitors.lib.database.initialization import get_connection


class NoRecordsException(Exception):
    pass


def record_site_status(site_name: str, timestamp: int, status: bool) -> None:
    connection = get_connection()
    connection.execute(f"INSERT into statuses VALUES ('{site_name}', '{status}', {timestamp})")
    connection.commit()

def query_site_latest_status(site_name: str):
    connection = get_connection()
    records = connection.execute(f"SELECT status, timestamp from statuses WHERE name = '{site_name}' ORDER BY timestamp LIMIT 1")
    try:
        record = records[0]
    except IndexError:
        raise NoRecordsException(f"No records found for site {site_name}")
    return record["status"]
