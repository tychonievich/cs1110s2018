---
title: "Lab 8: Crypto"
...


# Purpose of this lab

This lab has three goals

1.	Help them see cases where both `for element in thing:`{.python} and `for i in range(len(thing)):`{.python} are useful
2.	Have them write simple loops
3.	Provide an introduction to an important topic that we won't get to in lecture

# Pairing + Approach

If necessary in your lab, remind the students about good pairing:

1.	Two minds, one focus -- they should be working together
2.	Diver + Navigator roles, swapped from time to time

Also remind them that if you can't do something on paper, you can't tell the computer how to do it either.
Always start working off of the computer.

# Overview

Help them understand the example code on the student view of the lab:

````python
def encrypt_chunk(chunk, key):
    ...
    return transformed_version_of_chunk


def encrypt(plain_text, key):
    cipher_text = '' # accumulator pattern: start with no encrypted test
    for i in range(0, len(plain_text), chunk_size): # look one chunk at a time
        chunk = plain_text[i:i+chunk_size]          # all chunks the same size
        cipher_text += encrypt_chunk(chunk, key)    # the real work is in another function
    return cipher_text
````

Discuss how this works, and then show them a pair-swap encryption:

````python
def pair_swap_chunk(chunk):
    """Swaps the order of letters in a 2-letter string"""
    if len(chunk) < 2:
    	return chunk
    return chunk[1] + chunk[0]


def pair_swap(text):
    ans = ''
    for i in range(0, len(text), 2):
        chunk = text[i:i+2]
        ans += pair_swap_chunk(chunk)
    return ans
````

Pair swap does not need a key, and it is its own inverse.
Other ciphers in this lab are more complicated...

# Contextualize

There's a reason we said "Code up at least two of the following ciphers."
Programming all 6 is unlikely to be doable by most pairs.
Depending on which one you start with, even doing 2 might be out of scope for lab.

Point out the Application section and encourage them to try it out after getting a cipher implemented.

