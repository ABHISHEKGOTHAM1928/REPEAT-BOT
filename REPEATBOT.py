import pyautogui as pg
import time

"""
imported the pyautogui for automating typing and sending of messages and with that, 
I have also imported a time module to give some time interval between sending texts.
"""

time.sleep(5)
#time to wait so that we can place the cursor where ever we want after running the file

for i in range(10):
    pg.write("is it ok to wait")
    time.sleep(0.5)
    pg.press("Enter")