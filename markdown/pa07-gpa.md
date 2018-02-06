---
title: "PA 07: gpa.py"
...

# Warning -- Draft Status

This assignment is still in draft status. It may change.

# Task

Write a file named `gpa.py` that computes a cumulative GPA using three functions:
`add_course` adds a new course to the running total, and `gpa` and `credits` gets your cumulative GPA and credit count, respectively.
It uses two global variables to keep track of GPA and credits (both initially 0).

-   Invoking `gpa.add_course(3.7, 3)` should add a 3-credit course with GPA 3.7 to the running GPA and credit count total.
-   Invoking `gpa.gpa()` should retrieve your current total GPA.
-   Invoking `gpa.credit_total()` should retrieve your current total credits earned.
-   Invoking `gpa.add_course` with only one argument (e.g., `gpa.add_course(3.7)`) should add a 3-credit course.

None of the functions nor the file itself should `print`{.python} anything nor ask for any `input`{.python}.

# Example Invocations

When you run `gpa.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import gpa

gpa.add_course(4.0, 3)
print(gpa.gpa(), gpa.credit_total())

gpa.add_course(3.3)
print(gpa.gpa(), gpa.credit_total())

gpa.add_course(2.3, 4)
print(gpa.gpa(), gpa.credit_total())
````

you should get the following output:

````
4.0 3
3.65 6
3.11 10
````

# Troubleshooting

In case you are a little rusty on adding weighted averages, given an old GPA of $g_o$ and credit count of $c_o$, adding a course with GPA $g_c$ and credit count $c_c$ changes the GPA to be $(g_o c_o + g_c c_c) ÷ (c_o + c_c)$. For example, ... (to be added)

Make sure you understand the contents of our textbook, §8.2.4 and §8.3.2.
