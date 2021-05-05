import click
from yggamonitors.lib.checks import check_site
from yggamonitors.lib.utils import site_from_loose_name
from yggamonitors.fixtures.sites_to_monitor import sites
from yggamonitors.lib.monitors.HttpMonitor import BasicHttpMonitor
from yggamonitors.logger import configure_logger
import logging

logger = logging.getLogger(__name__)
configure_logger()


@click.command()
def test(site_name: str) -> None:
    site = site_from_loose_name(site_name)
    check_site(site)


def check_all_sites():
    for site in sites:
        site_monitor = BasicHttpMonitor(site)
        status = site_monitor.check()
        logger.error(f"{site} status: {status}")


if __name__ == "__main__":
    main()
