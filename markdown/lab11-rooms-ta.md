---
title: "Lab 11: Counting Rooms Again - TA Notes"
...


# Paring

Explain that the final project will be paired.
You have full authority to pair students however you wish.
They can't submit their own pairings; only you can.
We recommend 

- in lab pairs
- in-grading-group pairs (possibly by changing grading groups)
- if you need a group of 3, pick 3 solid students and ask them to do more than other teams do. A trio including 1 or more struggling students tends to go very poorly

Record parings on the [project partner site](https://archimedes.cs.virginia.edu/cs1110/partners.php) on archimedes.
If needed, also adjust [grading groups](https://archimedes.cs.virginia.edu/cs1110/gradegroup.php) to keep partners in the same grading group.

# Review the Task

Remind the students about lab 2, which had the goal of telling a robot how to count the number of rooms in a grid.

Explain that this lab has some example lab 2 submissions included, selected in part to show a diversity of solution designs. They might not all be equally useful or even correct. However, reading them is advised before coding.

# Overview `robot.py`

Walk though the example code on the student site, reproduced below

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

Show what happens if you change robot constructors or directions.
Show that the robot will crash if you change the room constructor to

````python
r = robot.Robot(1, (0,1))
````

Ask if they have any questions about `robot` before they begin.

## PyGame?

One goal of this lab is to make sure pygame is still working.
If something does not work, you might need to revisit [lab 1](lab01-installing.html) to install everything.

# Example solutions to the last task

## Recursion by Room

````python
seen = set()
path = []
def explore(pt):
    seen.add(pt)
    path.append(pt)
    n = (pt[0]-1,pt[1])
    if n not in seen and r.check_left():
        r.left()
        explore(n)
    n = (pt[0]+1,pt[1])
    if n not in seen and r.check_right():
        r.right()
        explore(n)
    n = (pt[0],pt[1]-1)
    if n not in seen and r.check_up():
        r.up()
        explore(n)
    n = (pt[0],pt[1]+1)
    if n not in seen and r.check_down():
        r.down()
        explore(n)
    path.pop()
    if len(path):
        prev = path[-1]
        if prev[0] < pt[0]: r.left()
        elif prev[0] > pt[0]: r.right()
        elif prev[1] < pt[1]: r.up()
        else: r.down()

explore((0,0))
r.say(len(seen))
````

## Recursion by Door

````python
def door(c, d):
    global count, visited
    to = (
        c[0] + (1 if d == 'r' else -1 if d == 'l' else 0), 
        c[1] + (1 if d == 'd' else -1 if d == 'u' else 0)
    )
    if to not in visited:
        if d == 'l' and not r.cl(): return
        if d == 'r' and not r.cr(): return
        if d == 'u' and not r.cu(): return
        if d == 'd' and not r.cd(): return
        if d == 'r': r.r()
        if d == 'l': r.l()
        if d == 'u': r.u()
        if d == 'd': r.d()
        visited.append(to)
        count += 1
        door(to, 'l')
        door(to, 'r')
        door(to, 'u')
        door(to, 'd')
        if d == 'r': r.l()
        if d == 'l': r.r()
        if d == 'u': r.d()
        if d == 'd': r.u()
        

visited = [(0,0)]
count = 1
door((0,0),'u')
door((0,0),'d')
door((0,0),'r')
door((0,0),'l')
r.say(count)
````

or, much shorter with metaprogramming,

````python
rev = {'r':'l','u':'d','l':'r','d':'u'}
def door(c, d):
    global count, visited
    to = (
        c[0] + (1 if d == 'r' else -1 if d == 'l' else 0), 
        c[1] + (1 if d == 'd' else -1 if d == 'u' else 0)
    )
    if to not in visited:
        if not r.__getattribute__('c'+d)(): return
        r.__getattribute__(d)()
        visited.append(to)
        count += 1
        for d2 in 'lrud': door(to, d2)
        r.__getattribute__(rev[d])()
        

visited = [(0,0)]
count = 1
for d2 in 'lrud': door((0,0), d2)
r.say(count)
````

## Shortest path queue

Note: this often crashes as it does not know a safe way to get from room to room

````python
unvisited = [(0,0)]
visited = []
here = (0,0)
while len(unvisited) > 0 and r.ok:
    visit = unvisited.pop()
    visited.append(visit)
    while here[0] < visit[0]:
        here = (here[0]+1, here[1])
        r.r() 
    while here[1] < visit[1]:
        here = (here[0], here[1]+1)
        r.d()
    while here[0] < visit[0]:
        here = (here[0]-1, here[1])
        r.l()
    while here[1] > visit[1]:
        here = (here[0], here[1]-1)
        r.u()
    if r.cr() and (here[0]+1, here[1]) not in visited:
        unvisited.append((here[0]+1, here[1]))
    if r.cl() and (here[0]-1, here[1]) not in visited:
        unvisited.append((here[0]-1, here[1]))
    if r.cd() and (here[0], here[1]+1) not in visited:
        unvisited.append((here[0], here[1]+1))
    if r.cu() and (here[0], here[1]-1) not in visited:
        unvisited.append((here[0], here[1]-1))
r.say(len(visited))
````

## Backtrace queue


````python
def adjacent(here, goal):
    if here[0] == goal[0] and here[1]+1 == goal[1]: return 'd'
    if here[0] == goal[0] and here[1]-1 == goal[1]: return 'u'
    if here[0]+1 == goal[0] and here[1] == goal[1]: return 'r'
    if here[0]-1 == goal[0] and here[1] == goal[1]: return 'l'
    return here == goal
def go(here, step, record=True):
    if step == 'l': 
        r.l()
        if record: trail.append('r')
        return here[0]-1, here[1]
    if step == 'r': 
        r.r()
        if record: trail.append('l')
        return here[0]+1, here[1]
    if step == 'u': 
        r.u()
        if record: trail.append('d')
        return here[0], here[1]-1
    if step == 'd': 
        r.d()
        if record: trail.append('u')
        return here[0], here[1]+1
def goback(here):
    return go(here, trail.pop(), False)

unvisited = [(0,0)]
trail = []
visited = []
here = (0,0)
while len(unvisited) > 0 and r.ok:
    visit = unvisited.pop()
    if visit in visited: continue
    x = adjacent(here, visit)
    while not x:
        here = goback(here)
        x = adjacent(here, visit)
    if type(x) is str:
        here = go(here, x)
    visited.append(visit)
    
    if (here[0]+1, here[1]) not in visited and r.cr():
        unvisited.append((here[0]+1, here[1]))
    if (here[0]-1, here[1]) not in visited and r.cl():
        unvisited.append((here[0]-1, here[1]))
    if (here[0], here[1]+1) not in visited and r.cd():
        unvisited.append((here[0], here[1]+1))
    if (here[0], here[1]-1) not in visited and r.cu():
        unvisited.append((here[0], here[1]-1))

r.say(len(visited))
````
