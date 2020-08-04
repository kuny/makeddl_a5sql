# coding=sjis

import yaml
import os

class Swap:

    def __init__(self):
        print("hello")

    def execute(self, src, dist):
        print("hello, hello")

    with open('config.yml', encoding='utf-8') as file:
        config = yaml.safe_load(file)
        Swap() \
        .execute()

