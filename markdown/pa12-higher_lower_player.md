---
title: "PA 12: higher_lower_player.py"
...

# Task

Write a file named `higher_lower_player.py` that plays a simple guessing game with you.
The game is the same as [the previous assignment](pa11-higher-lower.html),
but the roles are reversed: you think of the number, the computer guesses.

Before the game begins, the computer should ask how many guesses it gets.

If the computer loses, it should ask what the correct answer was.
It should also check to make sure that the answer is legal, and complain if it wasn't.

If the user gives inconsistent answers, the computer should complain and stop playing.

In addition to functional correctness, some points will be reserved for

1.  having good variable names
1.  having meaningful docstrings for any functions you write (note: functions are not required for this assignment, but might make sense).

# Algorithm

The optimal strategy for a game like this, assuming you don't know the person thinking of the number well enough to make an informed guess, is as follows.

-   Keep track of the range of possible numbers (initially 1 to 100)
-   Always guess the middle of that range
-   Move one endpoint of the range or the other based on the user response

# Example Invocations

An example run of the program might look like:

````
Think of a number between 1 and 100 and I'll guess it.
How many guesses do I get? `5`
Is the number higher, lower, or the same as 50? `lower`
Is the number higher, lower, or the same as 25? `higher`
Is the number higher, lower, or the same as 37? `lower`
Is the number higher, lower, or the same as 31? `higher`
Is the number higher, lower, or the same as 34? `lower`
I lost; what was the answer? 33
Well played!
````

Another run might look like:

````
Think of a number between 1 and 100 and I'll guess it.
How many guesses do I get? `8
Is the number higher, lower, or the same as 50? `lower`
Is the number higher, lower, or the same as 25? `higher`
Is the number higher, lower, or the same as 37? `lower`
Is the number higher, lower, or the same as 31? `higher`
Is the number higher, lower, or the same as 34? `lower`
Is the number higher, lower, or the same as 32? `higher`
Is the number higher, lower, or the same as 33? `lower`
Wait; how can it be both higher than 32 and lower than 33?
````

Another run might look like:

````
Think of a number between 1 and 100 and I'll guess it.
How many guesses do I get? `1`
Is the number higher, lower, or the same as 50? `higher`
I lost; what was the answer? `20`
That can't be; you said it was higher than 50!
````


Another run might look like:

````
Think of a number between 1 and 100 and I'll guess it.
How many guesses do I get? `3`
Is the number higher, lower, or the same as 50? `same`
I won!
````


# Thought Question

We'll only run your program entering exactly one of `higher`, `lower`, or `same`, but a general human might also type things like `  higher` or `Lower` or `low`.
How robust can you make your program to not-quite-right user inputs?

The version we ask you to submit should use just integers, but you might also consider making a second version that uses floating-point numbers.
Can you make it start with integers and only switch to floating-point numbers when all integers are ruled out?
Even if you get it working, submit the integer-only version.

# Troubleshooting

Nothing in this assignment uses random values.  If you have `import random` in your code, you are doing something wrong.

Every prompt of every `input`{.python} should end with a space character, for this and every other assignment that uses `input`{.python}. 

You want integers, not floats.  Round down if rounding is required.  The `//` operator might help with this.

If the initial range is \[1, 100\] and the user says `higher` to 50, what is the new range?
Not that it should *not* include 50.

The loop should stop if any of the following become true:

-   there has been an answer of `same`
-   the range of possible `int`{.python} becomes empty
-   there have been too many guesses

The order of cases in an `if`{.python}/`elif`{.python}/`else`{.python} matters because if the first one is `True`{.python}, the others don't get checked.
Consider combinations of stopping conditions;
for example, if the answer is `same` *and* all guesses are used up, which message should appear?

You should ask what the answer is only if the number of guesses was exceeded.


