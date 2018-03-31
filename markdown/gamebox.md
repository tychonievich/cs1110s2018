---
title: Help on module gamebox
...


This page is the full documentation of [`gamebox.py`](files/gamebox.py), extracted from its docstrings.
Looking for a quick-start guide instead? See the [gamebox sumamry overview](gamebox-summary.html).

# Name

gamebox

# Description
This code is the original work of Luther Tychonievich, who releases it
into the public domain.

As a courtesy, Luther would appreciate it if you acknowledged him in any work
that benefited from this code.

# Classes

-    [Camera](#camera)
-    [SpriteBox](#spritebox)


## Camera
A camera defines what is visible. It has a width, height, full screen status,
and can be moved. Moving a camera changes what is visible.

### Methods defined here:

#### clear
Usage: `camera.clear(color)`{.python}

Erases the screen by filling it with the given color

#### display
Usage: `camera.display()`{.python}

Causes what has been drawn recently by calls to draw(...) to be displayed on the screen

#### draw
Usage: `camera.draw(thing, *args)`{.python}

`camera.draw(box)`{.python} draws the provided SpriteBox object

`camera.draw(image, x, y)`{.python} draws the provided image centered at the provided coordinates

`camera.draw("Hi", 12, "red", x, y)`{.python} draws the text `Hi` in a red 12-point font at x,y

#### move
Usage: `camera.move(x, y=None)`{.python}

`camera.move(3, -7)`{.python} moves the screen's center to be 3 more pixels to the right and 7 more up

### Attributes defined here

#### Attributes you may set

The following attributes refer to the center of the viewable area:

-    `center`, which equals `(x, y)`
-    `x`
-    `y`

The following attributes refer to the edge of the viewable area:

-    `left`
-    `right`
-    `top`
-    `bottom`

The following attributes refer to a corner of the viewable area:

-    `topleft`
-    `topright`
-    `bottomleft`
-    `bottomright`

#### Attributes you may access but not set

The following refer to the size of the viewable area

-    `width`
-    `height`
-    `size`, which equals `(width, height)`

The following refer to the mouse cursor

-    `mousex`
-    `mousey`
-    `mouse`, which equals `(mousex, mousey)`
-    `mouseclick`, which is a Boolean value

#### User-defined attributes

You can add as many other attributes as you want, by (e.g.) saying `camera.number_of_coins_found = 5`{.python}.

##  SpriteBox
Intended to represent a sprite (i.e., an image that can be drawn as part of a larger view) and the box that contains it. Has various collision and movement methods built in.

SpriteBoxes are created using the functions `from_image`, `from_text`, or `from_color`.

### Methods defined here:

#### bottom_touches
Usage: `box.bottom_touches(other, padding=0, padding2=None)`{.python}

`b1.bottom_touches(b2)`{.python} returns `True`{.python} if both `b1.touches(b2)`{.python} and `b1`'s bottom edge is the one causing the overlap.
See `touches` for a description of the optional padding arguments.

#### contains
Usage: `box.contains(x, y=None)`{.python}

checks if the given point is inside this SpriteBox's bounds or not

#### copy
Usage: `box.copy()`{.python}

Make a new SpriteBox just like this one and in the same location

#### copy_at
Usage: `box.copy_at(newx, newy)`{.python}

Make a new SpriteBox just like this one but at the given location instead of here

#### draw
Usage: `box.draw(surface)`{.python}

`b1.draw(camera)`{.python} is the same as saying `camera.draw(b1)`{.python}

`b1.draw(image)`{.python} draws a copy of `b1` on the image proivided

#### flip
Usage: `box.flip()`{.python}

mirrors the SpriteBox left-to-right. 

Mirroring top-to-bottom can be accomplished by

````python
b1.rotate(180)
b1.flip()
````

#### full_size
Usage: `box.full_size()`{.python}

change size of this SpriteBox to be the original size of the source image

#### left_touches
Usage: `box.left_touches(other, padding=0, padding2=None)`{.python}

`b1.left_touches(b2)`{.python} returns `True`{.python} if both `b1.touches(b2)`{.python} and `b1`'s left edge is the one causing the overlap.
See `touches` for a description of the optional padding arguments.

#### move
Usage: `box.move(x, y=None)`{.python}

change position by the given amount in x and y. If only `x` given, assumed to be a point `[x, y]`

#### move_both_to_stop_overlapping
Usage: `box.move_both_to_stop_overlapping(other, padding=0, padding2=None)`{.python}

`b1.move_both_to_stop_overlapping(b2)`{.python} changes both `b1` and `b2`'s positions so that they no longer overlap.
See `touches` for a description of the optional padding arguments.

#### move_speed
Usage: `box.move_speed()`{.python}

change position by the current `speed` field of the SpriteBox object

#### move_to_stop_overlapping
Usage: `box.move_to_stop_overlapping(other, padding=0, padding2=None)`{.python}

`b1.move_to_stop_overlapping(b2)`{.python} makes the minimal change to `b1`'s position necessary so that they no longer overlap.
See `touches` for a description of the optional padding arguments.

#### overlap
Usage: `box.overlap( other, padding=0, padding2=None)`{.python}

`b1.overlap(b1)`{.python} returns a list of 2 values such that `self.move(result)`{.python} will cause them to not overlap
Returns `[0, 0]`{.python} if there is no overlap (i.e., if `b1.touches(b2)`{.python} returns `False`{.python}).

`b1.overlap(b2, 5)`{.python} adds a 5-pixel padding to `b1` before computing the overlap.
`b1.overlap(b2, 5, 10)`{.python} adds a 5-pixel padding in x and a 10-pixel padding in y before computing the overlap.

#### right_touches
Usage: `box.right_touches(other, padding=0, padding2=None)`{.python}

`b1.right_touches(b2)`{.python} returns `True`{.python} if both `b1.touches(b2)`{.python} and `b1`'s right edge is the one causing the overlap.
See `touches` for a description of the optional padding arguments.

#### rotate
Usage: `box.rotate(angle)`{.python}

Rotates the SpriteBox by the given angle (in degrees).

#### scale_by
Usage: `box.scale_by(multiplier)`{.python}

Change the size of this SpriteBox by the given factor.
`b1.scale_by(1)`{.python} does nothing; 
`b1.scale_by(0.4)`{.python} makes b1 40% of its original width and height.

#### top_touches
Usage: `box.top_touches(other, padding=0, padding2=None)`{.python}

`b1.top_touches(b2)`{.python} returns `True`{.python} if both `b1.touches(b2)`{.python} and `b1`'s top edge is the one causing the overlap.
See `touches` for a description of the optional padding arguments.

#### touches
Usage: `box.touches(other, padding=0, padding2=None)`{.python}

`b1.touches(b1)`{.python} returns `True`{.python} if the two SpriteBoxes overlap, `False`{.python} if they do not.
`b1.touches(b2, 5)`{.python} adds a 5-pixel padding to b1 before computing the touch.
`b1.touches(b2, 5, 10)`{.python} adds a 5-pixel padding in x and a 10-pixel padding in y before computing the touch.

### Attributes defined here

#### Attributes you may access and set


The following attributes refer to the center of the box:

-    `center`, which equals `(x, y)`
-    `x`
-    `y`

The following attributes refer to the edge of the box:

-    `left`
-    `right`
-    `top`
-    `bottom`

The following attributes refer to a corner of the box:

-    `topleft`
-    `topright`
-    `bottomleft`
-    `bottomright`

The following refer to the size of the box:

-    `width` -- setting this also changes `height` to keep the same aspect ratio.
-    `height` -- setting this also changes `width` to keep the same aspect ratio.
-    `size`, which equals `(width, height)`

The following attributes refer to the speed of the box:

-    `speed`, which equals `(speedx, speedy)`
-    `speedx`, also called `xspeed`
-    `speedy`, also called `yspeed`

The following attribute refers to the current look of the box:

-    `image`, a [`pygame.Surface`](http://www.pygame.org/docs/ref/surface.html) representing the current look of the box.

#### Attributes you may access but not set

-    `rect`, a [`pygame.Rect`](http://www.pygame.org/docs/ref/rect.html) providing the location and size of the box.

#### Attributes you may set but not access

-    `color`, replaces the current look of the box with a solid expanse of color

#### User-defined attributes

You can add as many other attributes as you want, by (e.g.) saying `box.number_of_coins_found = 5`{.python}.

# Functions

## from_color
Usage: `from_color(x, y, color, width, height)`{.python}

Creates a SpriteBox object at the given location with the given color, width, and height.

## from_image
Usage: `from_image(x, y, filename_or_url)`{.python}

Creates a SpriteBox object at the given location from the provided filename or url.

## from_text
Usage: `from_text(x, y, text, fontsize, color, bold=False, italic=False)`{.python}

Creates a SpriteBox object at the given location with the given text as its content.

## keys_loop
Usage: `keys_loop(callback)`{.python}

Requests that pygame call the provided function each time a key is pressed.

-    `callback`: a function that accepts the key pressed

````python
def onPress(key):
  if pygame.K_DOWN == key:
      print 'down arrow pressed'
  if pygame.K_a in keys:
      print 'A key pressed'
  camera.draw(box)
  camera.display()

gamebox.keys_loop(onPress)
````

You can *either* use `keys_loop` *or* use `timer_loop`, but not both.

## load_sprite_sheet
Usage: `load_sprite_sheet(url_or_filename, rows, columns)`{.python}

Loads a sprite sheet.
Assumes the sheet has rows-by-columns evenly-spaced images and returns a list of those images.

## pause
Usage: `pause()`{.python}

Pauses the timer used to run the `timer_loop`; an error if there is no timer to pause.

## stop_loop
Usage: `stop_loop()`{.python}

Completely quits one `timer_loop` or `keys_loop`, usually ending the program.

## timer_loop
Usage: `timer_loop(fps, callback)`{.python}

Requests that pygame call the provided function fps times a second

-    `fps`: a number between 1 and 1000.  Note that numbers above 60 are likely to cause the program to repsond sluggishly.
-    `callback`: a function that accepts a set of keys pressed since the last tick.

````python
seconds = 0
def tick(keys):
  seconds += 1/30
  if pygame.K_DOWN in keys:
      print 'down arrow pressed'
  if not keys:
      print 'no keys were pressed since the last tick'
  camera.draw(box)
  camera.display()

gamebox.timer_loop(30, tick)
````

## unpause
Usage: `unpause()`{.python}

Unpauses the timer used to run the `timer_loop`; an error if there is no timer to unpause.

