from io import StringIO

import jqp
import pytest


def test1() -> None:
    inputs = StringIO(
        """{"name": "Taro", "age": 10}
"""
    )
    outputs = StringIO()
    jqp.run(inputs, outputs, 'j["name"]')
    assert outputs.getvalue() == '"Taro"\n'


def test_import() -> None:
    inputs = StringIO(
        """{"name": "Taro", "age": 10}
"""
    )
    outputs = StringIO()
    jqp.run(inputs, outputs, 're.sub("a", "A", j["name"])', imports=["re"])
    assert outputs.getvalue() == '"TAro"\n'


def test_sort_keys() -> None:
    # This command ignores input
    inputs = StringIO(
        """1
"""
    )
    outputs = StringIO()
    jqp.run(inputs, outputs, '{"a": 0, "b": 0, "c": 0}', sort_keys=True)
    assert outputs.getvalue() == '{"a": 0, "b": 0, "c": 0}\n'


def test_raw_input() -> None:
    inputs = StringIO(" a \n")
    outputs = StringIO()
    jqp.run(inputs, outputs, "j", raw_input_mode=True)
    assert outputs.getvalue() == '" a "\n'


def test_raw_output() -> None:
    # This command ignores input
    inputs = StringIO(
        """1
"""
    )
    outputs = StringIO()
    jqp.run(inputs, outputs, '"a"', raw_output=True)
    assert outputs.getvalue() == "a\n"


def test_join_output() -> None:
    inputs = StringIO(
        """1
2"""
    )
    outputs = StringIO()
    jqp.run(inputs, outputs, "j", join_output=True)
    assert outputs.getvalue() == "12"


def test_ascii() -> None:
    # This command ignores input
    inputs = StringIO(
        """1
"""
    )
    outputs = StringIO()
    # This is a Japanese character
    jqp.run(inputs, outputs, '"\u3042"', ascii_output=True)
    assert outputs.getvalue() == '"\\u3042"\n'


def test_indent() -> None:
    inputs = StringIO(
        """[1]
"""
    )
    outputs = StringIO()
    jqp.run(inputs, outputs, "j", indent=4)
    assert outputs.getvalue() == "[\n    1\n]\n"


def test_parse_error() -> None:
    inputs = StringIO("invalid\n")
    outputs = StringIO()
    with pytest.raises(SystemExit) as e:
        jqp.run(inputs, outputs, "j")
    assert e.value.code == 4


def test_execution_error() -> None:
    inputs = StringIO("1\n")
    outputs = StringIO()
    with pytest.raises(SystemExit) as e:
        jqp.run(inputs, outputs, "invalid")
    assert e.value.code == 3


def test_dump_error() -> None:
    inputs = StringIO("1\n")
    outputs = StringIO()
    with pytest.raises(SystemExit) as e:
        jqp.run(inputs, outputs, "lambda: 0")
    assert e.value.code == 3


def test_import_error() -> None:
    inputs = StringIO("1\n")
    outputs = StringIO()
    with pytest.raises(SystemExit) as e:
        jqp.run(inputs, outputs, "j", imports=["unknown_module"])
    assert e.value.code == 5
