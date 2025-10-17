#! /usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
# ]
# ///
import argparse
from pathlib import Path as path

def main(args):
    print(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", help="Input File")
    parser.add_argument("-o", help="Output File")
    args = parser.parse_args()

    args_n = {}
    if args.i:
        args_n.update({"in": (path.cwd()/args.i).resolve()})

    if args.o:
        args_n.update({"out": (path.cwd()/args.o).resolve()})
    else:
        args_n.update({"out": (path.cwd()/"./results").resolve()})
        
    main(args_n)
