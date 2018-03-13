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

(see also this [pre-populated PythonTutor instance](http://pythontutor.com/visualize.html#code=def%20pair_swap_chunk%28chunk%29%3A%0A%20%20%20%20%22%22%22Swaps%20the%20order%20of%20letters%20in%20a%202-letter%20string%22%22%22%0A%20%20%20%20if%20len%28chunk%29%20%3C%202%3A%0A%20%20%20%20%20%20%20%20return%20chunk%0A%20%20%20%20return%20chunk%5B1%5D%20%2B%20chunk%5B0%5D%0A%0A%0Adef%20pair_swap%28text%29%3A%0A%20%20%20%20ans%20%3D%20''%0A%20%20%20%20for%20i%20in%20range%280,%20len%28text%29,%202%29%3A%0A%20%20%20%20%20%20%20%20chunk%20%3D%20text%5Bi%3Ai%2B2%5D%0A%20%20%20%20%20%20%20%20ans%20%2B%3D%20pair_swap_chunk%28chunk%29%0A%20%20%20%20return%20ans%0A%0Ap%20%3D%20'this%20is%20a%20test'%0Ae%20%3D%20pair_swap%28p%29&cumulative=false&heapPrimitives=true&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false))

Pair swap does not need a key, and it is its own inverse.
Other ciphers in this lab are more complicated...

# Contextualize

There's a reason we said "Code up at least two of the following ciphers."
Programming all 6 is unlikely to be doable by most pairs.
Depending on which one you start with, even doing 2 might be out of scope for lab.

Point out the Application section and encourage them to try it out after getting a cipher implemented.

