---
title: "PA 05: maydate.py"
...

# Task

Write a file with one function: `creepy`.
`creepy` should have two arguments, the ages of two people.
It should return `False`{.python} if the two may date each other without being creepy, `True`{.python}.
See [dating.py](w01-dating.html) for a definition of creepy.

Return the Boolean values `True`{.python} and `False`{.python}, not the strings `"True"`{.python} and `"False"`{.python}.

Note: it is possible to solve this problem using `if`{.python}, but that is not encouraged.
Your function should neither `print`{.python} nor ask for any `input`{.python}.
You should not have any code outside of the function.

You may assume that we only invoke the function with the younger age &ge; 14 and the older age in the second position.

# Example Invocations

When you run `maydate.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import maydate

print(maydate.creepy(18, 80))
print(maydate.creepy(50, 80))
print(type(maydate.creepy(50, 80)))
````

you should get the following output:

````
True
False
<class 'bool'>
````

# Thought Question

We won't test it, but what does your code do if you pass in the older age first?

````python
print(maydate.creepy(22, 18))
print(maydate.creepy(31, 18))
````

How hard would it be to make it work for both age orders?

We won't test fractional ages, but does your code work for them?  For example, does it think that a fifteen-year-old can date a fourteen-and-a-half year old?

The rule as given says it is creepy for a 13-year-old to date *anyone*.
How hard would it be to make a *different* function that is more permissive, always allowing people to date &plusmn;1 year even if they are under 16?
(Don't use a revised rule like this for the function you turn in!)


# Troubleshooting

You should probably write *two* python files for this assignment; the one you turn in (`maydate.py`) that *defines* `creepy` and a separate file you use to test it.
In your testing file,

-   Don't forget to `import maydate`{.python}
-   Try both the examples we give above and other examples of your own
-   When adding examples, make sure you know what the right answer is supposed to be!

Confused on how to not use `if`{.python}? 
Consider the following example:

````python
def example(x, y):
    '''returns True if x is bigger than y, False if it is not'''
    return x > y
````

Remember that Python cares about indentation, and that every more-indented block must be preceded by a colon `:`.

Want to write something more than just `<`{.python}?  and `>`{.python}?
There is a chart of other comparison operators (the Python equivalents of things like &ne; and &le; in Python) in &sect;6.1.2.
