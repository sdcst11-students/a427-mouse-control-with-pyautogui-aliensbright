#!python3
import pyautogui
import time

'''
Exit full screen (restore down).  Open the file square.webp in a side window (right click on it).
You will make a program that starts the mouse at the entry red arrow and navigates the maze.

Note: You will use variables in your locations so that you can still navigate the maze if you move the VSC window around your screen.
Points to consider:
Resizing the window will mess up your numbers
pyautogui.position() will help you get the initial x and y values for your mouse
You will want to do something like: pyautogui.moveTo(x+20, y-40) to set relative positions to some known point (like the starting point)

Extension:
Store the coordinates for your moves in a list, and iterate through the list with a for loop to move to each one of the locations one at a time! Your code will look a lot smaller although your variables will be a lot bigger.
'''
def movement():
    while True:
        try:
            coords=pyautogui.locateCenterOnScreen('assets/StartPoint.png', confidence=0.1)
            print(coords)
            pyautogui.moveTo(coords)
        except:
            print('this isnt working')
            input('x')
movement()
