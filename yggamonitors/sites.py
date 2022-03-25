import socket
import time

class Site:
    def __init__(self, address: str, port: int, name: str = None):
        self.address = address
        self.port = port
        self.name = name if name else f"{address}:{port}"

    def __str__(self):
        return f"<Site: {self.name} ({self.address}:{self.port})>"

    def check_tcp(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(3)
        print(f"Attempting connection for {self.name} at {time.time()}")
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
            return False

    async def check_tcp_async(self):
        return self.check_tcp()