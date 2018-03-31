---
title: "Lab 9: Debugging - TA Guide"
...

# Running the Lab

Encourage them to work in teams.  More than 2 is OK for this lab.

Review the debugging guide on the student site. Note: some instructors went over some of this in lecture, others did not, so their reaction to the review might vary.

Review the game strategy example on that site. Take questions to make sure they understand how to win at Nim.

Tell them they actually need to read the entire student page.  There is information there they will not be able to do the lab without.

Remind them that they should *either* fix all bugs *or* work until the end of lab; doing both is not required.

# The Bugs

The bugs I introduced are as follows,
listed in order of where they appear in the code.

## infinite loop

The `pow2` loop does not make progress.

incorrect                            fix
------------------------------------ ------------------------------------
`ans * 2`{.python}                   `ans *= 2`{.python} or `ans = ans * 2`{.python}


## Missing cast

The input for the number of marbles leaves the value as a string.

incorrect                                                           fix
-----------------------------------------------------------------   -----------------------------------------------------
`marbles = input("The number of marbles in the pile: ")`{.python}   `marbles = int(input("The number of marbles in the pile: "))`{.python}


## Incomplete input verification

The check on the player plays don't prevent non-positive numbers, and since the initial number is 0 this means the player never plays.

incorrect                           fix
----------------------------------  ---------------------------------------------
`while take > can_take`{.python}    `while take > can_take or take <= 0`{.python}


## Player can't lose

If the player has to take the last marble, the computer will instead refuse to accept any play
because `can_take` will be 0.

incorrect   fix
----------- ----------------------------------------
*missing*   `if can_take == 0:`{.python}
*missing*   `    can_take = 1`{.python}


## Off-by-one error

The computer's logic trys to get a power-of-two marbles.  It is supposed to try for one less than that.

incorrect                           fix
----------------------------------- -------------------------------------
`target = pow2(marbles)`{.python}   `target = pow2(marbles) - 1`{.python}


## Computer can cheat

The computer is allowed to take more marbles than it's supposed to.

incorrect               fix
----------------------- --------------------------------------------
`if take < 1:`{.python} `if take < 1 or take > marbles//2:`{.python}


