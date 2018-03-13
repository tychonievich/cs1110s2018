---
title: "Lab 5: Coding on Paper"
...

<center style="font-size:200%; margin:1em; ">
The slides used in lab can be found [here](https://docs.google.com/a/virginia.edu/presentation/d/1e0Uc4ffu3tmSY_6uEqOkfqpunXYwVd61XWIoUGIne_w)
</center>

# Participation

Labs are graded primarily on presence and participation, not product.
Be there and be kind to others.

# Prepping for the Exam

For various reasons, CS 1110 exams are given on paper and involve writing code by hand.
The goal of this lab is to prepare you for that: both the on-paper coding and the idea of being tested.


## TPEGS

We use a system called TPEGS to scan, grade, and return your paper exams.
For this to work, you need to fill in a bubble sheet on the first page of your exam.
The bubble region looks like this:

![Blank TPEGS footer](files/tpegs.png)

You fill in your computing ID, skipping rows if you have less than 6 characters in your id, like this:

![Example filled-in TPEGS footers](files/tpegs-examples.png)

The footers are read optically, so please fill in the bubbles darkly (either with ink or dark pencil).

## Lab mechanics

This lab will run as follows:

1.  The TAs will review what you've learned this week
1.  Paper coding questions will be distributed; you'll have some time to work on them
1.  The TAs will show the reference solution and the grading rubric; you'll grade your own papers
1.  Conversation about lessons learned and tips for successful testing maybe shared, time allowing


## Grading rubrics

Every piece of code looks a little different and we don't expect perfection on paper, but here are some thing we do look for:

1.  Neatness.  It should be easy to read what you wrote.

    -   Handwriting shouldn't require a huge effort to understand
    -   Indentation should line up pretty well -- it needn't be perfectly straight, but there should be no ambiguity what's indented how much
    -   We expect you to get colons, key-words, and parentheses right (e.g., `def baz(x, y):`{.python} not `define baz[x, y]`)

2.  Correctness.  The algorithm you write should solve the problem given.

    -   Partial credit for solving some cases but not all (but no credit for [hard coding](faq.html#what-is-hard-coding))
    -   Partial credit for comments outlining a good approach without supporting code
    -   Partial credit for a few missing bits

3.  Constraints.  Follow the directions...

    -   If we say "Write a function named `xyxxy`", don't name yours `quux` instead
    -   If we say "Write a function" give us a function, not a program
    -   Don't confuse input for arguments, nor return for print

We'll show you an actual point break-down after you code---we make custom rubrics for each question, often giving away part of the answer, so you won't get to see the rubric before you code.

# What else is on the exam?

In addition to coding-on-paper, we typically include

-   We might ask you what example code does, such as

    What does the following print?

    ````python
    def f(g):
        global h
        g = g + g
        h = g
        print(g)
        print(h)
    g = "3"
    h = 4
    f(g)
    print(g)
    print(h)
    ````
    
-   We might ask you for the type, value, or both of an expression; for example, we might expect you to identify that `2 * 3 / 2`{.python} is value `3.0`, type `float`.

-   We might ask open-ended questions, like "What is one advantage of writing functions in your code?"
    
    We don't ask very many of these kinds of questions because it is hard to find questions where all instructors agree on the right grading policy, but we like to ask at least a few.

-   We might ask questions about Python syntax and semantics, such as

    Which of the following is an error?
    
    1.  `2 * 3`{.python}
    1.  `'2' * 3`{.python}
    1.  `2 * '3'`{.python}
    1.  `'2' * '3'`{.python}

We try to design the exam so that the median student completes it before the 50 minutes are up.
Hitting this goal is not easy, but we try...

# Past Exams

Past exams and their rubrics can be found on the [review page](review.html).
Some minor edits are typically made to the rubric during grading, which are not reflected on those available from that site.

# Things we expect you to know

Built-in functions in Python
:   
    -   `print`{.python}
    -   `input`{.python} -- and related terminology like "prompt"
    -   `int`{.python} -- what it does given a string or a float and when it creates an error
    -   `str`{.python} -- what it does given an integer or a float
    -   `float`{.python} -- what it does given a string or an integer
    -   `len`{.python} -- to find length of strings
    -   `type`{.python} -- to find the type of a value

Python operators
:   
    -   `-`, `+`, `*`, `/`, `%`, `//`, `**`
    -   How operators and types interact (e.g., that `type(4/2)`{.python} is `<class 'float'>` not `<class 'int'>`; that `+` works on strings but `-` does not; that `*` can work with a string and an integer but not with two strings; etc).
    -   The update-assignment versions of each operator (e.g., `+=`)
    -   The logical operators `and` and `or`
    -   The comparison operators `<`, `<=`, `==`, `!=`, `>=`, and `>`

Variables and assignment
:   
    -   Correct syntax for assignment operator `=`
    -   Local vs global scope
    -   That a variable names a (_value_, _type_) pair
    -   the `global` keyword
    
Literals
:   
    -   Integer literals like `1111`{.python}
    -   Floating-point literals like `11.11`{.python}
    -   Boolean literals `True` and `False`
    -   String literals in all their forms: `'single'`{.python}, `"double"`{.python}, `'''triple-single'''`{.python}, `"""triple-double"""`{.python}, and `'with \\'escape sequences\\' for internal quotes'`{.python}

Functions
:   
    -   Definition with `def name(argument, list):`{.python}
    -   `return`{.python}: what it does, including that it ends the function
    -   invocation with `name(argument, values)`{.python}
    -   Creation and conclusion of local scope
    -   Why we like functions

Conditionals
:   
    -   Definition with `if`{.python}, `elif`{.python}, and `else`{.python}
    -   Putting conditionals inside functions or other conditionals
