---
title: "Lab 5: Coding on Paper"
...

# Background

The students have had six lectures since the add deadline:

-   one that introduced `print`, `input`, comments, literals, and whitespace
-   one that introduced `type`, values, `=`, variables, operators, and math
-   two that introduced `def`, parameters, `return`, and docstrings
-   one that introduced variable scope, globals, and locals
-   one that introduced `if`, `elif`, `else`, and comparison operators

One additional lecture before the exam will cover `and`, `or`, and `not`.

# Running the Lab

1.  Review TPEGS footers from [the lab's main site](lab-5-paper.html#tpegs)
1.  Review the three kinds of grades listed [on the lab's main site](lab-5-paper.html#grading-rubrics)
1.  **for** exercise **in** exercises:

    - Show the students a coding prompt.
    - Give them time to work on it.
    - Show the example solution; walk through it, answering any questions.
    - Show the rubric; have students grade their own assignments
    - Answer any remaining questions


# Exercises

See [google slides](https://docs.google.com/presentation/d/1e0Uc4ffu3tmSY_6uEqOkfqpunXYwVd61XWIoUGIne_w) for these exercises prepped for lab.

## One-liner

Write a Python expression for "the remainder of _a_^_b_^ divided by seven"


### Key

````python
a**b % 7
````

### Rubric (10 points)

- 2 points for having a `%` (1 point for a made-up function name like `mod` or `remainder`)
- 2 points for having either `**`, `pow`, or `math.pow` (1 point if a made-up function name like `power` or the wrong name like `math.exp`)
- 1 point for computing _a_^_b_^
- 1 point for computing something `% 7` (or `% seven`)
- 2 points for writing just an expression (no `print`, `def`, `=`, etc)
- 2 points for a fully correct answer
- Extra parentheses are free
- If it is not clear what was meant (e.g., the `*` look like `∙` or `x`) give at most half of the points for the portion in question
- If comments describe the right process but code is not present, give at most half of the points


## Function

Write a Python function named `norm_num` that takes a single parameter.  It does the following:

1. Use `float` to convert the parameter to a floating-point number
2. Use `int` to convert the result of `float` to an integer
3. If the integer and floating-point number are the same value, return the integer; otherwise, return the floating-point value

### Example invocation

Running `norm_num(2)`{.python} should return `2`{.python}

Running `norm_num(2.0)`{.python} should return `2`{.python}

Running `norm_num(2.3)`{.python} should return `2.3`{.python}

Running `norm_num('2.0')`{.python} should return `2`{.python}

### Key

````python
def norm_num(n):
    f = float(n)
    i = int(f)
    if i == f:
        return i
    else:          # else not needed; could have return on this line instead
        return f
````

### Rubric (12 points)

- 5 points: function structure
    - 1 point: `def`
    - 1 point: function named `norm_num`
    - 1 point: one argument; used its name consistently
    - 1 point: parentheses and colon
    - 1 point indentation
- 5 points: followed algorithm
    - 2 points: invoked `float` and `int`
    - 1 point: invoked `int` on `float`'s result, not the original parameter
    - 1 point: compared results with `if`
    - 1 point: returned the correct result
- 2 points: `return`, not `print`
- &minus;1 point: used `=` instead of `==`
- &minus;1 point: poor `if` syntax (keyword, colon, indentation)
- up to &minus;3 points for excessively sloppy indentation or writing


## Program

Write a Python program that asks the user for their age and year of birth and replies with one of the following phrases: "Your birthday is coming up!", "You've already had a birthday this year", or "Shouldn't you either be _age~1~_ or _age~2~_?"

Your program should assume it is being run in the year 2017.

### Example Runs

One example run might be

    How old are you? 18
    What year were you born? 1998
    Your birthday is coming up!

Another example run might be

    How old are you? 21
    What year were you born? 2001
    Shouldn't you either be 15 or 16?

### Key

````python
age = input('How old are you? ')
birth = input('What year were you born? ')
turning = 2017 - int(birth)
age = int(age)

if turning == age:
    print("You've already had a birthday this year")
elif turning - 1 == age:
    print("Your birthday is coming up!")
else:
    print("Shouldn't you either be", turning - 1, "or", str(turning)+"?")
````

### Rubric (12 points)

- 4 points for correct use of `input` and `print`
    - 1 point: used `something = input(`
    - 1 point: prompts present and appropriate 
    - 1 point: prompts end in `? ` or `: `
    - 1 point: the right set of responses
- 2 points: converted input to integer using `int` (or `float`)
- 4 points for correct `if`
    - 1 point: three cases
    - 1 point: one and only one case used per run
    - 1 point: compare `2017-birth` to `age` or `2017` to `birth+age`
    - 1 point: correct comparisons
- 2 points: correct two ages in `else` case
- Free: missing/extra spaces; putting `'` inside a `'`-delimited string
- &minus;1 point: `int + str` or other type errors
- &minus;1 point: used `=` instead of `==`
- &minus;1 point: poor `if` syntax (keyword, colon, indentation)
- &minus;1 point: missing quotation marks
- up to &minus;3 points for excessively sloppy indentation or writing

## Function (extra, only if excess time)

Write a Python function named `ordinal` that takes a single integer parameter; it returns a single string consisting of a string representation of the integer followed by a two-letter suffix.
The suffix is `th` unless one of the following holds:

- If the input number ends in a `1` but not a `11`, the suffix should be `st`
- If the input number ends in a `2` but not a `12`, the suffix should be `nd`
- If the input number ends in a `3` but not a `13`, the suffix should be `rd`

### Example invocation

Running `ordinal(243)`{.python} should return `'243rd'`{.python}

Running `ordinal(213)`{.python} should return `'213th'`{.python}

### Key

````python
def ordinal(n):
    if n%10 == 1 and n%100 != 11: 
        return str(n) + 'st'
    elif n%10 == 2 and n%100 != 12: 
        return str(n) + 'nd'
    elif n%10 == 3 and n%100 != 13: 
        return str(n) + 'rd'
    else:
        return str(n) + 'th'
````

### Rubric (16 points)

- 5 points: function structure
    - 1 point: `def`
    - 1 point: function named `ordinal`
    - 1 point: one argument; used its name consistently
    - 1 point: parentheses and colon
    - 1 point indentation
- 4 points: suffix construction
    - 2 points: `str(parameter)`
    - 1 point: `str(parameter) + 'ending'`
    - 1 point: has all four suffixes
- 5 points: logic
    - 1 point: at least one ends-in-digit case
    - 1 point: at least one but not two-digits case
    - 3 points: has approximation of other three cases
- 2 points: `return`, not `print`
- &minus;1 point: used `=` instead of `==`
- &minus;1 point: poor `if` syntax (keyword, colon)
- up to &minus;4 points for excessively sloppy indentation or writing

