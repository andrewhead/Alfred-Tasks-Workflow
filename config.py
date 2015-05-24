#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import logging
import json
import argparse

logging.basicConfig(level=logging.INFO, format="%(message)s")
CONFIG_FILE = 'config.json'


def set_option(name, value):
    with open(CONFIG_FILE, 'r') as cfg_file:
        cfg = json.load(cfg_file)
    cfg[name] = value
    with open(CONFIG_FILE, 'w') as cfg_file:
        json.dump(cfg, cfg_file, indent=2)


def get_option(name):
    with open(CONFIG_FILE) as cfg_file:
        cfg = json.load(cfg_file)
    try:
        return cfg[name]
    except KeyError:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Configure plugin")
    parser.add_argument("name", help="name of option")
    parser.add_argument("--value", help="value of option")
    args = parser.parse_args()

    if args.value is not None:
        set_option(args.name, args.value)
    else:
        print get_option(args.name)
