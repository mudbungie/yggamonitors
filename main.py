from typing import List
import click
from yggamonitors.lib.utils import get_site_from_loose_name
from yggamonitors.fixtures.sites_to_monitor import known_sites
from yggamonitors.lib.monitors.HttpMonitor import BasicHttpsMonitor
from yggamonitors.logger import get_logger
import logging

logger = get_logger(__name__)


@click.command()
@click.argument("site_name", type=str, required=True)
def check(site_name: str) -> None:
    site = get_site_from_loose_name(site_name)
    status = site.check()
    print(f"Status of {site.url}: {status}")


@click.command()
def check_all_sites():
    for site_name, address in known_sites.items():
        site_monitor = BasicHttpsMonitor(address=address)
        status = site_monitor.check()
        logger.error(f"{address} status: {status}")


@click.group()
@click.option("--debug", is_flag=True, default=False)
def cli(debug: bool):
    if debug:
        logger.setLevel(logging.DEBUG)


def add_functions_to_cli():
    commands: List[click.Group] = [check_all_sites, check]

    for command in commands:
        cli.add_command(command)


if __name__ == "__main__":
    add_functions_to_cli()
    cli()
