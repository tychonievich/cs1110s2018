---
title: "PA 09: averages.py"
...

# Task

Write a file named `averages.py` with several functions in it for computing averages of three values:

- `mean(a, b, c)`{.python} should compute the [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of `a`, `b`, and `c`.
- `median(a, b, c)`{.python} should compute the [median](https://en.wikipedia.org/wiki/Median) of `a`, `b`, and `c`.
- `rms(a, b, c)`{.python} should compute the [root-mean-square](https://en.wikipedia.org/wiki/Root_mean_square) of `a`, `b`, and `c`.
- `middle_average(a, b, c)`{.python} should compute the mean, median, and rms of `a`, `b`, `c`; and then return the median of those three averages.

Additionally, you should implement your solution such that

- `rms` invokes `mean` once.
- `middle_average` invokes `mean` and `rms` once each and `median` twice.
- use only features of Python we've learned in class (e.g., do not use `list`s, `sort`, `sorted`, etc.)


# Example Invocations

When you run `averages.py`, nothing should happen.
It defines functions, it does not run them.

If in another file (which you do not submit) you write the following:

````python
import averages

print(averages.mean(1, 5, 1))
print(averages.median(1, 5, 1))
print(averages.rms(1, 5, 1))
print(averages.middle_average(1, 5, 1))
````

you should get the following output:

````
2.3333333333333335
1
3.0
2.3333333333333335
````

Don't worry if you are off in the last few decimal places.


# Thought Question

How often is each of the three averages the middle average?  Are any of them always larger or always smaller than the others?

Can you use default values to allow your functions to work if only two arguments are supplied?  To get you started, consider writing `def mean(a, b, c=None):`{.python}.  If you get those working, what about allowing four or five values?

(Note: there [is a way](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists) to have arbitrarily-long argument lists, but we won't discuss the `tuple`{.python} construct it uses for a few weeks yet.)

There are [many other averages](https://en.wikipedia.org/wiki/Average); if you want additional practice, see how many of them you can get working.


# Troubleshooting

Your `mean` function can be a single line, as it only does math.

Your `median` function will probably need several `if`{.python} statements.

Did you test out your `median` when all three argument values are the same?

For `rms`, recall that <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ceaad50b7a0ae8ad64014319f138887ec5147f6c" title="square root means one-half power"/> an
