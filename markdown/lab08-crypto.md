---
title: "Lab 8: Cryptography"
...


# Overview

Cryptography is the art of hiding the meaning of a message in a way that the intended recipient can understand, but not anyone else.
Fully secure cryptography requires a a lot of detail-oriented nuance of implementation and some abstract algebra, but we can get some casual-level cryptography using what we know so far.

You'll write several functions in `crypto.py` that are suitable for casual encryption.
Feel free to use them to make messages harder for people who don't know the encryption to figure out,
but don't use them for truly sensitive information; every encryption on this page can be broken...

## Substitution ciphers

In this lab you'll create several functions for doing (and undoing) algorithms that belong to a class of encryption known as "substitution ciphers."
These encrypt by taking the input text (called the "plain text") in small chunks (such as a single character) and replacing each chunk with a new chunk to occupy the same position in the output text (called the "cipher text").
The inverse functions generally decrypt via in the same chunk-by-chunk process.
Many of the functions will also include a "key", some extra input that controls how they encrypt.

Most of the ciphers you write will have the following general form:

````python
def encrypt_chunk(chunk, key):
    ...
    return transformed_version_of_chunk


def encrypt(plain_text, key):
    cipher_text = '' # accumulator pattern: start with no encrypted test
    for i in range(0, len(plain_text), chunk_size): # look one chunk at a time
        chunk = plain_text[i:i+chunk_size]          # all chunks the same size
        cipher_text += encrypt_chunk(chunk, key)    # most work is in another function
    return cipher_text
````

The TAs will explain how this structure works for an example cipher at the beginning of lab.


# Ciphers to Implement

Code up at least two of the following ciphers.
Each should have two methods: one to encrypt, one to decrypt.
For example, if you do the shift cipher, write both `encrypt_shift` and `decrypt_shift`.

The examples below only describe encryption; to test decryption, note that it should always be the case that
`decrypt_X(encrypt_X(text, key), key) == text`{.python}.

Some ciphers depend on one another, or don't follow the same pattern as the others:

- Vigenère is an extension of Shift.
- Autokey is an extension of Vigenère. It is also by far the most secure cipher on this page.
- Ubbi Dubbi and Zombie Speak don't use the same loop structure to decrypt as they do to encrypt. They don't depend on one another, but Zombie Speak is somewhat harder.

## Shift cipher

One of the first documented ciphers was the Caesar Cipher, which adds 3 to each letter ("a" becomes "d", "b" becomes "e", etc.)
We'll generalize that to add an arbitrary integer *key*, not just 3.

Encryption should take an integer `key` and add `key` to every letter in `text`, wrapping around, so e.g. `a` + 1 = `b` and `z` + 1 = `a`.
Only change letters; leave non-letter characters as they are.

Example: `encrypt_shift("Caesar cipher", 3)`{.python} returns `"Fdhvdu flskhu"`{.python}; `encrypt_shift("Secret", 9)`{.python} returns `"Bnlanc"`{.python}


- - - - -
S + 9 = B
e + 9 = n
c + 9 = l
r + 9 = a
e + 9 = n
t + 9 = c
- - - - -


Suggestions:

-   You might want to try something like `'abcdefghijklmnopqrstuvwxyz'.find(character)` to convert characters to numbers.
-   Recall that `find` returns `-1` if it does not find the character, so you'll need to handle that specially for spaces and such to work.
-   How do you get capitalization to work?
-   You'll probably want to use `%` to deal with wrapping too-big keys.
    

## Vigenère cipher

Giovan Battista Bellaso modified the shift cipher by shifting different letters different amounts,
a method later misattributed to Blaise de Vigenère.
This cipher is much like the shift cipher, but instead of adding a single number to all letters,
a different number is added to each.
The numbers to add is selected by the letters of a key word;
if the key is `almost` then 

-   the first letter is shifted 0 (a = 0)
-   the second letter is shifted 11 (l = 11)
-   the third letter is shifted 12 (m = 12)
-   the fourth letter is shifted 14 (o = 14)
-   the fifth letter is shifted 18 (s = 18)
-   the sixth letter is shifted 19 (t = 19)
-   the seventh letter is shifted 0 (wrap around and use a = 0 again)
-   the eighth letter is shifted 11 (wrap around and use l = 11 again)
-   ...

For example, `encrypt_vignere("secret", "hi")`{.python} is going to be `"zmjzlb"`{.python}:

- - - - - - - - -
s + h = s + 7 = z
e + i = e + 8 = m
c + h = c + 7 = j
r + i = r + 8 = z
e + h = e + 7 = l
t + i = t + 8 = b
- - - - - - - - -

Suggestions:

-   Don't attempt Vigenère before trying Shift; it uses a lot of the same pieces, but in a more complicated way
-   There are two basic approaches: block-based and wrapping.
    -   Chunk-based
        -   We step a key-length chunk of the text at a time
        -   The chunk encryption loops through both key and text together
        -   This is chunk loop is easier by index (e.g., `for i in range(...):`{.python}) than by letter (e.g., `for c in text:`{.python)
        -   Note that the *last* chunk might be shorter than the key...
    - Wrapping
        -   We step 1 character at a time through both text and key, wrapping the key when we get to its end
        -   This is much easier if you loop in a way that knows the indices of letters (e.g., `for i in range(...):`{.python}) because that index can be used *both* for the text *and* for the key
        -   Wrapping indices is easily accomplished using the `%` operator: `key[i % len(key)]`{.python}.



## Autokey Cipher

Autokey ciphers use the message itself as part of the key.
The version we'll have you use is based on the Vigenère cipher, so you'll need to solve it first.

The principle is as follows:

-   Begin just as you would for Vigenère, shifting each letter by the corresponding letter of the key
-   When you get to the end of the key, instead of wrapping around use the plain text to extend the key

For example, `encrypt_autokey("secret", "hi")`{.python} is going to be `"zmuvgk"`{.python}:

- - - - - - -- - -
s + h = s +  7 = z
e + i = e +  8 = m
c + s = c + 18 = u
r + e = r +  4 = v
e + c = e +  2 = g
t + r = t + 17 = k
- - - - - - -- - -

Autokey ciphers are significantly harder to break than Vigenère ciphers, though the underlying word-based content still allows them to be cracked with effort.

Suggestions:

-   Encryption can be trivially implemented as `return encrypt_vignere(text, key+text)`{.python}. However, this approach does not work for decryption.
-   For decryption
    -   The first key-length letters can be decrypted as in Vigenère
    -   After that, the already decrypted letters are the new key


## Ubbi Dubbi

As documented by Wikipedia, Ubbi Dubbi works by leaving all consonants alone but preceding each vowel by `ub`; for example `encrypt_ubbi('hello')`{.python} is `'hubellubo'`{.python}.

This cipher has no key.

Suggestions:

-   Encryption is relatively easy; decryption is the hard part
-   Decrypting by removing all `ub`s does not work; it would make `rubber` encrypt to `rububbuber` decrypt to `rber`.
-   Decrypting is easiest by using a variable-step `while` loop, like
    
    ````python
    i = 0
    while i < len(cipher_text):
        if ...# check for ub + vowel
            ... # extract the vowel
            i += 3
        else:
            ... # extract the letter
            i += 1
    ````


## Permutation cipher

A permutation cipher does not change any letters, it simply rearranges them.
The pair-swap the TAs showed at the beginning of the lab is one example, but we want to do something more complicated.

For this cipher, the key will be a list (or tuple) of integers, which is a rearrangement of the integers in `range(n)` for some `n`.
The order tells us where each of the letters in a block get moved to.
For example, with the key `[1, 0, 3, 2, 4]` the string `abcde` would become `badce`.
We'll repeat the block-based approach for the whole string, first padding it with extra spaces to make it a multiple of the key length characters long.

For example, `encrypt_perm("now I, even I, would celebrate", [2,0,1,3])`{.python} will return `"wno  I,enve  I,wloude clreba te "`{.python}

Suggestions:

-   For encryption, the encrypted *k*th letter of each chunk is the `key[k]`th letter of the chunk's plain text.
-   For decryption, there are several options but one of the easiest is to create an inverse key and then use the encrypt function.
    -   If `k` is the key, then `i` is an inverse key if `i[k[x]] == x` for all `x`.
    -   For example, the inverse key of `[2, 0, 1, 3]` is `[1, 2, 0, 3]` and `decrypt_perm(x, [2,0,1,3])` is the same as `encrypt_perm(x, [1,2,0,3])`.


## Zombie Speak

Modern culture has decided the zombies can only make a few sounds.
An example set of letters might be a, b, g, h, m, n, r, z.
We'll use these to define a "zombie-like" encryption.

1. Leave `x` and `l` unchanged
1. Covert every other letter into a number between 0 and 23 (ignore case)
2. Convert the 0&ndash;5 into the constants `b`, `g`, `h`, `m`, `n`, and `z` (in order)
2. Convert the 6&ndash;11 into the same consonants followed by an `r`
2. Convert the 12&ndash;17 into the same consonants followed by an `a`
2. Convert the 18&ndash;23 into the same consonants followed by an `ra`

Thus `encrypt_zombie("please fix my brain")`{.python} returns `"halnbzan zhrx zrnra gnabhrba"`{.python}

Suggestions:

-   Encryption is somewhat tedious, but the core of it includes
    -   using `find` with an alphabet missing `x` and `l` (see [Shift cipher] above for more on how this works)
    -   using the index `% 6` to pick the leading consonant
    -   using `index // 6` to pick the trailing content (`""`, `"r"`, `"a"`, or `"ra`")
-   Decryption is much harder
    -   The number of characters to decrypt at each step varies...
    -   Use a `while` loop that adds different values to the index in each of several cases (see [Ubbi Dubbi] above for an example of how this works)
    -   make sure you handle the following cases:
        -   untranslated characters like `x` and `.`
        -   letters followed by `r` but not `ra`; by `ra`; by `a`; and by none of the above

Unlike the other ciphers on this page, this version of zombie speak was invented for 1110 so you won't find any pages devoted to breaking it online (unless one of your fellow 1110ers wrote one).

# Application

Once you have a working encryption method or two, try communicating with someone else in class using an encrypted message.

# Code Breaking

If you have extra time, try writing code to break encryption without knowing the key.

For `ceasar`, you might try a simple loop over possible keys and print them all; you can likely pick out the correct one pretty easily.  You can also use the observation that English texts generally have about 16% spaces and 13% `e`s to filter out some highly-unlikely keys that do not result in enough of these characters.

Vigenère is a lot harder (people were claiming it was unbreakable as late as the 1917), but if you want to give it a stab [wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Cryptanalysis) has a reasonable overview of the main tactics

Autokey is harder still, but can be solved by guessing bits of text that are likely to occur in the original message. [Wikipedia](https://en.wikipedia.org/wiki/Autokey_cipher) works through an example.

The permutation cipher is similar to several popular anagram word puzzles, and is relatively straightforward to crack.

Ubbi Dubbi is simple enough that you can train yourself to encrypt and decrypt it in you head in real time, actually speaking with others in Ubbi Dubbi. Related quasi-ciphers include oppish and pig latin.
Our zombie speak would be similar, if it was more pronounceable...

# Real security

Current encryption relies on several things we haven't discussed here:

-   Encrypting large blocks of text at once, instead of letter-by-letter.
-   Using methods of encryption based on abstract algebra and number theory which computer scientists are reasonably confident cannot be easily reversed.
-   Implementations that ensure each encryption of a block takes *exactly* the same amount of time, so that you can't infer things about the message from the timing.
-   The use of techniques beyond encryption, such as hashing (a topic you'll learn in our third programming course, CS 2150), to establish other kinds of trust.

However, one lesson learned from the Union's breaking of the Confederacy's use of Vignère ciphers in the US Civil War still holds today:
the Union didn't know how to break the cipher quickly in general, but once it discovered that the Confederacy used three keys for almost all of its communications ("ManchesterBluff", "CompleteVictory", and "ComeRetribution") they were able to break the codes with ease.
This remains true today: if you re-use passwords, or use passwords others might guess, good encryption doesn't help.


## Submission

**At least one partner** should submit one .py file named `crypto.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **all partners' ids** in comments at the top of the file.
