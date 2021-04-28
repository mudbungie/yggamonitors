from yggamonitors.fixtures.sites_to_monitor import sites
from yggamonitors.lib.monitors.HttpMonitor import BasicHttpMonitor
from yggamonitors.logger import configure_logger
import logging

configure_logger()
logger = logging.getLogger(__name__)


def check_all_sites():
    for site in sites:
        site_monitor = BasicHttpMonitor
        status = site_monitor.check()
        logger.info(f"{site} status: {status}")


if __name__ == "__main__":
    check_all_sites()
