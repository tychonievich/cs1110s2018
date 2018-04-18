---
title: Tips on building regular expressions
...

# Left to Right

Regular expressions match strings left-to-right.
They can be effectively built in that way.
The basic questions are

1.  What set of characters or substrings could come first?  How do I write those down?
1.  What set of characters or substrings could after the part I've already written? How do I write those down?

It can be helpful to write down a few examples and cross them off as you go.
We'll do examples of this later on on this page.

# Kinds of "one of"

Regular expressions provide two basic tools for saying "one of these":
character classes and alternations.

Character classes are often appropriate when it doesn't matter which character you see, you'll do the same thing afterwards.
For example, when parsing a number I don't much care what digit I see, I'll do the same thing next, so `[0-9]` probably makes sense.

Alternation is generally preferred when which character comes next changes what you do next.
For example, if I am looking for a year of birth of a living person, I expect a 9 to follow a leading 1 but a 0 to follow a leading 2, so I'd probably want `(19|20)[0-9][0-9]` not `[12][09][0-9][0-9]`.

Alternation is also preferred if you need to have (some of) the options have more than one character.

Representing "anything except" is a bit more complicated unless it can be encoded in a single character, like `[^0-9]` for "anything except a digit"

# Maybe, many, or one

If you find yourself thinking "there might be an $X$ here",
add `()?` and then fill in an expression for $X$ inside the parentheses.
The parentheses are optional only if the expression for $X$ is just a single character or character class.

If you find yourself thinking "there might be several $X$ here",
add `()*` and then fill in an expression for $X$ inside the parentheses.
The parentheses are optional only if the expression for $X$ is just a single character or character class.
If you always have at least one, use `+` instead of `*`.
If you always have two or more, repeat the expression:
for example, an at-least-three-digit number would be `[0-9][0-9][0-9]+`

# Examples


## Numbers with comma separators

### Video

This material is also available [in video form](screencasts/regex_number.webm):

<video width="618" height="480" controls>
    <source src="screencasts/regex_number.webm" type="video/webm">
    <source src="screencasts/regex_number.mp4" type="video/mp4">
</video>

The video uses a regular expression building help site, [regexr.com](https://regexr.com).
That site uses Javascript's regular expressions, which have a few differences from Python's regular expresisons;
we now suggest using [pythex.org](https://pythex.org) instead.

### Step-by-step

We'll start with a few examples:

    0
    10,349
    896
    921,334,234,250,100

Now we'll build the expression, left to right.

---

We always start with a digit.

    [0-9]

That makes some progress on the examples, which I'll note with a `█` below:

    0█
    1█0,349
    8█96
    9█21,334,234,250,100
---

Next we appear to have another digit, but not always.
We can express that as a maybe:

    [0-9]([0-9])?

That makes some more progress on the examples:

    0█
    10█,349
    89█6
    92█1,334,234,250,100

The parentheses are not needed in this case since all that was inside was a character class; we could just have correctly written 

    [0-9][0-9]?

---


We again have an optional digit: some do, some don't.
We could also say we have an optional comma, but since we can see commas waiting after a digit in one example, we'll handle the digit first in hopes the comma will be able to be handled all at once:

    [0-9][0-9]?[0-9]?

That makes some more progress on the examples:

    0█
    10█,349
    896█
    921█,334,234,250,100

---

Now, we are either done or we have a comma.
But, if we have a comma we always have three digits following the comma.
A comma followed by three digits is

    ,[0-9][0-9][0-9]

and we might have zero or more of those, so we put it inside a `()*`, like so:

    [0-9][0-9]?[0-9]?(,[0-9][0-9][0-9])*

That makes some more progress on the examples:

    0█
    10,349█
    896█
    921,334,234,250,100█

We appear to be done!


## Double-quoted strings

Suppose we want to find all the double-quoted strings in a `.py` file.
Some good examples include:

    ""
    "hi"
    "say \\"hi\\" to the visitors, please"

Some bad examples include:

    "
    hi
    "say \\\\"hi\\\" to the visitors, please"

----

It looks like we always start with a quote

    "

which updates our example inputs to

    good:
        "█"
        "█hi"
        "█say \\"hi\\" to the visitors, please"
    bad:
        "█
        hi
        "█say \\\\"hi\\" to the visitors, please"

----

Next, we might have zero or more characters within the string

    "()*

In-string characters can be almost anything, but `\\` and `"` are special and new-lines cannot appear at all.
As usual when some are special we'll use a | to handle the main cases:

    "([^\\\\"\\n]|)*


which updates our example inputs to

    good:
        "█"
        "hi█"
        "say █\\"hi\\" to the visitors, please"
    bad:
        "█
        hi
        "say █\\\\"hi\\" to the visitors, please"

----

Our examples are now waiting for a `\\` or ` `"`.
Since `"` should end the string, we'll start with the `\\`.

It's fine to see `\\` in a string, but when we encounter a `\\` the next character could be anything (even a `"` or new-line) without ending the string.
That means we want `\\\\.`: back-slash anything.

    "([^\\\\"\\n]|\\\\.)*

which updates our example inputs to

    good:
        "█"
        "hi█"
        "say \\"hi\\" to the visitors, please█"
    bad:
        "█
        hi
        "say \\\\█"hi\\" to the visitors, please"

----

The good examples now all end in a `"`:

    "([^\\\\"\\n]|\\\\.)*"

which updates our example inputs to

    good:
        ""█
        "hi"█
        "say \\"hi\\" to the visitors, please"█
    bad:
        "
        hi
        "say \\\\"█hi\\" to the visitors, please"

And we're done: we matched all the good examples and failed to match any of the bad ones.

Challenge: how would you extend this to match *all* Python strings, including `'these'` and `'''these'''`?
