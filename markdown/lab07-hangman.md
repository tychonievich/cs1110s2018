---
title: "Lab 7: Hangman"
...

# About this lab

The goal of this lab is to introduce loops and how to create them from non-loop repetitive code.
As such, you'll be asked to implement *two* versions of the programs it contains:
one that uses no loops, and another that does use loops.
For your best learning, implement them in that order: non-loop first, then loop.

[Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) is a paper and pencil guessing game which we will mostly replicate in this lab.


# Loopless version

First, make a loopless hangman in a file called `hangman_if.py`, which you will submit to [the submission system](https://archimedes.cs.virginia.edu/cs1110/).

## Design

We need to keep track of two basic elements:

-   The word the user is trying to guess
-   The portion of the word they have guessed
-   How the two relate to each other

We can relate the two by storing the letters next to each other: the key, then a blank or their guess;
thus if the word is `jellied`, we'd start with `j_e_l_l_i_e_d_`;
after they guess `e` and `d` it would be `j_eel_l_i_eedd`;
etc.

We'll then proceed as follows:

1.  ask them a letter
2.  adjust the string, replacing letter-blank pairs with letter-letter pairs
3.  display every other letter of the word so they see only the blanks and letters they guessed

We'll write that code, copy-and-paste it a bunch of times, and we'll have basic Hangman.

## Implementation

Write the code to do one step of hangman:
as them the word to use, ask for one letter, and show word with blanks and that one letter.

### Initialization

Ask the user for the word.  Make it all lower case, as hangman is traditionally case-insensitive.

Put an underscore after every letter.
The `join` method of strings will do most of this;
for example, try running `"Wow!".join("amazing")`{.python} and printing the result.
What do you have to do to change this to insert underscores?
One underscore will still be missing, but you can add it in another way you've been using for more than a month now...

### Ask them a letter

You know how to do this...

### Adjust the string

The `replace` method of strings can do this; if they guess `e`, replace `e_` with `ee`.

### Display the word

We've already talked about
indexing (e.g., `"welcome"[1]`{.python})
and slicing (e.g., `"welcome"[1:-1]`{.python});
there's also an *extended slice* that skips some letters.
The syntax is `s[i:j:k]`{.python}, which is the same as `s[i:j]`{.python} except it only shows every `k`th letter.
Thus, `"things are getting strange"[2:-3:3]`{.python} is `isrgtgt`:
we start at index 2: "th`ings are getting strange`";
end before the third to last: "th`ings are getting stra`nge";
and include every third character: "th`i`ng`s` a`r`e `g`et`t`in`g` s`t`range" → `isrgtgt`.

How can you use the extended slice to, given `word = "j_eel_l_i_eedd"`, display `_e___ed`?

### Example

At this point your program should contain no loops and be able to run like this:

````
Enter a word or phrase: jellied
The word to guess: _______
Guess a letter: e
The word to guess: _e___e_
````

or

````
Enter a word or phrase: keeping the lights on
The word to guess: _____________________
Guess a letter: n
The word to guess: _____n______________n
````


## Repetition

Since we are not yet using loops, to ask for several letters we copy-paste

### Basic Copies

Make ten copies of the guess-and-display code, one after another.

````
Enter a word or phrase: fun
The word to guess: ___
Guess a letter: n
The word to guess: __n
Guess a letter: e
The word to guess: __n
Guess a letter: f
The word to guess: f_n
Guess a letter: i
The word to guess: f_n
Guess a letter: a
The word to guess: f_n
Guess a letter: u
The word to guess: fun
Guess a letter: f
The word to guess: fun
Guess a letter: x
The word to guess: fun
Guess a letter: z
The word to guess: fun
Guess a letter: i
The word to guess: fun
````

### Guarded copies

Change the code so that you don't display the question and answer again after there are no more `_` in the text.
This can be done with one `if` statement around each step, conceptually like

````python
if not done:
    ask, update, and display

if not done:
    ask, update, and display

if not done:
    ask, update, and display

...
````

or with nested `if`s:

````python
if not done:
    ask, update, and display

    if not done:
        ask, update, and display

        if not done:
            ask, update, and display

            ...
````

Either way, you should now be able to run the game and see

````
Enter a word or phrase: fun
The word to guess: ___
Guess a letter: n
The word to guess: __n
Guess a letter: e
The word to guess: __n
Guess a letter: f
The word to guess: f_n
Guess a letter: i
The word to guess: f_n
Guess a letter: a
The word to guess: f_n
Guess a letter: u
The word to guess: fun
````

# Using `while`

Make a copy of the file `hangman_if.py` in `hangman_while.py`.
Change it to use a `while` loop instead of a lot of repeated `if` statements.

In general, the pattern for doing this is

1.  identify one copy of the code that repeats
1.  indent it and add `while ...:` in front of the indentation
1.  delete the other copies
1.  determine the right boolean expression to put in place of the `...`
2.  delete all the other repeated copies

However, since we already have repeated `if`s, a simpler process will work:

1.  replace the first of the repeated `if`s with `while`
2.  delete all the other repeated `if`s

## Test it

The program `hangman_while.py` should work in all cases where `hangman_if.py` works,
but also allow guessing text that has a whole lot of letters in it.

# Extensions

Try adding the following extensions to either copy of your game.

## Better end-game

At the end, don't show "The word to guess: ..."; 
instead, show either something like "It was ...; you win!"
or "You lose! You guessed ..., and the answer was ...".
You might want to try to line up the guess and the answer using some extra spaces...

In `hangman_if.py` this can be done with just one `if`/`else`, judiciously placed, or with one in each case.
In `hangman_while.py`, adding a variable to count guesses is preferable, using an `and` in the `while`'s guard condition, like

````python
while still_have_underscores and guesses < some_limit:
    ....
````

````
Enter a word or phrase: impossible to guess with so few letters
The word to guess: _______________________________________
Guess a letter: t
The word to guess: ___________t__________t___________tt___
Guess a letter: e
The word to guess: _________e_t____e_____t______e___ette__
Guess a letter: s
The word to guess: ____ss___e_t____ess___t__s___e___ette_s
Guess a letter: h
The word to guess: ____ss___e_t____ess___th_s___e___ette_s
Guess a letter: w
The word to guess: ____ss___e_t____ess_w_th_s___ew__ette_s
Guess a letter: f
The word to guess: ____ss___e_t____ess_w_th_s__few__ette_s
Guess a letter: i
The word to guess: i___ssi__e_t____ess_with_s__few__ette_s
Guess a letter: m
The word to guess: im__ssi__e_t____ess_with_s__few__ette_s
Guess a letter: p
The word to guess: imp_ssi__e_t____ess_with_s__few__ette_s
Guess a letter: o
You lose! 
You guessed    "impossi__e_to___ess_with_so_few__ette_s"
The answer was "impossible to guess with so few letters"
````

````
Enter a word or phrase: fun
The word to guess: ___
Guess a letter: n
The word to guess: __n
Guess a letter: e
The word to guess: __n
Guess a letter: f
The word to guess: f_n
Guess a letter: i
The word to guess: f_n
Guess a letter: a
The word to guess: f_n
Guess a letter: u
You win! The answer was "fun"
````

## Pre-guessing spaces

Return spaces back to spaces (not underscores) before they start guessing.

````
Enter a word or phrase: impossible to guess with so few letters
The word to guess: __________ __ _____ ____ __ ___ _______
Guess a letter: t                                  
The word to guess: __________ t_ _____ __t_ __ ___ __tt___
Guess a letter: e                                  
The word to guess: _________e t_ __e__ __t_ __ _e_ _ette__
Guess a letter: s                                  
The word to guess: ____ss___e t_ __ess __t_ s_ _e_ _ette_s
Guess a letter: h                                  
The word to guess: ____ss___e t_ __ess __th s_ _e_ _ette_s
Guess a letter: w                                  
The word to guess: ____ss___e t_ __ess w_th s_ _ew _ette_s
Guess a letter: f                                  
The word to guess: ____ss___e t_ __ess w_th s_ few _ette_s
Guess a letter: i                                  
The word to guess: i___ssi__e t_ __ess with s_ few _ette_s
Guess a letter: m                                  
The word to guess: im__ssi__e t_ __ess with s_ few _ette_s
Guess a letter: p                                  
The word to guess: imp_ssi__e t_ __ess with s_ few _ette_s
Guess a letter: o
You lose! 
You guessed    "impossi__e to __ess with so few _ette_s"
The answer was "impossible to guess with so few letters"
````

You might also want to pre-guess other common non-letters, such as `,`, `.`, `!`, `-`, etc.

## Counting failures

Make a variable that counts how many guesses they made that did *not* change the answer.
This involves coming up with an `if`-statement that detects if their guess didn't change the answer and increasing the count variable inside it.

````
Enter a phrase: fun
Phrase to guess: ___
Guess a letter:  n
There is a 'n'!
Phrase to guess: __n
Guess a letter:  e
Nope; that's mistake number 1
Phrase to guess: __n
Guess a letter:  f
There is a 'f'!
Phrase to guess: f_n
Guess a letter:  i
Nope; that's mistake number 2
Phrase to guess: f_n
Guess a letter:  f
Nope; that's mistake number 3
Phrase to guess: f_n
Guess a letter:  a
Nope; that's mistake number 4
Phrase to guess: f_n
Guess a letter:  u
There is a 'u'!
You win!
The answer was "fun"
````

Then stop accepting guesses once they have six failures, even if they have not made 10 guesses yet.
This can be done by modifying the conditions of some `if`s you already have...

Then, since there are only 26 letters and they only get 6 bad guesses, 32 guesses will be enough every time...
meaning to do this in `hangman_if.py` you'll need 32 copies of the code instead of 10.


````
Enter a phrase: if-statements, repeated, are a bit like "while" loops: our next topic!
Phrase to guess: __-__________, ________, ___ _ ___ ____ "_____" _____: ___ ____ _____!
Guess a letter:  e
There is a 'e'!
Phrase to guess: __-____e_e___, _e_e__e_, __e _ ___ ___e "____e" _____: ___ _e__ _____!
Guess a letter:  t
There is a 't'!
Phrase to guess: __-_t_te_e_t_, _e_e_te_, __e _ __t ___e "____e" _____: ___ _e_t t____!
Guess a letter:  i
There is a 'i'!
Phrase to guess: i_-_t_te_e_t_, _e_e_te_, __e _ _it _i_e "__i_e" _____: ___ _e_t t__i_!
Guess a letter:  o
There is a 'o'!
Phrase to guess: i_-_t_te_e_t_, _e_e_te_, __e _ _it _i_e "__i_e" _oo__: o__ _e_t to_i_!
Guess a letter:  n
There is a 'n'!
Phrase to guess: i_-_t_te_ent_, _e_e_te_, __e _ _it _i_e "__i_e" _oo__: o__ ne_t to_i_!
Guess a letter:  r
There is a 'r'!
Phrase to guess: i_-_t_te_ent_, re_e_te_, _re _ _it _i_e "__i_e" _oo__: o_r ne_t to_i_!
Guess a letter:  h
There is a 'h'!
Phrase to guess: i_-_t_te_ent_, re_e_te_, _re _ _it _i_e "_hi_e" _oo__: o_r ne_t to_i_!
Guess a letter:  s
There is a 's'!
Phrase to guess: i_-st_te_ents, re_e_te_, _re _ _it _i_e "_hi_e" _oo_s: o_r ne_t to_i_!
Guess a letter:  f
There is a 'f'!
Phrase to guess: if-st_te_ents, re_e_te_, _re _ _it _i_e "_hi_e" _oo_s: o_r ne_t to_i_!
Guess a letter:  j
Nope; that's mistake number 1
Phrase to guess: if-st_te_ents, re_e_te_, _re _ _it _i_e "_hi_e" _oo_s: o_r ne_t to_i_!
Guess a letter:  l
There is a 'l'!
Phrase to guess: if-st_te_ents, re_e_te_, _re _ _it li_e "_hile" loo_s: o_r ne_t to_i_!
Guess a letter:  z
Nope; that's mistake number 2
Phrase to guess: if-st_te_ents, re_e_te_, _re _ _it li_e "_hile" loo_s: o_r ne_t to_i_!
Guess a letter:  x
There is a 'x'!
Phrase to guess: if-st_te_ents, re_e_te_, _re _ _it li_e "_hile" loo_s: o_r next to_i_!
Guess a letter:  u
There is a 'u'!
Phrase to guess: if-st_te_ents, re_e_te_, _re _ _it li_e "_hile" loo_s: our next to_i_!
Guess a letter:  a
There is a 'a'!
Phrase to guess: if-state_ents, re_eate_, are a _it li_e "_hile" loo_s: our next to_i_!
Guess a letter:  m
There is a 'm'!
Phrase to guess: if-statements, re_eate_, are a _it li_e "_hile" loo_s: our next to_i_!
Guess a letter:  w
There is a 'w'!
Phrase to guess: if-statements, re_eate_, are a _it li_e "while" loo_s: our next to_i_!
Guess a letter:  f
Nope; that's mistake number 3
Phrase to guess: if-statements, re_eate_, are a _it li_e "while" loo_s: our next to_i_!
Guess a letter:  b
There is a 'b'!
Phrase to guess: if-statements, re_eate_, are a bit li_e "while" loo_s: our next to_i_!
Guess a letter:  q
Nope; that's mistake number 4
Phrase to guess: if-statements, re_eate_, are a bit li_e "while" loo_s: our next to_i_!
Guess a letter:  p
There is a 'p'!
Phrase to guess: if-statements, repeate_, are a bit li_e "while" loops: our next topi_!
Guess a letter:  d
There is a 'd'!
Phrase to guess: if-statements, repeated, are a bit li_e "while" loops: our next topi_!
Guess a letter:  k
There is a 'k'!
Phrase to guess: if-statements, repeated, are a bit like "while" loops: our next topi_!
Guess a letter:  c
There is a 'c'!
You win!
The answer was "if-statements, repeated, are a bit like "while" loops: our next topic!"
````
