import argparse
import json
import re
import sys
from dataclasses import dataclass
from typing import Any, Iterator, Optional, Sequence, TextIO

__version__ = "0.1.0"


def _exit(error: Exception, return_code: int, message: str) -> None:
    sys.stderr.write(message)
    sys.stderr.write("\nOriginal error: ")
    sys.stderr.write(str(error))
    sys.stderr.write("\n")
    sys.exit(return_code)


def _skip_space(s: str) -> int:
    m = re.match(r"[ \t\n\r]*", s)
    assert m is not None
    return m.end()


@dataclass
class Input:
    obj: Any
    line_no: int


def _iter_data(in_io: TextIO) -> Iterator[Input]:
    s = in_io.read()
    decoder = json.JSONDecoder()
    line_no = 1
    index = 0
    while True:
        n_spaces = _skip_space(s[index:])
        line_no += s.count("\n", index, index + n_spaces)
        index += n_spaces
        if index == len(s):
            break
        try:
            obj, end = decoder.raw_decode(s, index)
        except json.JSONDecodeError as e:
            _exit(e, 4, "Parse error: line: %d" % line_no)
        yield Input(obj, line_no)
        line_no += s.count("\n", index, end)
        index = end


def _iter_raw(in_io: TextIO) -> Iterator[Input]:
    for i, line in enumerate(in_io):
        yield Input(line.rstrip("\n\r"), i + 1)


def run(
    in_io: TextIO,
    out_io: TextIO,
    cmd: str,
    imports: Sequence[str] = (),
    sort_keys: bool = False,
    raw_input_mode: bool = False,
    raw_output: bool = False,
    join_output: bool = False,
    ascii_output: bool = True,
    indent: Optional[int] = None,
) -> None:
    environment = {}
    for mod_name in imports:
        try:
            mod = __import__(mod_name)
        except Exception as e:
            _exit(e, 5, "Cannot import module: %s" % mod_name)
        environment[mod_name] = mod

    iter_data = _iter_raw if raw_input_mode else _iter_data
    for in_data in iter_data(in_io):
        try:
            environment["j"] = in_data.obj
            out = eval(cmd, environment)
        except Exception as e:
            _exit(e, 3, "Cannot execute command: line %d" % in_data.line_no)

        if raw_output and isinstance(out, str):
            out_io.write(out)
        else:
            try:
                json.dump(
                    out,
                    out_io,
                    ensure_ascii=ascii_output,
                    sort_keys=sort_keys,
                    indent=indent,
                )
            except Exception as e:
                _exit(e, 3, "Cannot dump result: line %d" % in_data.line_no)

        if not join_output:
            out_io.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd")
    parser.add_argument(
        "--version",
        action="version",
        version="jqp %s" % __version__,
        help="show version and exit",
    )
    parser.add_argument(
        "--import", action="append", default=[], help="modules to import"
    )
    parser.add_argument(
        "--indent", type=int, default=4, help="use the given number of indent"
    )
    parser.add_argument(
        "--sort-keys",
        "-S",
        action="store_true",
        help="sort keys in objects when the command print it",
    )
    parser.add_argument(
        "--raw-input",
        "-R",
        action="store_true",
        help="pass each line text as a string instead of parsing it as JSON",
    )
    parser.add_argument(
        "--ascii-output",
        "-a",
        action="store_true",
        help="with this option, jqp ensures ASCII output",
    )
    parser.add_argument(
        "--raw-output",
        "-r",
        action="store_true",
        help="when a result is string, the command shows a raw string",
    )
    parser.add_argument(
        "--join-output", "-j", action="store_true", help="do not show newlines"
    )

    args = parser.parse_args()

    run(
        sys.stdin,
        sys.stdout,
        args.cmd,
        imports=getattr(args, "import"),
        sort_keys=args.sort_keys,
        raw_input_mode=args.raw_input,
        raw_output=args.raw_output,
        join_output=args.join_output,
        ascii_output=args.ascii_output,
        indent=args.indent,
    )
