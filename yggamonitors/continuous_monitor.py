from typing import List, Dict
from time import time, sleep
from yggamonitors.lib.target import Target
from yggamonitors.fixtures.statuses import MonitorStatus
from yggamonitors.lib.storage import write_check_status
import asyncio


def start_continuous_monitors(targets: List[Target], frequency) -> None:
    start_time = 0
    while True:
        new_time = time()
        if new_time - start_time > frequency:
            start_time = new_time
            for target in targets:
                status = target.check()
                write_check_status(target, status)
                print(target.name, status)
        else:
            sleep(0.5)



def parallel_continuous_checks(targets: List[Target], frequency) -> None:
    start_time = 0
    while True:
        new_time = time()
        if new_time - start_time > frequency:
            start_time = new_time
            results = asyncio.run(parallel_checks(targets))
            for target, status in results.items():
                write_check_status(target, status)

    

async def parallel_checks(targets: List[Target]) -> Dict[Target, MonitorStatus]:
    results = {}
    for target in targets:
        results[target] = await target.async_check()

    return results

        