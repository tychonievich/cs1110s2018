---
title: "Lab 2: Counting Squares"
...

# Desktop Computers

We have not yet received accounts for students in labs that have desktop computers.
Sorry!
If you don't have a laptop, pair up with someone who does for this lab.

# Pairing

For this and all subsequent labs, after the logic group activity you will work in pairs.
You will need your computer, etc, for the paired part of lab.
For now, you may pick your own pair partner.
Later on we may assign you a partner for some labs and/or assignments.

We will use a model called "pair programming" in this class. There are a
few things to know about successful pairing under this model:

-   **2 minds, 1 focus**. If at any point the two of you are doing
    distinct things, such as each typing on your own computer or each
    looking at your own piece of paper, then you are not pairing
    properly.
    
-   **Driver and Navigator**. At any given point in time, one partner
    will be the "driver", controlling the keyboard, pencil, or other
    tool currently being used. The other will be the "navigator,"
    observing and commenting on the driver's actions.
    
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

# Grid of doors

![Picture of door space](/images/gridrooms.png)

For this lab we will be programming a robot that has been dropped into a
grid of square rooms. Each wall of each room has been painted a
different color: the **N**orth wall is **N**eon, the
**E**ast wall is **E**ggplant, the **S**outh wall is
**S**andy, and the **W**est wall is **W**allnut. Walls
between rooms have doors in them, but walls on the edge do not. All of
the doors are closed initially.

The robot knows how to

-   **Check N** (or **Check E**, or **S**, or **W**) to see if there is
    a door on that wall of its current room;
-   **Go N** (or **E** or **S** or **W**) to move one room over; and
-   Do basic math and remember numbers

If you ask it to Go through a wall that does not have a door, it isn't
smart enough to know it can't so it will walk into the wall and damage
itself.

We won't be super formal in this lab,
but to the degree you can we'd like to see you practice pseudocode, as discussed in class.

## Simple Square

Suppose the robot is dropped into a square grid of rooms and starts in
the north-west corner of the grid. Come up with an algorithm that the
robot can use to figure out how many rooms are in the grid.

Is there any size grid for which your algorithm does not work? How about
on a 1-by-1, or a 1000-by-1000?

In a 3-by-3 grid, how many times will the robot have to move through a
door to run your algorithm? How about a 4-by-4? An *n*-by-*n*?

Assume that we want to save on robot fuel. Can you make an algorithm
that uses fewer moves for the same size grid?

Once you have an algorithm you think is general (works for all size
squares) and efficient (uses few moves), type it up and save it in a
text file. You'll submit all your algorithms at the end. Include a
simple statement about how many moves it takes, “on an n-by-n grid the
robot moves through 2n+5 doors” or something like that.

## Simple Rectangular

Suppose the robot is dropped into a rectangular (not necessarily square)
grid of rooms and starts in the north-west corner of the grid. Come up
with an algorithm that the robot can use to figure out how many rooms
are in the grid.

Type it up and save it on the same text file as before, including a
description of the number of moves needed for an *n*-by-*m* grid. If
your square algorithm still works, you are welcome to submit it again for
rectangles.

## General Rectangular

Suppose the robot is dropped into a rectangular (not necessarily square)
grid of rooms and might start in any arbitrary room in the grid. Come up
with an algorithm that the robot can use to figure out how many rooms
are in the grid.

Type it up and save it in the same text file as before, including a
description of the number of number of moves your robot will make for an
*n*-by-*m* grid. Since this will probably depend on the starting
location of the robot, just tell us the biggest number you could see
(assuming the robot started in the worst possible room).

If one of your previous two algorithms still works, you are welcome to
submit it again for general rectangular.

## Stranger Grids

See how general you can make your algorithm. Can you get it to work on
diamond-shaped grids of rooms? Grids with more complicated outlines?
Grids where some rooms are missing in the middle? Grids where some walls
between two rooms that do exist don't have doors? Arbitrary mazes of
rooms?

Type it up and save it in the same text file as before. At the beginning
of the submission, include a description of the kinds of grids you think
it can handle.

We are not looking for any particular functionality in this step; if
you end up with just rectangles, that's fine, just submit a note to that effect in the form.

Once you have all 4 algorithms done, submit them all in this Google
Form:
[https://docs.google.com/forms/d/e/1FAIpQLSeT9gFo495zGUQCcUQ9nbSI8cQuhYxveWoIguDq78akKiFBsA/viewform?usp=sf_link](https://docs.google.com/forms/d/e/1FAIpQLSeT9gFo495zGUQCcUQ9nbSI8cQuhYxveWoIguDq78akKiFBsA/viewform?usp=sf_link).
Only one partner needs to submit!
