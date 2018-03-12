---
title: "PA 13: str_redux.py"
...

# Task

Write a file named `str_redux.py` that implements versions of the string methods `find` and `split` without using any string methods or functions.

In particular, define a function `myfind` such that `myfind(s,t)`{.python} does the same thing that `s.find(t)`{.python} does;
and a function `mysplit` such that `mysplit(s,t)`{.python} does the same thing that `s.split(t)`{.python} does.

You may not use any [string methods](https://docs.python.org/3.6/library/stdtypes.html#string-methods) in your solution.
All operators (including `in`, `[index]`, `[i1:i2]`, etc) are fair game.
None of the functions (nor the file itself) should `print`{.python} anything nor ask for any `input`{.python}.

In addition to functional correctness, some points will be reserved for

1.  having good variable names
1.  having meaningful docstrings for all functions you write

# Example Invocations

When you run `str_redux.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import str_redux

print(str_redux.myfind('divided','d'))
print(str_redux.myfind('divided','id'))
print(str_redux.myfind('divided','ido'))

print()

print(str_redux.mysplit('divided','d'))
print(str_redux.mysplit('divided','id'))
print(str_redux.mysplit('divided','ido'))
````

you should get the following output:

````
0
3
-1

['', 'ivi', 'e', '']
['div', 'ed']
['divided']
````

# Troubleshooting

- `myfind` is simpler than, and will help prepare you for, `mysplit`. We suggest getting `myfind` working properly before starting on `mysplit`.
    - Did you test the edge cases of first- and last-characters? i.e., can you find both the `h` and `o` in `'hello'`{.python}?
- You'll likely find that `mysplit` is easier to write by calling `myfind` within it.
