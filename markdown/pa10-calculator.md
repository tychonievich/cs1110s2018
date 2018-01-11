---
title: "PA 10: calculator.py"
...

# Task

Write a file named `calculator.py` that has a function `binop` which can evaluate strings representing simple mathematical expressions.

`binop` accepts a single string parameter consisting of two positive integers and a singe operator between them, where the operator is one of `+`, `-`, `*`, or `/`.
There may also be arbitrarily many spaces before or after either number and/or the operator.
The function returns the `int` or `float` value created by evaluating the expression.

Python has several built-in ways to do this (`eval`, `exec`, `compile`); **do not** use them.  `calculator.py` also should not `import` anything.

# Example Invocations

When you run `calculator.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import calculator

print(calculator.binop("111 * 10"))
print(calculator.binop("    11+11     "))
print(calculator.binop("12345/678"))
print(calculator.binop("   965   -      123"))
````



you should get the following output:

````
1110
22
18.207964601769913
842
````


# Thought Questions

How hard would it be to

-   Return the number if all there is is one number?
-   Deal with negative numbers too, like `"-123 - -456"`
-   Deal with a string with two operators, like `"1 + 23 * 456"`?


# Troubleshooting

There are four operators that could be `in` the string, so you probably want four cases in a big `if`-`elif`-type statement.

Those string methods you learned about in lab will come in handy (1111 students or others that missed the lab: see [lab 06](lab06-strpuz.html), especially the "Tools to Use" section).

Since you can't rely on the number of spaces, it probably makes sense to find the operator and slice off the part before and after that to turn into `int`s.

`int` can deal with spaces just fine (`int(" 12  ")`{.python} works).

