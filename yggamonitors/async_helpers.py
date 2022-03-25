import asyncio
from pydoc import resolve
from typing import List
from yggamonitors.sites import Site
from yggamonitors.status import Status

async def async_check_sites(sites = List[Site]) -> List[Status]:
    tasks = []
    for site in sites:
        print(f"Creating task for {site}")
        tasks.append(asyncio.create_task(site.check_tcp_async()))
    results = []
    for task in tasks:
        # results.append(await task)
        results.append(asyncio.run(task))
        # results.append(task)
    return results


def check_sites(sites = List[Site]) -> List[Status]:
    results = asyncio.run(async_check_sites(sites=sites))
    return results