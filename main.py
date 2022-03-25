from yggamonitors.config import get_config
from yggamonitors.sites import Site
from yggamonitors.async_helpers import check_sites

def main():
    config = get_config()
    sites = []
    for site_def in config["sites"]:
        site = Site(address=site_def["address"], port=site_def["port"], name=site_def["name"])
        sites.append(site)

    check_sites(sites)

if __name__ == "__main__":
    main()