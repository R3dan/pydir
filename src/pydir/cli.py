import argparse
import pathlib
import sys
import os
from utils import *
import time

from __init__ import *
from tree import DirectoryTree


def main():
    parser = argparse.ArgumentParser(
        prog="Pydir", description="Creates a dictionary tree", epilog="Don't break"
    )

    parser.add_argument("--top_dir", default=os.getcwd())
    args = parser.parse_args()
    tree = DirectoryTree.generate(args.top_dir)
    debug(f"TREE = {tree}")
    for entry in tree:
        print(entry)
        time.sleep(2)