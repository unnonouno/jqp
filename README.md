# jqp

jqp is a JSON processor with Python one-liner.


## Requirement

- Python 2.7

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
