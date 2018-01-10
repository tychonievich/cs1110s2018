---
title: "Lab 1: Installing Python and PyCharm"
...

Lab this week is optional in that we will not be taking roll.
However, this is an opportunity to come to ensure that you have Python, PyCharm, and PyGame installed and working properly on your laptops. 
If you do not come to lab, we will assume you have taken care of this yourself and you are ready to go when we start coding in lecture next week. 
So, if you have any doubts, come on down to lab, meet some of the TAs, and make sure you're laptop is setup and ready to go!


# Installing

## on Windows

1.  Install Python 3.6.4:
    
    1.  Download [the executable x86-64 installer from python.org](https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe).
    
    2.  Run the installer.
    
    3.  Choose the "Custom Installation" option.
    
    4.  If asked, check "Add Python to environment variables" and "Install for all users"; leave all other options at their default values.

2.  Install PyCharm Community Edition 2017.3.2:
    
    1.  Download [the executable installer from jetbrains.com](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC).
    
    2.  Run the installer.
    
    3.  At the Installation Options screen, check "Create associations" - ".py"; leave all other options at their default values.

3.  Set up PyCharm and PyGame; see the cross-platform information [below](#pycharm-setup).
    
## on Mac

1.  Install Python 3.6.4:
    
    1.  Download [the installer from python.org](https://www.python.org/ftp/python/3.6.4/python-3.6.4-macosx10.6.pkg).
    
    2.  Run the installer.
    
    3.  Choose the "Custom Installation" option.
    
    4.  If asked, check "Add Python to environment variables" and "Install for all users"; leave all other options at their default values.

2.  Install PyCharm Community Edition 2017.3.2:
    
    1.  Download [the dmg disk image from jetbrains.com](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac&code=PCC).
    
    2.  Drag the icon to the Applications folder.
    
3.  Install prerequisites for PyGame

    1.  Download and install [XQuartz - https://dl.bintray.com/xquartz/downloads/XQuartz-2.7.11.dmg](https://dl.bintray.com/xquartz/downloads/XQuartz-2.7.11.dmg).

    2.  Open a Terminal window (`/Applications` → `Utilities` → `Terminal`).  In the terminal window, paste the following commands in **one at a time** and run them individually:

        1.  `xcode-select --install`{.bash}
        2.  `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`{.bash}
        3.  `alias brew=/usr/local/bin/brew`{.bash}
        4.  `brew install mercurial`{.bash}
        5.  `brew install git`{.bash}
        6.  `brew install sdl sdl_image sdl_ttf smpeg portmidi libogg libvorbis`{.bash}
        7.  `brew install sdl_mixer --with-libvorbis`{.bash}
        8.  `pip3 install hg+http://bitbucket.org/pygame/pygame`{.bash}
    
    3.  In the Finder, open  `/Applications` → `Python 3.6` and double-click on the icon for `Install Certificates.command`

4.  Set up PyCharm and PyGame; see the cross-platform information [below](#pycharm-setup).
    

## On Other Systems

If you are using a system other than Windows or Mac (\*nix, \*BSD, etc.), first off, good for you!
If you have trouble installing Python and PyCharm, post what system you are using on Piazza and we'll help get you set up.


# Set up PyCharm and PyGame

There's a fair bit of set-up, but you should only have to do this once.

1. Run PyCharm

2. Accept the default options in the various screens that pop up asking you to set up various aspects of PyCharm.
    These should only appear the first time you run PyCharm.

3.  When you reach the welcome screen,

    ![PyCharm welcome screen](files/pycharm-splash.png)
    
    set up PyGame and how Pycharm interacts with Python doing the following:
    
    1.  In the "configuration" menu (gear icon), select "Settings".
    
    2.  Go to the "Project Interpreter" option on the left of the screen.

        ![Project interpreter options](files/pycharm-interp-setup.png)
    
    3.  If the "Project Interpreter" drop-down on the top of the screen has a "Python 3" of some kind, select it and skip the indented steps below; **otherwise**

        1.  Click the gear icon beside the drop-down (top-right corner of the window) and select "Add Local..." from the menu
        2.  In the pop-up window, on the left chose "System Interpreter"
        3.  In the drop-down, pick python3.6 if it is present; if not, click the "..." button and find where you installed Python.
        
            ![Project interpreter selection](files/pycharm-interp.png)
        
        4.  Click OK
    
    4.  Click the green + either to the top right or bottom left of the list of packages

        ![Project interpreter options](files/pycharm-interp-setup.png)
    
    5.  In the pop-up window, type `pygame` in the search bar, select "Pygame" in the left-hand list, and click "Install Package"
    
        ![PyGame installation](files/pycharm-pygame.png)

    6.  Wait until an "installation successful" message appears
    
    7.  Click "Apply" and "OK" in each window until back in the welcome screen

        ![Welcome screen](files/pycharm-splash.png)

4.  Click "Create New Project"

5.  In the new project window

    1.  Set the Location to some place you can find in your OS's file browser; suggested:
        
        -   Windows: `C:\\Users\\`*your-user-name-on-your-computer*`\\Desktop\\cs1110`
        -   OS X: `/Users/`*your-user-name-on-your-computer*`/Desktop/cs1110`
    
    2.  Expand the "Project Interpreter" with the little triangle and pick the "Existing Interpreter" option, with Python 3.6 as the interpreter.

        ![New project setup window](files/pycharm-newproject.png)

    3.  Click the Create button

6. Create a new Python file by right-clicking (control-click if you only have one button) on the cs1110 folder in the Project pane on the left side of the window, then pick New → Python File

    ![New file menu](files/pycharm-newfile.png)

7. Type `setup\_test.py` in the new file pop-up

    ![New file pop-up](files/pycharm-newfile-test.png)

8. In the editor window, type or paste the following:

    ````python
    import pygame
    import urllib.request
    
    pygame.init()
    urllib.request.urlopen('https://cs1110.cs.virginia.edu')
    
    print('Hello, world!')
    ````

9. Right-click in white space in the editor window (not on any text) and select "Run setup_test" from the drop-down menu.

    ![Run menu](files/pycharm-run.png)

10. If you see "Hello, world!" in the second line of the bottom of the window, everything is set up correctly!

    ![Desired run results](files/pycharm-run-success.png)

    If you see something else, or if something went wrong along the way, ask a TA for help.

