---
title: "Lab 11: Counting Rooms Again"
...


<style> 
.hidden { display: none; }
.hide-header { display: block; margin: 0ex -1ex; padding: 0ex 1ex; border-bottom: thin solid black; }
</style>
<script>
function toggle(element) {
    var s = element.nextElementSibling;
    if (s.classList.contains('hidden')) {
        s.classList.remove('hidden');
    } else {
        s.classList.add('hidden');
    }
}
</script>

![Picture of door space](/images/gridrooms.png)

In [lab 2](lab02-counting.html) you designed pseudocode for having a robot count the rooms in a grid.
In this lab you'll implement those algorithms in Python.

# Getting Started

Download [gamebox.py](files/gamebox.py) and [robot.py](files/robot.py) into the same folder.
Also in that folder, create a file named `rooms.py` and put inside it the following:

<table><tbody><tr><td width="30%">
````python
import robot
r = robot.Robot(4)
r.say("Ready!")
if r.check_north():
    r.west()
else:
    r.east()
    r.south()
r.say("Done!")
````
</td><td width="50%">
<img src="files/room.png" style="width:100%"/>
</td></tr></tbody></table>

If you run it, you should see a random set of rooms appear, with cyan doors and sandy/walnut/neon/eggplant walls and a robot represented as a stylized eyeball.

Press a key to dismiss the "`Ready!`" message; the robot will then execute the instructions given until it either reaches it's last instruction or crashes into a wall.

If you have any trouble running this, please contact a TA who can hopefully help fix your computer's setup.
We'll use the underlying `gamebox.py` and PyGame libraries for your final project, so getting them working now is important.

## The Robot's API

You can give the robot the following instructions

### Creation

A robot can be created with an integer parameter (1, 2, 3, or 4) corresponding to the 4 tasks we defined in [lab 2](lab02-counting.html).
It can also be created with a string representing the exact room layout.

````python
r = robot.Robot(2) # a random rectangle with the robot in the top-left corner
````

<table><tbody><tr><td width="50%">
````python
r = robot.Robot('''
x xxx x
xxx xxx
xxx xxx
x xxx x
''') # a specific room arrangement
````
</td><td width="50%">
<img src="files/room-str.png" style="width:100%"/>
</td></tr></tbody></table>

All robot creations allow an optional start position parameter, which should be a tuple with two integers:
the first is the column, the second the row, in which the robot should start (if possible; if that cell is not open, it will start at a random location instead).

````python
r = robot.Robot(2, (1, 2)) # rectangle, robot 1 square from left and 2 from top
````

### Looking around

The following methods all return `True` if the robot sees a door in the indicated direction, `False` otherwise.

-   `r.check_north()`, `r.check_up()`, `r.cn()`, `r.cu()`
-   `r.check_east()`, `r.check_right()`, `r.ce()`, `r.cr()`
-   `r.check_south()`, `r.check_down()`, `r.cs()`, `r.cd()`
-   `r.check_west()`, `r.check_left()`, `r.cw()`, `r.cl()`

### Moving

The following methods all move the robot one room in the indicated direction.

-   `r.north()`, `r.up()`, `r.n()`, `r.u()`
-   `r.east()`, `r.right()`, `r.e()`, `r.r()`
-   `r.south()`, `r.down()`, `r.s()`, `r.d()`
-   `r.west()`, `r.left()`, `r.w()`, `r.l()`

### Other

`r.say(x)` will display `x` in large red font and wait for a key press or mouse click before continuing.

`r.done()` will wait for the window to close (without this it will close once all other instructions are done).

# Your Task

Implement the same room-counting algorithms you defined in [lab 2](lab02-counting.html) as four functions in a file `rooms.py`.

We've included a few example pseudocode submissions from your peers for each of the four kinds of rooms.
In all cases, we value code that makes fewer moves while still resulting in the correct answer.

## Square from corner

Complete the following function

````python
def square():
    r = robot.Robot(1)
    ...
````

It should end with the robot `.say`ing the number of rooms in the grid.
The `robot.Robot(1)` invocation will place the robot in the top-left corner of a square grid of rooms.


<div style="border: thin solid black; padding: 1ex; border-radius:1ex; margin-top:1ex; ">
<strong class="hide-header" onclick="toggle(this)">Peer solutions from Lab 02 (click to toggle view)</strong><div>

    Let n= length of side 
    1. Input variable n; start x = 1
    2. Move east through (n-x)) doors
    3. Move south (n-x) doors
    4. Move west through (n-x) doors
    5. Move north through (n-(x+1)) doors
    6. Repeat steps 2 through 5; for each repetition use (x+1) instead x  
    7. Stop repeating when (n^2-1)=0

 

    WHILE there is a door to the east:
      Count width +1
      Go E
    Rooms = (width+1)^2

 

    count equals 1
    repeat:
        Check E to see if there is a door
        if there is a door, then go through the door and count + 1
        else do not repeat
    square count
    display count

 

    Observe if there is a door to the south
    If so; pass through
    If not; Stop
    Count door.

</div>
</div>

## Rectangle from corner

Complete the following function

````python
def rect():
    r = robot.Robot(2)
    ...
````

It should end with the robot `.say`ing the number of rooms in the grid.
The `robot.Robot(2)` invocation will place the robot in the top-left corner of a rectangular grid of rooms.

<div style="border: thin solid black; padding: 1ex; border-radius:1ex; margin-top:1ex; ">
<strong class="hide-header" onclick="toggle(this)">Peer solutions from Lab 02 (click to toggle view)</strong><div>

    First travel south 
    Count doors passed and add 1
    Stop when no door south
    Travel east 
    count doors passed and add 1
    stop when no door east
    Calculate: number of rooms = (doors tavelled south + 1) x (doors tarvelled east + 1)
    End

 

    Remember number of rooms you’ve been in while travelling S (n) 
    Check S
            If S has door go through it
    Otherwise
            Stop 
    Add rooms you’ve remembered to get variable n 
    Remember numbers of rooms you’ve been in after calculating variable n 
    Check E
            If has door go through it 
    Otherwise 
            Stop 
    Add rooms you’ve remembered to get variable m 
    Multiply variable n times m 

 

    WHILE there is a door to the east:
        Count width + 1
        Go E
     While there is a door to the south:
        Count length + 1
        Go S
    Rooms = (width+1)*(length+1)

 

    Start Count A at 1
    Repeat until Check E is false:
        Check E
           If E True    
           Go E
        Add 1 to Count
        Check E
    Start Count B at 1
    Repeat until Check S is false:
        Check S
        If S True
        Go S
        Add 1 to Count
        Check S
    Count A*Count B

</div></div>


## Rectangle from anywhere

Complete the following function

````python
def middle():
    r = robot.Robot(3)
    ...
````

It should end with the robot `.say`ing the number of rooms in the grid.
The `robot.Robot(3)` invocation will place the robot somewhere within a rectangular grid of rooms.

<div style="border: thin solid black; padding: 1ex; border-radius:1ex; margin-top:1ex; ">
<strong class="hide-header" onclick="toggle(this)">Peer solutions from Lab 02 (click to toggle view)</strong><div>

    Repeat:
        Check E
            If door: Go E
            If no door: Check S
                Go S 
    Multiply number of E moves times number of S moves to get dimensions of rectangle

 

    Repeat until Check N is false:
        Check N
        If N True
        Go N
        Check N
    Repeat until Check W is false:
        Check W
        If W True
        Go W
    Start Count A at 1
    Repeat until Check E is false:
        Check E
        If E True
        Go E
        Add 1 to Count
    Start Count B at 1
    Repeat until Check S is false:
        Check S
        If S True
        Go S
        Add 1 to Count
    Count A*Count B

 

    Let n = length 
    Let m= width
    1. Input variable n; start x = 1
    2. Move east through (n-x)) doors
    3. Move south (m-x) doors
    4. Move west through (n-x) doors
    5. Move north through (m-(x+1)) doors
    6. Move east through (n-3) doors
    7. Repeat steps 2 through 5; for each repetition use (x+1) instead x  
    8. Stop repeating when(nm-1)=0

 

    Travel north until no door north
    Travel west until no door west
    First travel south 
    Count doors passed and add 1
    Stop when no door south
    Travel east 
    count doors passed and add 1
    stop when no door east
    Calculate: number of rooms = (doors tavelled south + 1) x (doors tarvelled east + 1)
    End

</div></div>

## Random set of rooms

Complete the following function

````python
def middle():
    r = robot.Robot(4)
    ...
````

It should end with the robot `.say`ing the number of rooms in the grid.
The `robot.Robot(4)` invocation will place the robot somewhere within some set of connected rooms

Design and implement a solution to this problem; it's not simple, so don't be worried if you find it challenging.
Some ideas to consider:

-   If you (the human writing this code) were in the maze and asked to count rooms, you'd probably want to do both of the following:
    -   mark rooms so you know you've already counted them
    -   mark your path so you can find your way back to rooms you passed without entering
-   Rooms aren't stored as data you can interact with, but you can fake it:
    -   A room can be identified by a pair of numbers, like `(1, 3)`.
    -   You can pick any arbitrary name for the first room and compute all others relative to that.
    -   A `list` of rooms (e.g. `[(0, 0), (1, 0), (1, 1), (1, 2)]`{.python} can represent a path; so can a `list` of directions (e.g., `['e', 'n', 'n']`{.python})
    -   A `set` or `list` of rooms can represent the set you've marked
    -   If you need different markings in each room, a `dict` can work well for that (e.g., `{(1, 3): "unchecked: north, west"}`{.python})

<div style="border: thin solid black; padding: 1ex; border-radius:1ex; margin-top:1ex; ">
<strong class="hide-header" onclick="toggle(this)">Example pseudocode solutions (click to toggle view)</strong><div>

    When you look at a door
        if the room on the other side has not been visited
            enter that room
            mark it as visited
            add one to the count
            look at each of its doors
            return back through the door you entered

 

    Let n = set containing the first room
    repeat until n is empty
        remove a room from n
        move to that room
        add one to the count
        add all of the unvisited neighbors of that room to n

 

    https://en.wikipedia.org/wiki/Flood_fill has a lot of pseudocode and seems related; just replace coloring with counting

    
</div></div>


## Submission

**At least one partner** should submit one .py file named `rooms.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **all partners' ids** in comments at the top of the file.
