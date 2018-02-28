---
title: "PA 15: credit_card.py"
...

# Task

Write a file named `credit_card.py` containing a single function, `check`.
Check accepts a single input -- a positive integer.
It returns `True`{.python} if the integer represents a valid credit card number.
As with all functions that return a `bool` value, if it does not return `True` it should return `False`.

Credit card numbers have what is called a check digit.
This is a simple way of detecting common mis-typings of card numbers.
The algorithm is as follows:

1.  Form a sum of every other digit, including the right-most digit;
    so 5490123456789128 (5**4**9**0**1**2**3**4**5**6**7**8**9**1**2**8**) sums to 4 + 0 + 2 + 4 + 6 + 8 + 1 + 8 = 33.
2.  Double each remaining digit, then sum all the digits that creates it;
    the remaining digits (5 9 1 3 5 7 9 2) in our example (**5**4**9**0**1**2**3**4**5**6**7**8**9**1**2**8) double to 10 18 2 6 10 14 18 4,
    which sums to 1+0 + 1+8 + 2 + 6 + 1+0 + 1+4 + 1+8 + 4 = 37
3.  Add the two sums above (33 + 37 = 70)
4.  If the result is a multiple of 10 (i.e., its last digit is 0) then it was a valid credit card number.

In addition to functional correctness, some points will be reserved for

1.  having good variable names
1.  having meaningful docstrings for all functions you write


# Example Invocations


When you run `credit_card.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import credit_card

if credit_card.check(1):
    print('ERROR: 1 is not valid')

if credit_card.check(240):
    print('GOOD: 240 is valid')

if credit_card.check(9548):
    print('GOOD: 9548 is valid')

if credit_card.check(5490123456789129):
    print('ERROR: 5490123456789129 is not valid')
````

you should get the following output:

````
GOOD: 240 is valid
GOOD: 9548 is valid
````


# Thought Question

How hard would it be to suggest a similar correct card number when the input was incorrect?
How many digits would need to change?
Could you put the change in any digit?
Could you suggest inserting a missing digit?

It is also possible to do this without ever dealing with any multi-digit numbers... but doing it that way makes the code fairly ugly.

# Troubleshooting

You probably want a `for`{.python} loop -- in fact, you probably want more than one.

You can iterate every-other index in several ways:
iterating every index and skipping some with an `if`,
iterating the first half of indices and doubling each with `*2`, or 
using [the three-argument version of `range`{.python}](https://docs.python.org/3/library/stdtypes.html#range).

If you have not done the check by hand on paper, you are going to find this *very* hard.

If your code is not working for a few numbers, try adding `print`{.python} statements inside your loops and checking that what is printed is what should be printed according to how you did it on paper.

The easiest way to get the digits out of an `int`{.python} is to convert it to a `str`{.python}, but using `%`{.python} is also possible and not much harder.

The last digit is `% 10` (for an `int`{.python}) or `[-1]` (for a `str`{.python}).

Make sure you return `True` and `False`, not other true-ish or false-ish values like `1` or `None`.
