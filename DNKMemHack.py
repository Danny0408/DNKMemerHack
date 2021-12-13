from pynput import keyboard #line:1
from pynput .keyboard import Controller as KeyboardController #line:2
from pynput .keyboard import Key #line:3
import pyautogui #line:4
from discord import utils #line:5
import threading #line:6
import random #line:7
import time #line:8
import os #line:9
import pyfiglet #line:10
FLAG =True #line:11
counter =0 #line:13
first =0 #line:14
last =0 #line:15
print (pyfiglet .figlet_format ("DNK Memer Hack"))#line:17
print ('Creator: Danny04#9024')#line:18
print ('Youtube: MX-Black')#line:19
print ('Insta  : Danny.tc4')#line:20
def send (OO000OO0OOO00OO00 ):#line:22
    OO0O0OO0O0OO00O0O =KeyboardController ()#line:23
    OO0O0OO0O0OO00O0O .type (OO000OO0OOO00OO00 )#line:25
    OO0O0OO0O0OO00O0O .press (Key .enter )#line:26
    OO0O0OO0O0OO00O0O .release (Key .enter )#line:27
def beg_loop ():#line:29
    while FLAG :#line:30
        send ('pls beg')#line:31
        send ('pls dep all')#line:32
        time .sleep (random .randint (46 ,50 ))#line:34
def findButton ():#line:36
    OO00OO00OO0OOOO0O =(95 ,103 ,238 )#line:37
    O0OOOOO000O0OO0OO =False #line:38
    O000O0O0OOOOO0O0O =pyautogui .screenshot ()#line:39
    for O0O0O0O0OOOOOO000 in range (O000O0O0OOOOO0O0O .width ):#line:40
        for O0O00O000O0OO0O0O in range (O000O0O0OOOOO0O0O .height ):#line:41
            if O000O0O0OOOOO0O0O .getpixel ((O0O0O0O0OOOOOO000 ,O0O00O000O0OO0O0O ))==OO00OO00OO0OOOO0O :#line:42
                pyautogui .click (O0O0O0O0OOOOOO000 ,O0O00O000O0OO0O0O )#line:43
                O0OOOOO000O0OO0OO =True #line:44
                break #line:45
        if O0OOOOO000O0OO0OO ==True :#line:46
            break #line:47
    OO000OO00OOOO0O00 =KeyboardController ()#line:48
    OO000OO00OOOO0O00 .press (Key .tab )#line:49
    OO000OO00OOOO0O00 .release (Key .tab )#line:50
def search_loop (O000OOOO0OO00O00O ,OO0O00O0O00O0O0OO ,OOO00OOOOO0OO0O0O ):#line:53
    time .sleep (5 )#line:54
    while FLAG :#line:56
        send ('pls search')#line:57
        time .sleep (2 )#line:58
        findButton ()#line:59
        time .sleep (random .randint (29 ,33 ))#line:60
        send ("pls beg")#line:61
        time .sleep (1 )#line:62
        send ("pls dep all")#line:63
threads =[threading .Thread (target =beg_loop ),threading .Thread (target =search_loop (counter ,first ,last ))]#line:67
for thread in threads :#line:69
    thread .start ()