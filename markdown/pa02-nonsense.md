---
title: "PA 02: nonsense.py"
...

# Task

Write a program called `nonsense.py`.
When run, it should 

1. ask the user to type their favorite word
2. print that word 12 times on a single line
3. print "\"*word*\" doesn't even sound like a word anymore"

# Example Runs

## Example 1

````
What's your favorite word? `elbow`
elbow elbow elbow elbow elbow elbow elbow elbow elbow elbow elbow elbow 
"elbow" doesn't even sound like a word anymore.
````

## Example 2

````
What's your favorite word? `prandial`
prandial prandial prandial prandial prandial prandial prandial prandial prandial prandial prandial prandial 
"prandial" doesn't even sound like a word anymore.
````

# Troubleshooting

In this and every other assignment all semester long, every `input('some prompt: ')`{.python} must end in either a colon or a question mark, and then a space (like the `'? '`{.python} in the example above).
Failure to follow this rule will result in loss of points.

To put quotes around something, use the other kind of quotes: `'"'`{.python}.

To print two things next to each other with no spaces, use string concatentation with `+`{.python} instead of `,`s in your `print`{.python}.

# Thought Question

There are at least two solutions to this problem; one has many commas in the code and one has few if any.
If you wrote one, see if you can also find and write the other.
Just submit one of the two.
