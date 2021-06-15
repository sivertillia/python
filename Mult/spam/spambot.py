import pyautogui as pag
import time

time.sleep(5)

for word in open("number.txt", "r"):
    pag.typewrite(word)
    pag.press("enter")