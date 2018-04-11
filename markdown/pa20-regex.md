---
title: "PA 20: regexs.py"
...

# What we mean by "match"

In the following, we say things like "`t.j.` should not match."
This means that the full string `t.j.` wil not appear in the set of answers returned by `finditer`.
Sub-parts of it might (e.g., `t.j` may match), but `t.j.` won't.

# Task

Write a python file called `regexs.py` that defines several variables containing compiled regular expressions,
as follows:

-   `nospace =`{.python} a regular expression that matches one or more non-whitespace characters. There is a relatively straightforward solution that is 12 characters long.

    `CS1110-001/smile` should match, as should `!`
    
    `hi there` should not match, nor should the empty string.

-   `quotation =`{.python} a regular expression that matches text beginning and ending with a `"`, with no internal `"`, where the first and last character inside the quotes are not spaces.
    Our reference solution is 32 characters long.
    
    `"hi there"` should match
    
    `" hi there"` should not match, nor should `"hi there "` or `"I said "hi" just now"`.

-   `twonum =`{.python} a regular expression that matches pairs of numbers, separated by a space, comma, or both (with the space after the comma if both: `, `but not ` ,`).
    Accept both numbers with and without decimal places, and allow an optional preceding `-` on each number.
    If there is a decimal place, there must be at least one digit on each side of it.
    Our reference solution is 50 characters long.
    
    Additionally, each of the two numbers (with the `-` if present) should be a group after a match.
    
    `3,4`, `3.0, 4.5`, and `-3.14159265 1110` should all match.
    
    `3.4.5, 1`, `1   2`, and `3 - 4` should not match.
    

# Testing your code

When you run `regexs.py`, nothing should happen.
It defined variables, it does not define functions or run anything.

If in another file you enter the following

````python
import regexs

text = '''
CS1110-001/smile ! hi there
"hi there" but not " hi there" or "hi there " or "I said "hi" just now"
3,4, 3.0, 4.5 and -3.14159265 1110 but not 3.4.5, 1 or 1   2 or 3 - 4
Thomas Jefferson and Edmund Jennings Randolph and J. Pierpont Finch and T. Jefferson
but not T Jefferson or Thomas J. or Flannery O'Connor
'''

def full_match(regex, text):
    '''Gives a list of all complete matches'''
    ans = []
    for match in regex.finditer(text):
        ans.append(match.group(0))
    return ans

ns = full_match(regexs.nospace, text)
print('nospace:',
    'CS1110-001/smile' in ns,
    '!' in ns,
    'hi there' not in ns,
    '' not in ns)

q = full_match(regexs.quotation, text)
print('quotation:',
    '"hi there"' in q,
    '" hi there"' not in q,
    '"hi there "' not in q,
    '"I said "hi" just now"' not in q)

tn = full_match(regexs.twonum, text)

print('twonum:',
    '3,4' in tn,
    '3.0, 4.5' in tn,
    '-3.14159265 1110' in tn,
    '3.4.5, 1' not in tn,
    '1   2' not in tn,
    '3 - 4' not in tn)

for match in regexs.twonum.finditer(text):
    if match.group(0) == '3,4':
        print('  match1:', '3' in match.groups(), '4' in match.groups())
    if match.group(0) == '-3.14159265 1110':
        print('  match2:', '-3.14159265' in match.groups(), '1110' in match.groups())
````

then that file, when run, should print all `True`{.python}:

````
nospace: True True True True
quotation: True True True True
twonum: True True True True True True
  match1: True True
  match2: True True
````


# Troubleshooting

For `nospace`, negative character classes (i.e., beginning `[^`) are your friend.

For `quotation`, you'll probably include most of `nospace` twice (for the first and last non-white character), but also exclude quotes `"`.
Also, you might want to handle the special case of a quote with zero or one non-white characters inside specially.

For `twonum`, you probably want to get a single number matcher working, and a gap (comma, or, space, or comma space) working, and then combine them into "number gap number".

"Whitespace characters" includes space ` `, but also newlines `\n` and `\r` and tabs `\t`.

The "should be in a group" constraint can be met by adding parentheses...

[pythex](https://pythex.org/) is your friend.  If you are not sure what your regexs are doing, try playing with them there.
