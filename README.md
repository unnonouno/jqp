[![pypi](https://img.shields.io/pypi/v/jqp.svg)](https://pypi.python.org/pypi/jqp)
[![travis](https://img.shields.io/travis/unnonouno/jqp/master.svg)](https://travis-ci.org/unnonouno/jqp)
[![coveralls](https://img.shields.io/coveralls/unnonouno/jqp.svg)](https://coveralls.io/github/unnonouno/jqp)

# jqp

jqp is a JSON processor with Python one-liner.


## Requirement

- Python 2.7, 3.3, 3.4, 3.5

## Install

```
$ pip install jqp
```

## Usage

jqp parses each line as a JSON object, and evaluates a given expression.
A parsed JSON object is bounded a variable named `j`.


```
jqp cmd
```

- `cmd`: An expression to evaluate.

## Example

```
% echo '{"name": "Taro", "age": 10}' | jqp '[j["name"], j["age"]]'
["Taro", 10]
```

## Lisence

MIT License
