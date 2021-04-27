from yggamonitors.monitors.HttpMonitor import BasicHttpMonitor
from yggamonitors.fixtures.monitor_statuses import MonitorStatuses

def test_connection_to_arbitrary_site() -> None:
    arbitrary_site = "iscaliforniaonfire.com"
    monitor = BasicHttpMonitor(address=arbitrary_site, protocol="http")
    result = monitor.check()
    assert result == MonitorStatuses.HEALTHY

