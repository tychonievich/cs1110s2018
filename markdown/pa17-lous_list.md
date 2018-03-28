---
title: "PA 17: lous_list.py"
...

# Task

It's advising time! Time to start thinking about classes for the Spring!

It can be tough to search through the course listings to find the classes you want.
So let's write a program to help you out!
The problem here that since registration for the Spring hasn't started yet, the data is kinda boring... so were are going to use data from a snapshot for registration for last Spring instead.

Write a library called `lous_list.py` that will contain two methods that will aid students in finding information about classes.

## The Data

We could have you write programs that access [Lou's List](http://rabi.phys.virginia.edu/mySIS/CS2) directly,
but there are several hundred of you and we don't want Lou Bloomfield to get upset if you all start having programs reading his site repeatedly.
Instead, we'll use snapshots hosted within our own course's webspace.
For example, if you want to see all the courses in the CS department, can go to:

<http://cs1110.cs.virginia.edu/files/louslist/CS>

and you'll see many lines like this:

    CS|1110|002|Introduction to Programming|Upsorn Praphamontripong|Lecture|3|true|false|true|false|true|1100|1150|Wilson Hall 301|181|200

We use the vertical-bar `|` as a separator because all of the more common separators (`,`, `;`, etc) are used at UVa as part of course titles.

By replacing the text after the last `/` with any department at UVa, you can see their classes;
for example, `BIOL` will load all Biology classes.

For each line on the page, the fields are (in order):

-   Dept ID (0)
-   Course Number (1)
-   Section (2)
-   Course Title (3)
-   Instructor (4) -- which may end with `+1` (or more; GBUS has a `+4` lecture) for multi-instructor classes.  This will always be a single-digit number if present.
-   Type of class (5)
-   Hours (6)
-   Monday (7)
-   Tuesday (8)
-   Wednesday (9)
-   Thursday (10)
-   Friday (11)
-   Start Time (12)
-   End Time (13)
-   Location (14)
-   Enrollment (15)
-   Allowable Enrollment (16)

Start and end times are expressed as a 3- or 4-character string representing a 24-hour clock
so, e.g., CS 1112 starts at 1400 and ends at 1515, for a duration of 75 minutes;
CS 2150 section 101 starts at 930 and ends at 1015 for a duration of 105 minutes.

Sections without times are not listed.

## Your Functions

### instructors
`def instructors(department)`{.python}

Returns an alphabetically-sorted list containing each instructor listed in Lou's List for the given department.
Do not count the same instructor twice.
Do not include `+1`s or the like.

For example, the `CS` list would contain `Luther Tychonievich` only once;
the `ECE` list would not contain `Andrea Vaccari+1` but would contain `Andrea Vaccari`.


### class\_search
`def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None)`{.python}

Returns a **list of lists** which contains all the information for all the classes that meet the provided criteria.

Most of the parameters are optional.
Only `dept_name` needs to be provided.
Defaults are listed above.
Details of the optional parameters are given below:

`has_seats_available`
:   If set to `True`, the function will check to ensure that Enrollment is not greater than or equal to Allowable Enrollment
    (i.e. there are seats actually available for a student to take).
    If set to `False` then it doesn't matter if there are seats available or not and current enrollment should be ignored when determining if the class should be returned or not.

    Note that `has_seats_available` will always be a boolean.

`level`
:   Given a 4-digit level value, the function should only include classes that are at that level.
    For example, saying `level=2000` should limit the list to only courses whose first digit is 2.

    Note that `level` will either be `None`{.python} or a four-digit integer (not a 1-digit integer or string).
    If `None`{.python}, do not limit the level the classes.

`not_before`
:   Tells the function to exclude all classes that start before (but not at) that time.
    For example, if you say `not_before=1000`,
    then the function should exclude 9:00 and 9:30 classes, but still include 10:00 classes.
    
    Note that `not_before` will either be `None`{.python} or an integer (not a string).
    If `None`{.python}, do not limit the start time of the classes.

`not_after`
:   Tells the function to exclude all classes that *start* after (but not at) that time.
    For example, if you say `not_after=1400`,
    then the function should exclude classes that start at 3:00, but not 2:00.

    Note that `not_after` will either be `None`{.python} or an integer (not a string).
    If `None`{.python}, do not limit the start time of the classes.

## Style matters

In addition to functional correctness, some points will be reserved for

1.  having good variable names
1.  having meaningful docstrings for all functions you write


# Example Runs

When you run `lous_list.py`, nothing should happen.
It defines functions, it does not run them.

If in another file (which you do not submit) you write the following:

````python
import lous_list

print(lous_list.instructors('BME'))

print('-'*40)

for f in lous_list.class_search('CS', level=3000, not_before=1100, not_after=1100):
    print(f)

print('-'*40)

print(len(lous_list.class_search('CS', False, 3000, not_after=1300)))
````

you should get the following output

````
['', 'Alexander Klibanov', 'Brian Helmke', 'Craig Meyer', 'Eli Zunder', 'Farzad Hassanzadeh', 'Frederick Epstein', 'George Christ', 'Jason Papin', 'Jeffrey Holmes', 'Jennifer Munson', 'Kevin Janes', 'Mete Civelek', 'Michael Lawrence', 'Richard Price', 'Shayn Peirce-Cottler', 'Steven Caliari', 'Timothy Allen', 'William Guilford', 'William Levy']
----------------------------------------
['CS', '3205', '001', 'HCI in Software Development', 'Mary Smith', 'Lecture', '3', 'false', 'true', 'false', 'true', 'false', '1100', '1215', 'Olsson Hall 009', '75', '80']
['CS', '3330', '001', 'Computer Architecture', 'Charles Reiss', 'Lecture', '3', 'false', 'true', 'false', 'true', 'false', '1100', '1215', 'Olsson Hall 120', '125', '135']
----------------------------------------
5
````

# Troubleshooting

Each department has its own URL: <http://cs1110.cs.virginia.edu/files/louslist/CS>, <http://cs1110.cs.virginia.edu/files/louslist/ECE>, etc.  That ending string (`CS`, `ECE`, etc) is provided as the `department` or `dept_name` argument to each function.

Don't forget to `decode('utf-8')` what you read from the web.

Stray `\n` in your strings?  You probably forgot to `strip()` before you `split(...)`.

The `def`{.python}-lines in the problem writeup will handle the default arguments for you.  Handling them should require no extra work on your part.

11:00 is not after 1100, nor it is before 1100.

`level=3823` and `level=3000` should do the same thing as one another...

Because the `+1` indicator is always a single-digit number if present, it can be detected by looking for the `+` (which always has the same index from the end of the string).

Web browsers sometimes try to be too smart for their own good, displaying files in the wrong format; for example, many browsers mis-read <http://cs1110.cs.virginia.edu/files/louslist/BME> as being an image file (which it is not) and thus do not show its content. You can get around this by printing the contents of the URL from python, or on most browsers by manually adding "view-source:" to the beginnign of the URL, like "<view-source:cs1110.cs.virginia.edu/files/louslist/BME>"
