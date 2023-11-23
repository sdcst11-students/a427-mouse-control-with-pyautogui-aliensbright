#!python3
import py
import pyautogui
import time
"""
locateImage Optional Parameters:

region: specifies a box (left, top, width,height) to search. This can signficantly speed up your search
"""

print('looking for icon on whole screen')
for i in range(10):
    start = time.time()
    x = pyautogui.locateCenterOnScreen('assets/winIcon.png')
    print(round(time.time()-start,5),end=", ")

print('\n\nlooking in a small box on the bottom left (note that your screen is 1440x900)')
for i in range(10):
    start = time.time()
    x = pyautogui.locateCenterOnScreen('assets/winIcon.png',region=(0,800,100,100) )
    print(round(time.time()-start,5),end=", ")
