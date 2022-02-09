import matplotlib.pyplot as plt
from yggamonitors.lib.storage import get_uptime_data


def graph_one_day_uptime_for_router() -> None:
    graph_uptime("https://192.168.1.1", 86400)


def graph_uptime(site, duration) -> None:
    records = get_uptime_data(site, duration)

    up_value = [1 if record[0] else 0 for record in records]
    timestamps = [record[1] for record in records]
    plt.plot(timestamps, up_value)
    plt.ylabel("Online")
    plt.xlabel("Time")
    plt.xscale("linear")
    plt.show()