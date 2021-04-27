import requests

from yggamonitors.monitors.Monitor_Base import Monitor
from yggamonitors.fixtures.monitor_statuses import MonitorStatuses

class BasicHttpMonitor(Monitor):
    def __init__(self, address: str, protocol = "https", port: int = None) -> None:
        self.address = address
        self.protocol = protocol
        if not port:
            if protocol == "http":
                self.port = 80
            elif protocol == "https":
                self.port = 443
            else:
                raise Exception("If you're gonna check a weird protocol, specify a port.")
        self.url = f"{self.protocol}://{self.address}:{self.port}"

    def check(self):
        try:
            r = requests.get(url = self.url)
        except requests.exceptions.ConnectionError:
            return MonitorStatuses.DOWN
        
        if r.status_code == 200:
            return MonitorStatuses.HEALTHY
        else:
            return MonitorStatuses.IMPAIRED

