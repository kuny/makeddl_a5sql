# coding=sjis

import sys
import os
import openpyxl

class Swap:

    def __init__(self):
        print("hello")

    def execute(self, src, dist):
        print(src)
        print(dist)        


if __name__ == '__main__':
    args = sys.argv

    if len(args) == 3:
        src = args[1]
        dist = args[2]

        Swap().execute(src, dist)
