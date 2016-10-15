.. image:: https://img.shields.io/pypi/v/jqp.svg
   :target: https://pypi.python.org/pypi/jqp

.. image:: https://travis-ci.org/unnonouno/jqp.svg?branch=master
   :target: https://travis-ci.org/unnonouno/jqp

.. image:: https://coveralls.io/repos/unnonouno/jqp/badge.png?branch=master
   :target: https://coveralls.io/r/unnonouno/jqp?branch=master

=====
 jqp
=====

jqp is a JSON processor with Python one-liner.


Requirement
===========

- Python 2.7, 3.3, 3.4, 3.5


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


Example
=======

::

    % echo '{"name": "Taro", "age": 10}' | jqp '[j["name"], j["age"]]'
    ["Taro", 10]


Lisence
=======

MIT License
