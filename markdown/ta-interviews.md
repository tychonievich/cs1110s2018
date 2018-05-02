---
title: Interviewing to be a TA
...

# What we want

We have many people apply to be a TA for CS 1110.
We unfortunately lack the funding to hire them all, and also lack the bandwidth to train and oversee them all if we did hire them all.
Thus, we have to be somewhat selective in whom we hire.

We are looking for TA applicants who

-   Know the material.
    Fall 2018 will teach using the Python language and the PyCharm editor;
    you should be comfortable with these.

-   Did reasonably well in Intro to Programming.
    As and Bs are prefered;
    Cs often represent sufficient struggle that effective TAing is unlikely.
    If you had a C in intro but did better in later courses,
    we encourage you to TA for those later courses.

-   Relate well to struggling students.
    Having struggled yourself can be a plus;
    but in general we want TAs who help calm and validate students
    rather than TAs who show off how much they know or seem condescending.

-   Teach, not solve.
    TA stands for "teaching assistant" not "assignment assistant;"
    we want TAs who help students solve to their own problems.

# Interview

To help evalaute whom to hire, we are instituting a two-phase interview process.
We have not done this before, so there might be some kinks in the system…

## Stage 1: TA-led interview

You will sign up for an interview slot with a pair of current CS 1110 TAs.
You'll have 15 minutes; that time will be used as follows:

-   One TA will role-play being a student needing help in an assignment.
    You'll role-play being their TA.
    They'll have some broken code and you'll help them.
    The assignment we'll use is listed below.
    
    The other TA will observe, noting how you do.
    
    This is expected to take 8--10 minutes.
    
-   You'll be asked to reflect on the role-play.
    What did you do well?  What should you have done differently?

-   There'll be time for you to ask any questions you might want
    about TAing, your performance, etc.

At the end of all TA-led interviews, the TAs will give a list of recommendations to the lead instructor for CS 1110 and 1111.

TA-led interviews will occur primarily during the last weeks of the semester preceding the hired-for semester.

## Stage 2: Instructor-led interview

It is our goal to have a TA-let interview for most (if not all) applicants;
the lead instructor, who is just one person, will of necessity have to be more selective.

The basic structure of the instructor-led interview will be similar to the TA-led interview,
though (a) there will be one interviewer present, not two; and (b) the assignment will be different.

We are working to secure promise of funding soon.
However, traditionally the department does not commit to a particular number of TA slots until the first week of classes.
If that tradition holds, instructor-led interviews will occur during the first weeks of classes and hiring decisions will be made at that time.

# The assignments

## Stage 1

Write a program that reads a file containing a list of data in the format:

````
year,month,day,high,low,average
````

It should include a function that calculates the average temperature between two days and takes two lists `[year, month, day]` that represent two days as arguments.

When run, the program should prompt the user for the data needed to find two lines in the file and invoke the function on those days, printing the result.

An example data file (obtained from the [national climatic data center](https://www.ncdc.noaa.gov/)) can be found at <http://cs1110.cs.virginia.edu/files/cho-temp.csv>.

## Stage 2

> Stage 2 will take place in the first weeks of the Fall semester, and the professor writing this document may not be the same as the one conducting the interviews. If the new professor provides different instructions, follow them in lieu of what appears below. 

Write a program that asks the user for an integer greater than 1, then prints out the list of prime factors of that integer.
Your solution should break the problem into sub-problems and add functions with one sub-problem per function.
Your output should include the original number and the factors, smallest factor first.

Recall that 

-   *x* is a factor of *y* if the remainder of *y* ÷ *x* is zero.
-   *x* is prime if its only positive integer factors are 1 and itself.
-   *x* is a prime factor of *y* if both (a) *x* is a factor of *y* and (b) *x* is prime.
-   every integer ≥ 2 has a unique prime factorization; for example, 28 = 2 × 2 × 7 and 28 cannot be factored into any other set of primes.


### Stage 2 Example runs

````
What number? 7
The prime factors of 7 are [7]
````

````
What number? 32
The prime factors of 32 are [2, 2, 2, 2, 2]
````

````
What number? 1110
The prime factors of 1110 are [2, 3, 5, 37]
````

### Stage 2 reference solution

As a TA, you generally have access to a reference solution, written to aid in autograding, though that solution is not always the best model for students.  We have [a reference implementation of this program](files/factor.py) if you want to peruse it.

