import argparse
import json
import sys


__version__ = '0.0.0.1'


def _exit(error, return_code, message):
    sys.stderr.write(message)
    sys.stderr.write('\nOiginal error: ')
    sys.stderr.write(str(error))
    sys.stderr.write('\n')
    sys.exit(return_code)


def run(in_io, out_io, cmd, imports=[], sort_keys=False):
    environment = {}
    for mod_name in imports:
        try:
            mod = __import__(mod_name)
        except Exception as e:
            _exit(e, 5, 'Cannot import module: %s' % mod_name)
        environment[mod_name] = mod

    for i, line in enumerate(in_io):
        if line.strip() == '':
            continue

        line_no = i + 1
        try:
            js = json.loads(line)
        except Exception as e:
            _exit(e, 4, 'Parse error: line %d' % line_no)

        try:
            environment['j'] = js
            out = eval(cmd, environment)
        except Exception as e:
            _exit(e, 3, 'Cannot execute command: line %d' % line_no)

        try:
            json.dump(out, out_io, sort_keys=sort_keys)
        except Exception as e:
            _exit(e, 3, 'Cannot dump result: line %d' % line_no)

        out_io.write('\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd')
    parser.add_argument(
        '--version', action='version', version='jqp %s' % __version__,
        help='show version and exit')
    parser.add_argument(
        '--import', action='append', default=[],
        help='modules to import')
    parser.add_argument(
        '--sort-keys', '-S', action='store_true',
        help='sort keys in objects when the command print it')

    args = parser.parse_args()

    run(sys.stdin, sys.stdout, args.cmd, imports=getattr(args, 'import'),
        sort_keys=args.sort_keys)
