## SDSS Computing Studies Python Assignment
### Assignment #9 Pyaugotui and Automation (Marks 10)

Objectives:
* Use pyautogui locate image functions
* Use pyautogui mouse controls
* Use pyautogui pixel commands
* Solve a complex problem through planning using code structures
* Make use of prebuilt modules not native to the Python basic installation
* Have programs receive automatic inputs.

There are many helper files/libraries/modules that you can import and use in Python.  We often get these from The Python Package Repository at https://pypi.org

You can visit and search for almost anything there and you will usually be directed to someone's Github page where you can get documentation and examples.

Today, we will be installing some modules to your computer and then using one of them.

We use pip (the python package installer) to install the modules

#### Getting Input ####
Look at some of the commands on https://pyautogui.readthedocs.io/en/latest/msgbox.html.  Try experimenting with some of them to get user input while your autobot is running.

#### Mouse Commands ####
Take a look at: https://pyautogui.readthedocs.io/en/latest/mouse.html
Some of the most important commands are:
* pyautogui.position() - gets the current coordinates of the mouse
* pyautogui.click() - clicks the mouse at the current location or you can specificy the location as a tuple
* pyautogui.mouseDown() - presses the mouse button down (but does not release it)
* pyautogui.mouseUp() - releases the mouse button if it is down
* pyautogui.moveTo() - moves the mouse to a specific coordinate

### Task 1 Install Pyaugogui module
Open a terminal and type in:
```
pip install pyautogui
```
It's that simple!
You might sometimes type in:
```
py -m pip install pyautogui --user
```
This does the same, but only installs it to your user account on the computer. It is sometimes considered a good idea to instead install packages to folders that are part of your project, to allow for you to use different version of packages on different projects you might be working on.  You can research environments if you are interested in further exploring this.

**We are also going to install:**
opencv-python
pillow

### Task 2 Navigate the Maze
We will have you navigate a maze using pyautogui to control your mouse
Visit https://www.google.com/search?tbm=isch&q=maze%20images&tbs=imgo:1 and save some of the maze images.
Open your Visual Studio Code to full screen mode. This will allow you to set a consistent starting point for your maze.
Use physical locations of coordinates to move the mouse using the pyautogui.moveTo() command.  This command uses 2 required parameters and a 3rd optional paramater:

```
pyautogui.moveTo(x,y,time)
```
x is required and specifies the x location on the screen.  You can run "mouseExample.py" to help you find where those locations are
y is required and specifies the y location
time is optional and specifies how long it takes for the mouse to move
to that position
You may want to include a pause to allow you to switch your screen to the correct locations, or use the input options to allow a keyboard input to start the maze run

### Task 3 Navigate the Maze, random maze placement
Exit full screen (restore down).  Open the file square.webp in a side window (right click on it).
You will make a program that starts the mouse at the entry red arrow and navigates the maze.

Note: You will use variables in your locations so that you can still navigate the maze if you move the VSC window around your screen.
Points to consider:
Resizing the window will mess up your numbers
pyautogui.position() will help you get the initial x and y values for your mouse
You will want to do something like: pyautogui.moveTo(x+20, y-40) to set relative positions to some known point (like the starting point)

Extension:
Store the coordinates for your moves in a list, and iterate through the list with a for loop to move to each one of the locations one at a time! Your code will look a lot smaller although your variables will be a lot bigger.
