from jarbas_hive_mind import HiveMindListener
from jarbas_hive_mind.configuration import CONFIGURATION
from jarbas_utils.log import LOG
from os.path import exists, join


def start_mind(config=None, bus=None):

    config = config or CONFIGURATION

    # read configuration
    port = config["port"]
    max_connections = config.get("max_connections", -1)
    certificate_path = config["ssl"]["certificates"]
    key = join(certificate_path,
               config["ssl"]["ssl_keyfile"])
    cert = join(certificate_path,
                config["ssl"]["ssl_certfile"])

    # generate self signed keys
    if not exists(key):
        LOG.warning("ssl keys dont exist")
        HiveMindListener.generate_keys(certificate_path)

    # listen
    listener = HiveMindListener(port, max_connections, bus)
    listener.secure_listen(key, cert)


if __name__ == '__main__':
    start_mind()