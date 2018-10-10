import os

import yaml


def parse(dir, name):
    with open(os.path.join(dir, name), 'r') as stream:
        config = yaml.load(stream)

    return config['token'], config['backend'], config['filename']
