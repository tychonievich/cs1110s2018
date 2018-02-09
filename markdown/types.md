---
title: "Everything has a type..."
...

Every expression can be evaluated to a value, and every value has a type.
The `type`{.python} built-in function and show what those types are.
For example, if you enter the Python Console you can replicate the following:

````python
>>> 2
2
>>> type(2)
<class 'int'>
>>> 2+4.5
6.5
>>> type(2+4.5)
<class 'float'>
>>> x = type("hi there")
>>> x
<class 'str'>
>>> type(x)
<class 'type'>
>>> y = print('hi!')
hi!
>>> type(y)
<class 'NoneType'>
>>> print(y)
None
>>> 2 < 3
True
>>> type(2 < 3)
<class 'bool'>
>>> False
False
>>> type(False)
<class 'bool'>
>>> print
<built-in function print>
>>> type(print)
<class 'builtin_function_or_method'>
````


The following tries to summarize the most common basic types:

| Type | Example literal values | Example expressions                                  |
|------|----------------|------------------------------------------------------|
| `int`{.python} | `3`{.python}, `-5023`{.python}, ...  | `2 + 3`{.python}, `3**4`{.python}, `abs(2 - 3)`{.python} |
| `float`{.python} | `3.0`{.python}, `-0.5023`{.python}, ...  | `2 / 3`{.python}, `1.0 + 4`{.python}, `pow(1.2, 3.4)`{.python} |
| `str`{.python} | `""`{.python}, `'candles'`{.python}, ...  | `'yes' * 3`{.python}, `'co' + 'uch'`{.python}, `input('Type something: ')`{.python} |
| `bool`{.python} | `True`{.python}, `False`{.python} (those are the only two) | `2 < 3`{.python}, `4 == 5`{.python} |
| `NoneType`{.python} | `None`{.python} (that is the only one) | `print()`{.python} or the result of any other function that does not have a `return`{.python} |
| function | (created using `def`{.python}) | `print`{.python}, `input`{.python}
