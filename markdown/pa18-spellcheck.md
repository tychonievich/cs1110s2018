---
title: "PA 18: spellcheck.py"
...

# Task

Write a file named `spellcheck.py` that checks user-entered text for misspelled words.

Do this by reading a list of correctly spelled words from 
<http://cs1110.cs.virginia.edu/files/words.txt>
-- the file has one word per line.

Then read lines of user-entered text;
list any misspelled words in what they entered;
and keep reading lines until they enter a blank line.
Strip off any leading or trailing punctuation before checking the word (i.e., strip `.?!,()"'`).
Only list a word as misspelled if it does not appear either in the case they typed it or in lower-case form.

Your program should read the list of words from the web only once per run of the program, no matter how many lines of text the user types in a given run.

## Style matters

In addition to functional correctness, some points will be reserved for

1.  having good variable names
1.  having meaningful docstrings for all functions you write


# Example Invocations

An example run of the program might look like:

    Type text; enter a blank line to end.
    "'But oh, beamish nephew, beware of the day,
      MISSPELLED: beamish
    If your Snark be a Boojum!  For then
      MISSPELLED: Snark
      MISSPELLED: Boojum
    You will softly and suddenly vanish away,
    And never be met with again!'
     


# Thought Question

How hard would it be to handle hyphenated words?
To only permit capitalized words if they appear capitalized in the word list or start a sentence?
To let the user specify which word list they want (or allow several word lists)?
To have multiple dictionaries (e.g., for multiple languages) and infer the language based on which reports the fewest misspellings?

As always with such enhancements, don't submit them if you implement them.

# Troubleshooting

Did you remember to `decode` and `strip` the lines of text you read from the website?

Match our formatting exactly, including 

-   having a line printed up front and then no prompt in the `input`s for each line the user types
-   putting two spaces before the all-caps `MISSPELLED:`, one space after it
-   reporting misspellings in the order they appear within the line
-   reporting misspellings without bracketing punctuation (report `Boojum` not `Boojum!`, etc.)

Capitalization sometimes matters.
For example, `Abe` is spelled correctly (because it is a common nick-name)
but `abe` is not (because it is not an English word).
A few more examples:

User enters | Dictionary has | Decision
------------|----------------|---------
Abe         | Abe            | correctly spelled
abe         | Abe            | misspelled
Abjure      | abjure         | correctly spelled
abjure      | abjure         | correctly spelled
ecmascript  | ECMAScript     | misspelled
Ecmascript  | ECMAScript     | misspelled
ECMAscript  | ECMAScript     | misspelled
ECMAScript  | ECMAScript     | correctly spelled

Can't figure out what case you are missing? Try the following:

-   Apostrophe inside a word that needs one, like `wits's`
-   Apostrophe inside a word that can't have one, like `wi'ts`
-   Correctly spelled word inside apostrophes, like `'wits'`
-   Incorrectly spelled word inside apostrophes, like `'witss'`
-   All of the above with other punctuation (not just apostrophes)
-   The above with incorrect capitalization instead of incorrect spelling
-   Incorrectly spelled words at the beginning, middle, and end of the first, middle, and last line of input

Confused how to read the page only once?  Try reading the page into a list of words before you do any spellchecking.
