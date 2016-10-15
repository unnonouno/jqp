import argparse
import json
import sys


__version__ = '0.0.0'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd')
    args = parser.parse_args()

    for line in sys.stdin:
        if line.strip() == '':
            continue
        js = json.loads(line)
        out = eval(args.cmd, {'j': js})
        json.dump(out, sys.stdout)
        sys.stdout.write('\n')
