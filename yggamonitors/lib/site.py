from os import stat
import socket
import time
import asyncio
from typing import Tuple

from yggamonitors.lib.database.interface import query_site_latest_status, record_site_status

class Site():
    def __init__(self, name: str, address: str, port: int=442):
        self.name = name
        self.address = address
        self.port = port


    #TODO paralellize this
    def is_tcp_accessible(self) -> bool:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((self.address, self.port))
            client.send(b"SYN")
            print(f"Connection successful for {self.name}")
            return True
        except ConnectionRefusedError:
            print(f"Connection refused for {self.name}")
            return False
        except OSError:
            print(f"No route to {self.name}")

    def check(self) -> bool:
        now = time.time()
        status = self.is_tcp_accessible()
        asyncio.run(self.record_status(status=status, timestamp=now))
        return status


    async def record_status(self, status: bool, timestamp: int) -> None:
        record_site_status(site_name=self.name, status=status, timestamp=timestamp)
        print(f"Finished logging event for {self.name}")

    def latest_status(self) -> Tuple[bool, int]:
        status = query_site_latest_status(site_name=self.name)
