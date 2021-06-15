import pyautogui as pag
import time

time.sleep(5)
list = "."
for i in range(1, 1501):
    # pag.typewrite(str(i))
    pag.typewrite(list)
    pag.press("enter")