.. image:: https://img.shields.io/pypi/v/jqp.svg
   :target: https://pypi.python.org/pypi/jqp

.. image:: https://github.com/github/docs/actions/workflows/test.yml/badge.svg
   :target: https://github.com/unnonouno/jqp/actions/workflows/test.yml

.. image:: https://coveralls.io/repos/unnonouno/jqp/badge.png?branch=master
   :target: https://coveralls.io/r/unnonouno/jqp?branch=master

=====
 jqp
=====

jqp is a JSON processor with Python one-liner.


Requirement
===========

- Python 3.7, 3.8, 3.9, 3.10, 3.11


Install
=======

::

    $ pip install jqp


Usage
=====

jqp parses each line as a JSON object, and evaluates a given expression.
A parsed JSON object is bounded a variable named `j`.

::

    jqp cmd


:`cmd`: An expression to evaluate.

optional arguments:
  -h, --help  show this help message and exit
  --version   show version and exit
  --import IMPORT  modules to import
  --ascii-output, -a  with this option, jqp ensures ASCII output
  --sort-keys, -S  sort keys in objects when the command print it
  --raw-input, -R  pass each line text as a string instead of parsing it as JSON
  --raw-output, -r   when a result is string, the command shows a raw string
  --join-output, -j  do not show newlines


Example
=======

::

    % echo '{"name": "Taro", "age": 10}' | jqp '[j["name"], j["age"]]'
    [
        "Taro",
        10
    ]


License
=======

MIT License
