# Entrypoint for monitoring. Takes an argument, which is a config file. 
import yaml
from click import command, option

from yggamonitors.lib.site import Site


@command()
@option("--config-file", default="/opt/yggamonitors.yaml")
def main(config_file):
    with open(config_file) as f:
        config = yaml.safe_load(f)
    
    for name, site_config in config["sites"].items():
        site = Site(name=name, address=site_config["address"], port=site_config["port"])
        site.check()


if __name__ == "__main__":
    main()
