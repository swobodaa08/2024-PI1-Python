import pyautogui as pag
import time
import random

while True:
    pag.FAILSAFE = False
    x = random.randint(100, 800)
    y = random.randint(100, 800)
    pag.moveTo(x, y, 0.1)
    time.sleep(0.2)