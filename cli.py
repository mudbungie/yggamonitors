#!/usr/bin/env python

from typing import List, Optional
from yggamonitors.lib.storage import initialize_tables
from yggamonitors.continuous_monitor import start_continuous_monitors
import click
from yggamonitors.lib.utils import get_all_targets, get_site_from_loose_name
from yggamonitors.fixtures.sites_to_monitor import known_sites
from yggamonitors.lib.monitors.HttpMonitor import BasicHttpsMonitor
from yggamonitors.logger import get_logger
import logging

log = get_logger(__name__)


@click.command()
@click.argument("site_name", type=str, required=True)
def check(site_name: str) -> None:
    site = get_site_from_loose_name(site_name)
    status = site.check()
    print(f"Status of {site.url}: {status}")


@click.command()
def check_all_sites():
    for site_name, address in known_sites.items():
        site = get_site_from_loose_name(address)
        status = site.check()
        print(f"Status of {site.url}: {status.value}")


@click.command()
@click.option(
    "--frequency", type=int, default=60, help="Frequency of checks in seconds"
)
def start_polling_all_sites(frequency):
    targets = get_all_targets()
    print("Continuous monitors initiated")
    start_continuous_monitors(targets=targets, frequency=frequency)
    print("Continuous monitors concluded")


@click.command()
def init_db() -> None:
    initialize_tables()


@click.group()
@click.option("--debug", is_flag=True, default=False)
def cli(debug: bool):
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)


def add_functions_to_cli():
    commands: List[click.Group] = [
        check_all_sites,
        check,
        start_polling_all_sites,
        init_db,
    ]

    for command in commands:
        cli.add_command(command)


if __name__ == "__main__":
    add_functions_to_cli()
    cli()
