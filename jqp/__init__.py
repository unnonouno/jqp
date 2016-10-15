import argparse
import json
import sys


__version__ = '0.0.0'


def run(in_io, out_io, cmd):
    for line in in_io:
        if line.strip() == '':
            continue
        js = json.loads(line)
        out = eval(cmd, {'j': js})
        json.dump(out, out_io)
        out_io.write('\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd')
    args = parser.parse_args()

    run(sys.stdin, sys.stdout, args.cmd)
