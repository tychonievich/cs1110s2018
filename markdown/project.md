---
title: "Final Project: game.py"
...

# Overview

Your task is to use PyGame and gamebox to create in interesting game with a partner.
Unlike other assignments,

-   You should work with one (1) partner for the entirety of this assignment
    -   These will be handled in lab on 12 April (or in an adjacent class for 1111)
-   This assignment is worth more points (see [the syllabus](syllabus.html) for details)
-   You are expected to define the details of this assignment yourselves
-   We'll check your progress (based on checkpoint archimedes submissions) several times; lack of progress will result reduced final grades.

# Partnering

For logistical reasons, partners will generally be assigned within a single lab section by TAs with little input from students.
Your partner, once entered by a TA, will show up near the bottom of the submission site under "Project".

<!--
You can submit a partner evaluation using [this google form](https://docs.google.com/forms/d/e/1FAIpQLSclqTmYTrGNerC158UMlN5A2jgbA7xquFpAlnQ4p_F1MGlOAw/viewform?usp=sf_link).
-->


## Working together

To the degree possible, please plan to work together, rather than each working independently and combining code later.
Working together can result in fewer bugs and better code.

If you have problems with your partner, first bring them up to your partner and then to your instructor.
We'll do our best to help things run smoothly.

We will also ask for each student to submit a partner evaluation near the end of your time together.

# Designing your game

Each game is expected to be unique; we do not tell you what to implement.
However, we do provide some guidelines to keep the scope appropriate:

## Required Features

Your game should look like a game someone might want to play (i.e., probably not just a lot of colored boxes).
You must include all of the following:

User Input
:   Either through the keyboard or mouse, you should have appropriate and working user controls.

Graphics/Images
:   You should use some appropriate images in your game.

Start Screen
:   Game has a start screen with game name, student names (and IDs), and basic game instructions.

Small Enough Window
:   Some graders don't have large screens; your game window may not be larger than `gamebox.Camera(800, 600)`{.python} (it may be smaller...)

## Optional Features

You must include at least four of the following:

Animation
:   Use a sprite sheet to have an animated character.

Enemies
:   Have characters that can hinder the player character from accomplishing the goal.
    For full credit, enemies must move.

Collectibles
:   Add collectables (i.e. coins) to the level that can be picked up by the character with a counter that appears on the screen.
   
    We typically get many "does *X* count as a collectible?" questions.
    Standard collectibles exist in the environment, vanish when you touch them, and give you some benefit from collecting them.
    
Scrolling level
:   Make the level much larger than the screen (You may need to add a background image to make this more obvious.)

Timer
:   Have a countdown (or count up) timer for your game.
    For full points, this needs to make some kind of sense within the context of the game itself.

Health meter
:   Have a health meter that changes as you hit enemies/obstacles.
    It's only a *health* meter if it getting to 0 results in loss of game (or re-spawning at a save point).

Two players simultaneously
:   Two players who are able to interact with one another within the game.

Multiple levels
:   Make several distinct levels that the player can advance through.
    If you do this, make it clear that there are several levels so that your grader knows to try to reach more than one.

Save points
:   When the player reaches some milestone, future failures cause the player to respawn at that save point
    instead of having to start over.

Inter-session progress
:   Have your game write some information to a file when it closes, and use that to update the next play.
    For example, you could have a cumulative high-score chart; a "save game" option;
    or even log what the player does and make "instant replays" or the like.

Something More
:   Want to add another feature, not listed above, and have it count?
    Describe it in your game checkpoints and see if your grader thinks it is worth points!
    Note, it will typically need to be at least as programming-complicated as the examples above...

## Other Constraints

It is *not* sufficient to base your game on our examples.
The example code is designed to teach concepts and give code snippets you can use,
but your game should be significantly more than any of our examples.

# Game Ideas

Don't have a good game idea in mind?
See [Wikipedia's list of golden-age arcade games](https://en.wikipedia.org/wiki/Golden_age_of_arcade_video_games#List_of_popular_arcade_games) for many ideas.

# FAQ

Many questions of the form "how do I do *X*" are answered in [The Gamebox Docs](gamebox-summary.html) or [The Gamebox API](gamebox.html).
Others are added here as they come to our attention.

Why do my fast-moving objects pass through walls?
:   Because in a single frame they make it past the center of the wall, so `move_to_stop_overlapping` moves them out the wrong side.

    The simplest solution is making fatter obstacles (or fatter objects; if an object cannot move more than `min(obj.width, obj.height) / 2` pixels per frame, it cannot have this problem)
    
    A fancier solution is to use sub-frame physics. Essentially, your ticks function would then be something like
    
    ````
    the key handling code
    
    n = small integer
    for i in range(n):
        the moving and collisions code but with 1/nth speed

    the drawing code
    ````
    
    The most robust solution is to track which side of each obstacle you were last frame and which side this frame and if that changes, do something about it; doing this correctly is not simple, but the `overlap` method of boxes can help if you want to try.

How do I make a grid-movement-based game?
:   Pick a grid size $g$ and then only change $x$ and $y$ in increments of $g$.

I'm getting an error opening images
:   If the last line of the error contains the number 403, this means the website won't let Python access the image.
    
    If the last line of the error contains the text "SSL: CERTIFICATE_VERIFY_FAILED" and you are on OS X, this means you need to tell Python how to access encrypted webpages.
    Go to "Applications/Python\ 3.6/Install\ Certificates.command" on your hard-drive and double-click on it: a window should pop up and install the necessary certificates.
    
    If you get an error message that says "No video mode has been set", you need to create the `gamebox.Camera(w,h)`{.python} *before* you use `gamebox.from_image` or `gamebox.load_sprite_sheet`.
    
    If you have either `/` or `\\` in your file path, and it is not a URL beginning either `http://` or `https://`, then you need to instead move the file into your project directory (and uploaded it when you submit your game) and use a file path without slashes instead.
    
    If you have another error, check Piazza and if it is not described there, add a question so we can update this FAQ.

Can I use `robot.py` from Lab as part of my game?
:   No.

# Submission

You'll need to submit your code and any support files to Archimedes.
In addition to the final submission date of midnight, the last day of classes (not the last day of finals).
We will also check your progress with two intermediate checkpoints, each due midnight the day before a lab.
**Making steady progress every week** is a requirement for full credit on this assignment.

## Checkpoint 1

Should be a python file, named `game.py`, containing comments describing your game idea and how you will fill the optional requirements.  We also encourage starting the game code in that file as well.

This checkpoint is due at 5:00 AM Wednesday morning, and late submissions are *not* accepted. If you miss the checkpoint and would still like feedback, contact your grader in lab (or class for 1111).

## Checkpoint 2

Should be a the basics of a working game, in `game.py`, possibly with a few "it crashes if you do *X*"-type bugs or missing features.

This checkpoint is due at 5:00 AM Wednesday morning, and late submissions are *not* accepted. If you miss the checkpoint and would still like feedback, contact your grader in lab (or class for 1111).

## Final Submission

Should be the entire game.

This submission is due at 11:59 PM Tuesday night, and per university policy late submissions are *not* accepted.

## Uploading files beyond `game.py`

We accept all kinds of files in the submission, but note:

-   The game must be run by using a file named `game.py`; it may use other `.py` files too if you want (upload them too)
-   If you make your own graphics, level files, etc., upload those; but if you access them in your game by URL yo don't need to upload them
-   Don't upload copyrighted material unless you have rights to give it to us

At least one partner will need to submit your files each time you submit.
If more than one submit the same file name, the last submission of the group will be used.

