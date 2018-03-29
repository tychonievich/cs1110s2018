---
title: "PA 16: gradebook.py"
...

# Task

In this class, like many others, assignments are clustered by type: exams, programming assignments, etc.
Each assignment type has a given weight, and each assignment within a given type might also have a weight.
For example, exams might be 50% of the overall grade and the final exam might be worth 1.5× as much as a midterm.

Write a file `gradebook.py` that has (one or more) global gradebook `dict`, which stores a running total and cumulative weight for each supplied grade type^[You'll probably need at least two pieces of information per grade type, but there are several things you could store; anything that lets the two functions work is OK.];
and two functions to interact with that `dict`:


## `assignment(kind, grade, weight)`{.python}

The `kind` will be a string, and will indicate which group of assignments this one belongs to.
It might be either a known kind or a new one.

The `grade` will be a number between 0 and 100, indicating how well the student did on this assignment.

The `weight` is optional; if present, it indicates how much weight this assignment has compared to others of this kind.
If not present, assume it is `1`{.python}

The behavior of this function is to add to the running total grade for the given kind, using a similar logic to what you used in [PA 07 -- GPA](pa07-gpa.html) but with a different running total for each kind, stored in a `dict`.

## `total(proportions)`{.python}

Given a `dict` with keys as types of assignments and values as ratios of overall grade this type applies to,
return the cumulative grade so far based on this set of proportions.

You may assume the values in the `dict` total to `1.0`.

The given `proportions` may include assignment types that have never been sent to `assignments(...)`; return the grade assuming the student got 0 in those missing assignments.

The given `proportions` may fail to include some assignment types that were sent to `assignments(...)`; those assignment types do not contribute to the returned grade.

## Style matters

In addition to functional correctness, some points will be reserved for

1.  having good variable names
1.  having meaningful docstrings for all functions you write

# Example Invocations

When you run `gradebook.py`, nothing should happen.
It defines functions, it does not run them.

If in another file (which you do not submit) you write the following:

````python
import gradebook

syllabus = {
    'exam': 0.5,
    'hw': 0.4,
    'lab': 0.1,
}
print(gradebook.total(syllabus))
gradebook.assignment('exam', 83)
gradebook.assignment('exam', 88)
gradebook.assignment('exam', 91, 2)
print(gradebook.total(syllabus))
gradebook.assignment('hw', 100)
gradebook.assignment('hw', 100)
gradebook.assignment('hw', 70)
gradebook.assignment('hw', 0)
gradebook.assignment('hw', 100, 4)
gradebook.assignment('hw', 50)
gradebook.assignment('lab', 90)
print(gradebook.total(syllabus))
gradebook.assignment('extra', 300)
print(gradebook.total(syllabus))
````

you should get the following output:

````
0
44.125
85.125
85.125
````

Your program should also work with any other syllabus and any number of assignment types of any name.

# Troubleshooting

You'll almost certainly want to have one `global`{.python} `dict` to store the per-kind averages. There are alternatives to this, but they are significantly more complicated.

There are several ways to compute a weighted average, but the simplest is to

1.  Compute the simple average (mean) of all the scores in each category individually
    -   If an assignment has extra weight, count it as worth more within its average, like you did in [PA 07](pa07-gpa.html)
1.  Multiply each computed average by its weight and sum the results

You program should also work if we re-order the `assignment` invocations, including having another `exam` in the middle of the `hw`s.

There are many ways to set up your `dict`s. For example, you could

-   Have a `dict` of `list`s of scores
-   Have one `dict` of compiled averages and another of credit counts
-   Have one `dict` of credit counts and another of accumulated grade points
-   ...

It should be possible to call `total` multiple times, with or without additional `assignment`s in between, and get the right answer each time.

