---
title: "PA 08: bmr.py"
...

# Task

Write a file named `bmr.py` with a function named `st_jeor` which, if given (mass, height, age, sex), returns Mifflin St Jeor estimate of the [basal metabolic rate](https://en.wikipedia.org/wiki/Basal_metabolic_rate#BMR_estimation_formulas),
an estimate of the Calories consumed to keep the body alive.
Assume `mass` is given in kilograms, `height` in centimeters, `age` in years, and `sex` is either `"male"`{.python} or `"female"`{.python}.

In the formula

> ![Formula from Wikipedia](https://wikimedia.org/api/rest_v1/media/math/render/svg/45400b1e5220880f1b37ed6dabbda842c4f7b61a)

*s* is +5 if `sex` is `"male"`{.python} and &minus;161 if it is `"female"`{.python}; 
*m*, *h*, and *a* represent `mass`, `height`, and `age` respectively.


# Example Invocations

When you run `bmr.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import bmr

print(bmr.st_jeor(74.7, 162.9, 19, 'female'))
````

you should get the following output:

````
1509.125
````

# Thought Question

Consider adding the other formulas listed in Wikipedia: 
`harris_benedict`, `revised_harris_benedict`, and `katch_mcardle` (`katch_mcardle` will require a [body fat percentage estimate](https://en.wikipedia.org/wiki/Body_fat_percentage)).
How much do they differ?


# Troubleshooting

The unit multipliers in the equation all cancel out; you can ignore them.

Have you tried other cases besides `(74.7, 162.9, 19, 'female')`{.python}?
To know you got them right, try changing one argument at a time and see if it creates the expected size change in the output; for example, adding 10 kg should add 100 Calories.

