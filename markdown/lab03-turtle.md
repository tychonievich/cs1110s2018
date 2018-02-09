---
title: "Lab 3: Art Contest"
...

# Grading Groups

In an effort to bring at least a tiny piece of small-class feel to the giant course that is 1110/1111, each of you will be assigned a particular grader, who will be one of your lab TAs.
When there are paired projects, such as most labs and your final project, you'll generally be expected to pair within the set of students that share your grader.
Thus, please sit near anyone you want to be paired with, and expect the TAs to open the lab with the boring but important process of recording grading groups.


# Pairing

For this and all subsequent labs, you will work in pairs.

We will use a model called "pair programming" in this class. There are a
few things to know about successful pairing under this model:

-   **2 minds, 1 focus**. If at any point the two of you are doing
    distinct things, such as each typing on your own computer or each
    looking at your own piece of paper, then you are not pairing
    properly.
-   **Driver and Navigator**. At any given point in time, one partner
    will be the "driver", controlling the keyboard, pencil, or other
    tool currently being used. The other will be the "navigator,"
    observing and commenting on the driver's actions
-   **Equality and Communication**. Driver and navigator are equal
    partners; the ideas of both are equally important, and both should
    talk, both should listen when the other speaks, and both should
    treat the other's ideas with respect.
-   **Switch Roles**. Which partner is driving should change at least
    every 15-20 minutes, if not more often.

Pairing in this model has many advantages both from a productivity and
learning standpoint. One of these is generally an increase the intensity
of focus, which can get tiring. Feel free to take breaks every now and
then, but try not to distract other pairs during your breaks.

For more hints on successful pairing, you might want to watch this
10-minute video on your own time:
[http://youtu.be/rG\_U12uqRhE](http://youtu.be/rG_U12uqRhE)

# Art Contest

Your goal with this lab is to make the *neatest picture you can* using
the turtle and any example code we have provided. You can use any of the
code posted on the lecture notes as a starting point, or you can use
your own.

Make sure to look at the Turtle API
[https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html).
(Remember: the API is the "list of things that you can do")

# Submission

Submit an image *and* your code, both under the `Lab03` item of the [CS 1110 submission page](https://archimedes.cs.virginia.edu/cs1110/).

## Image 

Save a picture of your image by doing *one* of the following:

-   Taking a screenshot and then cropping down to just your image.
    Please save as a PNG (`.png`) file.
    
    Windows
    :   1.  Hit the windows key on your keyboard (looks like Microsoft logo)
        2.  Type "snipping tool" into the search bar
        3.  Open the snipping tool application & click "New" 
        4.  Drag the cursor around the area you want to take a snapshot of
        5.  Save the snip as a PNG
    
    OS X
    :   1.  Press the Shift + Command + 4 key combination (command looks like ⌘)
        2.  Drag the cursor around the area you want to take a snapshot of
        3.  The screenshot appears on the Desktop: rename it

-   Use the following code immediately before the `turtle.mainloop()` line to save a Postrcript file (`.ps`):
    
    ````python
    turtle.getscreen().getcanvas().postscript(file="930-OLS-mst3k-mst3k.ps", colormode="color")
    ````
    
    Note: Poststript was a precursor to PDF, and some machines can't display it properly.
    If you can't look at your image; don't worry.

Submit either a `.png` file or a `.ps` file to the `lab03-turtle` on [CS 1110 submission page](https://archimedes.cs.virginia.edu/cs1110/).
To be entered into the competition, your file name must look like:

        time-room-id1-id2.png

For example, if Craig Dill and Luther Tychonievich were paired in the 9:30am Olsson 001 lab, we'd submit

        930-OLS-lat7h-cd9au.png

Use 930, 1100, 1230, 200, 330, 500, or 630
along with either OLS, MEC, or RICE for your lab location
so we can keep all the labs together and we know who you are!

Then put in BOTH partners' computing IDs, separated by dashes.

Images will be displayed (anonymously).
The staff will pick our favorite images, with prizes awarded next lab!

## Code

Go to the [CS 1110 submission page](https://archimedes.cs.virginia.edu/cs1110/) and submit your code under the `lab03-tutle` entry.
Most submissions will require a particular file name, but this one is noted as `*.py` meaning you may submit any file ending in `py`.

We are more interested in verify that the submission system works for you than in your actual code (this will change in later labs).
To help with this verification, both partners should submit code (it can be the same file) and report any problems to your lab TAs.
