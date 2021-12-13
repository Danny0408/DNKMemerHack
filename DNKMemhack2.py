from pynput import keyboard
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
import pyautogui
from discord import utils
import threading
import random
import time
import os
import pyfiglet
FLAG = True

counter = 0
first = 0
last = 0

print(pyfiglet.figlet_format("DNK Memer Hack"))
print('Creator: Danny04#9024')
print('Youtube: MX-Black')
print('Insta  : Danny.tc4')
print('-'*33)

def send(message):
    keyboard1 = KeyboardController()

    keyboard1.type(message)
    keyboard1.press(Key.enter)
    keyboard1.release(Key.enter)

def beg_loop():
    while FLAG:
        send('pls beg')
        send('pls dep all')
        print('Begged')

        time.sleep(random.randint(46, 50))

def findButton():
    color = (95, 103, 238)
    clicked = False
    s = pyautogui.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                pyautogui.click(x, y)
                clicked = True
                break 
        if clicked == True:
            break
    keyboard2 = KeyboardController()
    keyboard2.press(Key.tab)
    keyboard2.release(Key.tab)


def search_loop(counter, first, last):
    time.sleep(5)

    while FLAG:
        send('pls search')
        print("searched")
        time.sleep(2)
        findButton()
        time.sleep(random.randint(29, 33))
        send("pls fish")
        send("pls hunt")
        print("hunted")
        print("fished")
        time.sleep(1)
        send("pls beg")
        print("begged")
        time.sleep(1)
        send("pls dep all")
        print("deposited")



threads = [threading.Thread(target=beg_loop), threading.Thread(target=search_loop(counter, first, last))]

for thread in threads:
    thread.start()