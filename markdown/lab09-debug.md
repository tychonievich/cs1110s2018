---
title: "Lab 9: Debugging"
...

# Mechanics

There will be 

1.  A logic-group activity
2.  Pairing to work on the lab tasks.
    For this lab, you'll likely want to join with a second pair; four minds are better than two for some tasks!
3.  TAs pulling aside students to explain their code.

# Setup


## Overview

The goal of this lab is to practice debugging techniques.
To that end we have a program which we have intentionally seeded with various kinds of common bugs.
You'll sleuth them out and fix them.

## Debugging tips

As a reminder, debugging typically works as follows:

1.  Determine that there is a problem, typically by identifying a set of inputs that creates the wrong result.

2.  Discover where in the code the wrong behavior is introduced.  A general guide to doing this is

    -   Add `print`{.python} statements to help determine what is happening

    -   Include enough information to know if what is happening is what should happen, such as

        -   putting a `print`{.python} inside a control construct (`if`{.python}, `while`{.python}, or `for`{.python}) to see if you getting inside the control construct the expected number of times
        -   printing the value of variables to see if they are what you expect
        -   printing part of a subsequent expression to see if its parts are correct.  For example, if `fun[fun.index('keen') + 1] < 'nifty'`{.python} is doing the wrong thing, you might print `fun.index('keen')` to see if it is a sensible value.
    
    -   Narrow in on where the problem happened, using a variant of "binary search":
        
        1.  print before anything goes wrong and after you know something is wrong
        2.  print something about halfway between the other two prints
        3.  if the new print suggests things are working, you only need look after it; or if broken, you only need to look before it; either way, you've cut the region where the problem may have occurred in half
        4.  repeat steps 2 and 3, narrowing the region where the problem must have occurred in half again and again until you locate the problem
    
3.  Once you find the source of the problem, fix it.

## The code to debug

### Nim

In this lab we provide [a broken implementation](files/debug_task.py) of one variant of Nim, a game defined as

> Assume you have a large pile of marbles. Two players alternate taking marbles from the pile. In each move, a player is allowed to take between 1 and half of the total marbles. So, for instance, if there are 64 marbles in the pile, any number between and including 1 and 32 is a legal move. Whichever player takes the last marble loses.

The optimal strategy is to always take enough marbles so that the remaining pile is one less than a power of two.
That optimal strategy is what the code you are given is trying to do.
On any turn in which it cannot play that strategy (because doing so requires taking an illegal number of marbles), it will take one marble instead.

### Example of the strategy

For example, the computer is supposed to play as follows:

1.      The Game of Nim

        The number of marbles in the pile: 7
        Who will start? (p or c): c
    
    The computer sees a pile with 7 marbles.
    It wants to take enough marbles so that the remainder is one less than a power of 2.
    7 is already one less than a power of 2 ($2^{3}-1 = 7$), but you can't take 0 marbles.
    The next smaller target size is 3 ($2^{2}-1 = 3$); to get there requires taking 4 marbles, which is more than half of the pile and thus not allowed.
    Since no one-less-than-power-of-two can be reached, the computer takes 1 marble.

        The computer takes 1 marbles.
        The pile has 6 marbles in it.

    Let's assume the player also takes 1 marble.

        How many marbles to you want to take (1-3): 1

2.      The pile has 5 marbles in it.
    
    The computer sees a pile with 5 marbles.
    It wants to take enough marbles so that the remainder is one less than a power of 2.
    The next smaller power of 2 is 4 ($2^{2}$) so it wants the pile to be 3 ($2^{2}-1 = 3$) after it takes marbles.
    That means taking 2 marbles ($5-2=3$), which is a legal move.

        The computer takes 2 marbles.
        The pile has 3 marbles in it.
        How many marbles to you want to take (1-1): 1

3.      The pile has 2 marbles in it.

    The computer sees a pile with 2 marbles.
    It wants to take enough marbles so that the remainder is one less than a power of 2.
    That is a power of two already ($2^{1}$) so it wants the pile to be 1 ($2^1-1=1$) after it takes marbles.
    That means taking 1 marbles ($2-1=1$), which is a legal move.

        The computer takes 1 marbles.
        The pile has 1 marbles in it.
        How many marbles to you want to take (1-1): 1
        The computer wins!

### Your Goal

Unfortunately, the [code we give you](files/debug_task.py) does not currently work properly.
Your job is to fix it (not re-write it); the best solutions will change, insert, or delete fewer than a dozen lines of code.

When you are finished debugging, you should be able to play the following game:

    The Game of Nim

    The number of marbles in the pile: 0
    The number of marbles in the pile: 127
    Who will start? (p or c): c
    The pile has 127 marbles in it.
    The computer takes 1 marbles.
    The pile has 126 marbles in it.
    How many marbles to you want to take (1-63): 63
    The pile has 63 marbles in it.
    The computer takes 1 marbles.
    The pile has 62 marbles in it.
    How many marbles to you want to take (1-31): 31
    The pile has 31 marbles in it.
    The computer takes 1 marbles.
    The pile has 30 marbles in it.
    How many marbles to you want to take (1-15): -1
    How many marbles to you want to take (1-15): 0
    How many marbles to you want to take (1-15): 1
    The pile has 29 marbles in it.
    The computer takes 14 marbles.
    The pile has 15 marbles in it.
    How many marbles to you want to take (1-7): 7
    The pile has 8 marbles in it.
    The computer takes 1 marbles.
    The pile has 7 marbles in it.
    How many marbles to you want to take (1-3): 2
    The pile has 5 marbles in it.
    The computer takes 2 marbles.
    The pile has 3 marbles in it.
    How many marbles to you want to take (1-1): 1
    The pile has 2 marbles in it.
    The computer takes 1 marbles.
    The pile has 1 marbles in it.
    How many marbles to you want to take (1-1): 1
    The computer wins!

## Submission

**At least one partner** should submit one .py file named `debug_task.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **all partners' ids** in comments at the top of the file.
