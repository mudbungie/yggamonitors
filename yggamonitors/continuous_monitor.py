from typing import List
from time import time, sleep
from yggamonitors.lib.target import Target
from yggamonitors.lib.storage import write_check_status


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
