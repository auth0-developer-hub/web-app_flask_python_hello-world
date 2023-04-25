import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read(".config")
    return config

config = load_config()