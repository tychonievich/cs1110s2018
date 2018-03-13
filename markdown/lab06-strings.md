---
title: "Lab 6: String Puzzles"
...


# Mechanics of this Lab

1.	We'll start with a group logic puzzle! Get in a group of 3(ish) and the TAs will show a puzzle on the screen. Talk together to figure it out.

2.	Read -- this lab is intended to help you learn on your own.  Read what we've written before you code!


# String Puzzles

Strings can be manipulated using operators, functions, and methods.
Manipulating strings is a common part of many kinds of  programs.
This lab explores some of these ideas.
It's structure is an overview of available operations and a set of puzzles.
Restrict yourself to the listed operations for this lab;
we'll learn other, more complicated tools later, which you can find if you search online,
but using them before you understand these simpler operations will generally confuse, not enlighten.

In everything that follows, there is a rule Python *never* breaks:

> Nothing but `=` changes a string; everything else either inspects it unchanged or creates a new string.

# Tasks

Create a file named `str_funcs.py` in which you implement as many of the following tasks as possible.  You are welcome to also have testing code in that file, or to test in a different file.

See also the [Tools to Use] section below, which lists both things you already know and things you haven't seen before.
Part of our goal here is to encourage you to develop the skills needed to learn on your own, so make an effort to understand how to use the components we list before you ask for help.

Don't be afraid to experiment; trial-and-error is a safe and productive way to learn programming.

Most of you won't get to all the problems below. That's expected; do as many as you can get to in the time alloted and submit what you have at the end, primarily so we can see how much you got to.


## Ellipsis
Write a function `ellipsis(s)` that replaces all but the first two and last two characters of a string with an ellipsis (`...`).

Example: `ellipsis("computer science")`{.python} should return `"co..ce"`{.python}

Tools: There is a solution that uses only the slice and concatenation operators.

## Eighteen
When internationalization of computer applications became a topic of interest, people got tired of typing internationalization so they shortened it to i18n, meaning "an "i", 18 more letters, and then an "n"". Write a function `eighteen(s)` that uses the same idea to shorten any string.
	
Examples: 

-	`eighteen("computer science")`{.python} should return `"c14e"`{.python}
-	`eighteen("is")`{.python} should return `"i0s"`{.python}
-	`eighteen("fun")`{.python} should return `"f1n"`{.python}

Tools: There is a solution that uses only the index operator and built-in functions

## Alliterative
Two words are alliterative if they start with the same consonant sound.
Since sounds are a bit complicated in English, write a simpler version:
a function `allit(s, t)` that is `True` if `s` and `t` start with the same non-vowel character.
Your code should treat upper- and lower-case letters as the same.

Examples:

-	`allit("hi", "hello")`{.python} should return `True`{.python}
-	`allit("Hi", "hello")`{.python} should return `True`{.python}
-	`allit("fun", "great fun")`{.python} should return `False`{.python}
-	`allit("exciting", "excitement")`{.python} should return `False`{.python}

Tools: There is a solution that uses one method to fix case, several operators, and an extra string literal.

## Between
Write a function `between` that returns the portion of its first parameter that falls between the first and second occurrence of its second parameter; or return the empty string if the second parameter does not occur twice.

Examples:

-	`between("peripatetics", "p")`{.python} gives `"eri"`{.python}
-	`between("loan me a lovely loon to look at", "lo")`{.python} gives `"an me a "`{.python}
-	`between("loan me a lovely loon to look at", " lo")`{.python} gives `"vely"`{.python}
-	`between("quick", "u")`{.python} gives `""`{.python}
-	`between("quick", "z")`{.python} gives `""`{.python}

Tools: There is a solution that uses the `find` method, the slice operator, an `if` statement or two, and a little arithmetic.


## Reversed-Between
Write a function `rbetween` that does the same as `between`, but looks between the last two, not first two, occurrences.

Examples:

-	`rbetween("peripatetics", "p")`{.python} gives `"eri"`{.python}
-	`rbetween("loan me a lovely loon to look at", "lo")`{.python} gives `"on to "`{.python}
-	`rbetween("loan me a lovely loon to look at", " lo")`{.python} gives `"on to"`{.python}
-	`rbetween("quick", "u")`{.python} gives `""`{.python}
-	`rbetween("quick", "z")`{.python} gives `""`{.python}

Tools: There is a solution that uses the `rfind` method, the slice operator, an `if` statement or two, and a little arithmetic.

## Random Between
Write a function `rand_between` that randomly does either `between` or `rbetween`.

Examples:

-	`rand_between("peripatetics", "p")`{.python} gives `"eri"`{.python}
-	`rand_between("loan me a lovely loon to look at", "lo")`{.python} gives `"on to "`{.python} sometimes and `"an me a "`{.python} other times
-	`rand_between("loan me a lovely loon to look at", " lo")`{.python} gives `"vely"`{.python} sometimes and `"on to"`{.python} other times.
-	`rand_between("quick", "u")`{.python} gives `""`{.python}

Tools: There is a solution that `random.randint`, an `if` statement, and both `between` and `rbetween`.

## Temperature
Web pages are coded in a language called HTML, and understanding it can help us write programs that use the Internet.  For example, part of <weather.gov>'s page for a given zip code is current temperature which shows up between `class="myforecast-current-lrg">` and `&deg;F`; for example, at the time I am writing this description [Charlottesville's page](view-source:http://forecast.weather.gov/MapClick.php?lat=38.0356284&lon=-78.4948031) contains `<p class="myforecast-current-lrg">83&deg;F</p>`.

Write a function `temperature` that returns the the content between the first `class="myforecast-current-lrg">` and `&deg;F` in its argument string.

Examples:

-	`temperature("<p class="myforecast-current-lrg">83&deg;F</p>")`{.python} should return `"83"`{.python}
-	`temperature("<p class="myforecast-current">Fair</p>\n<p class="myforecast-current-lrg">103&deg;F</p><p class="myforecast-current-sm">28&deg;C</p>")`{.python} should return `"103"`{.python}

Tools: There is a solution that uses the `find` method, the slice operator, and a little arithmetic.


## Unhide
Sometimes people obscure email addresses by writing the `@` and `.` as `at` and `dot`.
Write a function `unhide` that converts these back to `@` and `.`.
Even do this if they use capitals or parentheses.

Examples:

-	`unhide("mst3k@virginia.edu")`{.python} gives `"mst3k@virginia.edu"`{.python}
-	`unhide("mst3k at virginia.edu")`{.python} gives `"mst3k@virginia.edu"`{.python}
-	`unhide("mst3k (at) virginia (dot) edu")`{.python} gives `"mst3k@virginia.edu"`{.python}
-	`unhide("mst3k AT virginia DOT edu")`{.python} gives `"mst3k@virginia.edu"`{.python}
-	`unhide("mst3k@virginia dot edu")`{.python} gives `"mst3k@virginia.edu"`{.python}

Tools: All you need is `replace`; but remember that `replace` (like all string methods) does not modify the string in-place, rather returns a copy.  Thus

````python
a = "a string"
a.replace("tr", "w")
print(a)
````

prints `a string` not `a swing`; however

````python
a = "a string"
a = a.replace("tr", "w")
print(a)
````

prints `a swing`.
	
## Vowel confusion
Write a function `vowel_confusion` that swaps all `e`s and `i`s.

Examples:

-	`vowel_confusion("Electric slide")`{.python} gives `"Ilictrec sledi"`{.python}
-	`vowel_confusion("I sang, and thought I sang very well; but he just looked up into my face with a very quizzical expression, and said, 'How long have you been singing, Mademoiselle?'")`{.python} gives `"E sang, and thought E sang viry will; but hi just lookid up ento my faci weth a viry quezzecal ixprisseon, and saed, 'How long havi you biin sengeng, Madimoesilli?'"`{.python}

Tools: All you need is `replace`; but you'll need to use three, not two, replacements, using some kind of rarely-typed placeholder character like `ß`.

## Few quoted characters
Write a program in a file `changing_str.py` whose first line is `a = "reasonable simplicity"`{.python}, whose last line prints `radical complexity`{.python}, with as few characters appearing between quotes within the program as possible.

The following program:

````python
a = "reasonable simplicity"
print("radical complexity")
````

has 39 characters in quotes (21 for the first line, 18 for the second).

But this one:

````python
a = "reasonable simplicity"
print(a[0] + "adical complex" + a[-3:])
````

has only 35.
We're pretty confident that it is possible to get to only 23...


# Submission

**Each partner** should submit one .py file named `str_funcs.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
If you got to the last task, also submit `changing_str.py`.
Please put **both partners' ids** in comments at the top of the file.




# Tools to Use

In the following, `s` and `t` are assumed to be strings;
`i` and `j` are assumed to be integers, with `i <= j`;
`k` is also assumed to be an integer.

## Operators

Concatenation
:	`s + t` makes a new string containing the characters of `s` followed by the character s of `t`

	Example: `"where" + "fore"`{.python} creates `"wherefore"`{.python}

Comparison
:	-	`s == t`{.python} is `True`{.python} if `s` and `t` have the same characters in the same order.
	-	`s != t`{.python} is `True`{.python} if `s == t`{.python} is `False`{.python}.
	-	`s < t`{.python} is `True`{.python} if `s` comes before `t` in something similar to alphabetical order (except it puts all capitals before any lower-case and also has positions for all punctuation, etc).
	-	`s in t`{.python} is `True`{.python} if `t` could be written as `x + s + y` for some (possibly empty) strings `x` and `y`.
	
	Examples: the following are all `True`
	
	-	`"fun" == 'fun'`{.python}
	-	`"fun" != "Fun"`{.python}
	-	`"120" < "20" < "40" < "8"`{.python}
	-	`"aardvark" < "animal" < "artificial" < "be" < "bee"`{.python}
	-	`"A" < "Z" < "a" < "z"`{.python}
	-	`"fun" in "more functions"`{.python}

Indexing
:	`s[i]`{.python} extracts a single-character string from `s`.
	`s[0]`{.python} is the first character of `s`, 
	`s[1]`{.python} is the second character of `s`, 
	and so on up to `s[len(s)-1]`{.python}.
	`s[-1]`{.python} is the last character of `s`, 
	`s[-2]`{.python} is the next-to-last character of `s`, 
	and so on down to `s[-len(s)]`{.python}.
	
	Example: `"where"[1]`{.python} creates `"h"`{.python}; so does `"where"[-4]`{.python}

Slicing
:	`s[i:j]`{.python} extracts a substring from `s`,
	beginning with `s[i]`{.python} and ending *before* `s[j]`{.python}.
	
	A missing index is treated as the end of the string.
	
	Example: 
	
	-	`"slices"[1:4]`{.python} creates `"lic"`{.python} -- not `"lice"`{.python} because when slicing we do not get the character at ending position.
	-	`"slices"[:4]`{.python} creates `"slic"`{.python}
	-	`"slices"[4:]`{.python} creates `"es"`{.python}

This is also an operator called an *extended slice* but it isn't needed for any of the puzzles in this lab.
If you are curious,

	-	`"many letters"[1::2]`{.python} creates `"ayltes"`{.python} -- every 2nd character starting at index 1.
	-	`"many letters"[1:9:2]`{.python} creates `"aylt"`{.python} -- every 2nd character starting at index 1 and ending before reaching index 9.
	-	`"many letters"[::3]`{.python} creates `"myee"`{.python} -- every 3rd character starting at index 0.

## Functions

Functions that manipulate strings take the strings are their arguments.
The following functions do not need any `import`{.python} to be found.
	
-	`len(s)`{.python} returns the number of characters in `s`.
	
	Example: `len("fun")`{.python} returns `3`

-	`str(anything)`{.python} returns a string representation of `anything`.
	
	Example: `str(1110)`{.python} returns `"1110"`{.python}; `str(str)`{.python} returns `"<class 'str'>"`{.python}.

-	`repr(anything)`{.python} returns a "canonical" string representation of `anything`.
	Notably for strings, this is includes surrounding quotes and no new-lines.
	
	Example: 
	
	-	`repr("fun")`{.python} returns `"'fun'"`{.python},
		which, when printed, will look like `'fun'`
	-	`repr("don't " + 'mix "quotes" ' + "with 'quotes' " + '''and
		new lines''')`{.python}
		returns a string that, when printed, will look like `'don\'t mix "quotes" with \'quotes\' and\nnew lines'`

-	`format(value, s)`{.python} is like `str`, but more flexible.
	
	-	`format(value)`{.python} returns exactly what `str(value)` returns.
	-	`format(value, '8')`{.python} returns `str(value)` padded with spaces to be at least 8 characters wide.
	-	`format(number, '.3f')`{.python} returns the number represented with three digits to the right side of the decimal point.
	
	There are many many more things `format` can do (e.g., try `format(0, 'w<+12.3f')`{.python}) but even what we've covered is more than you usually need.

## Methods

String methods are invoked by putting them after a string, preceded by a period.
They generally return a value based on the string they follow.

-	`s.capitalize()`{.python} returns a version of `s` with the first letter upper case, the rest lower case.  The same as `s[0].upper() + s[1:].lower()`{.python}.

	`s.title()`{.python} is similar, but capitalizes and character following a space as well.

-	`s.center(i)`{.python} returns `s` if `len(s) >= i`{.python}; otherwise it adds spaces to each side of `s` to return a string of length `i`.
	
	`s.ljust(i)`{.python} and `s.rjust(i)`{.python} are similar but left- or right-justify, instead of centering.

-	`s.count(t)`{.python} returns how many non-overlapping occurrences of `t` there are in `s`.  `'hahahahaha'.count('hah')`{.python} returns `2`.

	`s.count(t,i,j)`{.python} only counts between positions `i` and `j`

-	`s.endswith(t)`{.python} returns `True` if `s[-len(t):] == t`{.python}
	
	`s.startswith(t)`{.python} is similar, but checks the other end of `s`

-	`s.find(t)`{.python} returns the first location of `t` within `s`, or `-1` if `t not in s`{.python}.
	
	Example: 
	
	-	`"fun for fun's sake".find("fun")`{.python} returns `0`
	-	`"fun for fun's sake".find("fun'")`{.python} returns `8`
	
	`s.find(t,i,j)`{.python} only looks between positions `i` and `j`
	
	`s.index(...)`{.python} is just like `find` except it has an error if `t` is not found instead of returning `-1`.
	
	`s.rfind` and `s.rindex` are just like `find` and `index` except they return the index of the last occurance instead of the first.
	
	-	`"fun for fun's sake".rfind("fun")`{.python} returns `8`
	-	`"fun for fun's sake".rfind("fun ")`{.python} returns `0`

-	`s.lower()` returns a new string where all characters with a defined case have been replaced by their lower-case versions.  Thus `"WoNk123e!".lower() == "wonk123e!"`{.python}
	
	`s.upper()` is similar, but uses upper-case instead of lower-case characters.

-	`s.strip()` returns a new string that is like `s` but has no white-space characters (spaces, newlines, etc) at its beginning or end.  Thus `" so odd ".strip() == "so odd"`{.python}.

	`s.strip(t)` removes characters in `t` instead of white-space characters.
	Thus `"periodically".strip("repyli") == "odica"`{.python}

	The related function `s.lstrip` only removes them from the beginning, `s.rstrip` only from the end.

-	`s.replace(t1, t2)` returns a new string with all occurances of `t1` replaced by `t2`.
	Thus `"cocoa is coo-coo".replace("o", "uh") == "cuhcuha is cuhuh-cuhuh"`{.python}.
	
	`s.replace(t1, t2, i)` replaces the first `i` occurrences of `t1`, leaving any extras unchanged.
	Thus `"cocoa is coo-coo".replace("o", "uh", 3) == "cuhcuha is cuho-coo"`{.python}.

-	There are also two other useful methods, `join` and `split`, that we will discuss more in the weeks to come.

