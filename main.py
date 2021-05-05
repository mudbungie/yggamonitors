from typing import List
import click
from yggamonitors.lib.checks import check_site
from yggamonitors.lib.utils import get_site_from_loose_name
from yggamonitors.fixtures.sites_to_monitor import sites_to_check
from yggamonitors.lib.monitors.HttpMonitor import BasicHttpsMonitor
from yggamonitors.logger import configure_logger
import logging

logger = logging.getLogger(__name__)
#configure_logger()

def cli():
    pass

@click.command()
@click.argument("site_name", type=str, required=True)
def check(site_name: str) -> None:
    site = get_site_from_loose_name(site_name)
    check_site(site)

@click.command()
def check_all_sites():
    for site_name, address in sites_to_check.items():
        site_monitor = BasicHttpsMonitor(address=address)
        status = site_monitor.check()
        logger.error(f"{address} status: {status}")

@click.group()
@click.option("--debug", is_flag=True, default=False)
def cli(debug: bool):
    if debug:
        configure_logger(level=logging.DEBUG)
    else:
        configure_logger(level=logging.INFO)

def add_functions_to_cli():
    commands: List[click.Group] = [
        check_all_sites,
        check
    ]

    for command in commands:
        cli.add_command(command)

if __name__ == "__main__":
    add_functions_to_cli()
    cli()
    #check_all_sites()
