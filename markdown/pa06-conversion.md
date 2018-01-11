---
title: "PA 06: conversion.py"
...

# Task

Write a file with two functions: `c2f` and `f2c`.
`f2c` should accept as a parameter a temperature in Fahrenheit and return the corresponding temperature in Celsius.
`c2f` should accept as a parameter a temperature in Celsius and return the corresponding temperature in Fahrenheit.

Neither function should `print`{.python} anything nor ask for any `input`{.python}.
You should not have any code outside of these two functions.

# Example Invocations

When you run `conversion.py`, nothing should happen.
It defines functions, it does not run them.

If in another file (which you do not submit) you write the following:

````python
import conversion

print(conversion.c2f(31))
print(conversion.c2f(100))
print(conversion.f2c(-40))
print(conversion.f2c(72))
````

you should get the following output:

````
87.8
212.0
-40.0
22.22222222222222
````

Don't worry if you are off in the last few decimal places

# Troubleshooting

It does not matter in what order you write `c2f` and `f2c`, nor which appears first inside your file.

## IndentationError: expected an indented block

You can't have a function without a body; the following code:

````python
def a():
    # nothing here but comments
    # (nothing at all would give the same error)


def b():
    return -2
````

will producing the error message `IndentationError: expected an indented block` on the line for `def b():`{.python}.
This is because

-   every `def`{.python} must be followed by a `:`.
-   every `:` must be followed by a line of code that is indented more than the line of code before it.
-   blank lines and lines that contain only comments are not lines of code.

Thus Python reads `def a():`{.python}, then reads forward (skipping blank lines and comments) until it finds `def b():`{.python}, and gets upset because it wanted an indented line first.

If you want to have an empty function, put a docstring in it instead of a comment:

````python
def a():
    '''docstrings are python code, so this line counts as an indented line'''


def b():
    return -2
````


## SyntaxError: invalid syntax

Typically, this means you left something out or included something you shouldn't, and Python is decent, but not perfect, at pointing out where this happened; for example

````python
def a()
    return 0
````

will point to the spot where a `:` is missing, but something like

````python
def a(b:
    return 0
````

will not know which line is missing the `)`.
If you don't see what's wrong where it points, look earlier in the file and see if something is wrong up there.
