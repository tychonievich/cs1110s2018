---
title: "Lab 4: Madlibs"
...

# Participation

Labs are graded primarily on presence and participation, not product.
Be there, participate, and profit.

# Turtle art gallery

We've posted <a href="turtleart/" target="_blank">the turtle art submissions</a>!

# Pairing

For this and all subsequent labs, you will work in pairs.

# Survey

As part of our ongoing effort to try to improve CS 1110, we have a group of researchers looking into how labs work and how they might work better.
They have a survey they'd like you to fill out:

<div style="display:table;margin: 1em auto;font-size:150%; padding:1ex; border:thin solid #e3e3e3; border-radius:4px; background:#f5f5f5;-webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05); -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05); box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);">[Take the Survey](survey.html)</div>

# Recitation

The TAs will do a quick review lesson on data types before moving on to
the in-lab activity.

# Building a Madlib

Madlibs work as follows:

1.  Pick a phrase, and replace key words with what kind of word they are.
    For example, you might decide your phrase is
    
    > When I was younger I wanted to be a *profession1*. I pictured myself at a *event1*.  One person says "I'm a *profession2*." Another says "I'm a *profession3*, just back from *where profession3 works*."  I say "I'm a *profession1*!" With a gasp, everyone turns to me.  "You're a *profession1*?  Tell us more!"
    >
    > Then I met you. Now I know that all *profession1*s do is *task1* and no one cares.  Thank you for showing me the true way.
    
    You can pick any phrase you want.
    Often stranger phrases with more key words missing are more interested.
    
1.  Without showing the user the phrase, ask the user for the words you left out.
    For example, you might ask
    
        A profession: phone booth sterilizer
        Something people do: make money
        Another profession: juggler
        A third profession: astronaut
        A place: the Gobi desert
        A kind of event: bluegrass jam session
        
1.  Display the phrase, replacing the key words with the words the user supplied.

    > When I was younger I wanted to be a phone booth sterilizer. I pictured myself at a bluegrass jam session.  One person says "I'm a juggler." Another says "I'm a astronaut, just back from the Gobi desert."  I say "I'm a phone booth sterilizer!" With a gasp, everyone turns to me.  "You're a phone booth sterilizer?  Tell us more!"
    >
    > Then I met you. Now I know that all phone booth sterilizers do is make money and no one cares.  Thank you for showing me the true way.
   
Your goal in this lab is to work with a partner write a program that performs a madlab,
called `madlib.py`.
The program will prompt the user for all the words, then display the phrase.
The phrase should use at least one of the words the user types in more than once place.

For this assignment, we are not auto-grading your results.
So feel free to be creative with the phrase! (Within reason, of course...)

We will, however, look at how you wrote the code.
Specifically, how you solved the problem.

-   You must write at least one function as part of your solution
-   Ideally you'd have several, such as
    1.  A "main" function like
        ````python
        def madlib():
            """asks for user input and returns the modified string of the full phrase"""
        ````
        which would make repeated use of
    1.  a "helper" function like
        ````python
        def replace_with(prompt, text_so_far, placeholder):
            """returns new text replacing all placeholders with user response to prompt"""
        ````
-   Other designs are fine, so long as they make reasonable use of functions.

Remember to good variable names and comments to help make your code easy to read!

## Submission

**Each partner** should submit one .py file named `madlib.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **both partners' ids** in comments at the top of the file.

