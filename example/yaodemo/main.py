# -*- coding:utf-8 -*-

import sys

from aioquant import quant

def initialize():
    from strategy.strategy import MyStrategy
    MyStrategy()


if __name__ == "__main__":
    config_file = "config.json"
    quant.start(config_file, initialize)
