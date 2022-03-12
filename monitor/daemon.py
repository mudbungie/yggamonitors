# Entrypoint for monitoring. Takes an argument, which is a config file. 
import yaml
import socket
from click import command, option

class Site():
    def __init__(self, name: str, address: str, port: int=443):
        self.name = name
        self.address = address
        self.port = port


#TODO paralellize this
def is_site_accessible(site) -> bool:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((site.address, site.port))
        client.send(b"SYN")
        print(f"Connection successful for {site.name}")
        return True
    except ConnectionRefusedError:
        print(f"Connection refused for {site.name}")
        return False
    except OSError:
        print(f"No route to {site.name}")


@command()
@option("--config-file", default="/opt/yggamonitors.yaml")
def main(config_file):
    with open(config_file) as f:
        config = yaml.safe_load(f)
    
    for name, site_config in config["sites"].items():
        site = Site(name=name, address=site_config["address"], port=site_config["port"])
        is_site_accessible(site)



if __name__ == "__main__":
    main()
