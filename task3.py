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

def getStartPoint():
    '''
    x=1
    while True:
        try:
            pyautogui.moveTo(1318,200)
            coords=pyautogui.locateCenterOnScreen('assets/StartPoint123.png', confidence=x)
            print(coords)
            pyautogui.moveTo(coords)
            input('x')
        except:
            print('this isnt working')
            x=x-0.05
            input('x')
'''
    input('go to the start spot')
    return pyautogui.position()

x,y=getStartPoint()
a=28  #allows user to change the width of the maze
CoordsList=([x,y,0],[x+3*a,y,3],[x+3*a,y+3*a,3],[x+2*a,y+3*a,1],[x+2*a,y+7*a,4],[x+4*a,y+7*a,2],[x+4*a,y+6*a,1],[x+3*a,y+6*a,1],[x+3*a,y+4*a,2],[x+5*a,y+4*a,2],[x+5*a,y+2*a,2],[x+7*a,y+2*a,2],[x+7*a,y+1*a,1],[x+9*a,y+1*a,2],[x+9*a,y+3*a,2],[x+7*a,y+3*a,2],[x+7*a,y+6*a,3],[x+6*a,y+6*a,1],[x+6*a,y+9*a,3],[x+8*a,y+9*a,2],[x+8*a,y+8*a,1],[x+12*a,y+8*a,4])

for i in CoordsList:
    pyautogui.moveTo(i[0],i[1],i[2])