import time
import tkinter as tk
from tkinter import messagebox as mb

import multiprocessing

thr = ''

root = tk.Tk()
# root.overrideredirect(1)
textSpam = tk.Entry(master = root, width=20)

def play():
    print('Play')
    mp_while_test()
    

def while_test(spam_num, textasda, c, d):
    spam_num = int(spam_num)
    while 0 <= spam_num:
        print(textasda)
        time.sleep(2)

def mp_while_test():
    global thr
    thr = multiprocessing.Process(target=while_test, args=(widthSpam.get(),textSpam.get()), kwargs = {"c": 3, "d": 4})
    thr.start()

def stop():
    global thr
    try:
        thr.kill()
    except:
        print('Error')
    print('Stop')

def on_close():
    if mb.askokcancel("Quit", "Do you want to quit?"):
        try:
            thr.kill()
        except:
            print('Error')
        root.destroy()

if __name__ == "__main__":
    textSpam.pack()
    widthSpam = tk.Entry(master = root, width=20)
    widthSpam.pack()
    startBtn = tk.Button(master = root, text="Start", width=14, command=play)
    startBtn.pack()
    stopBtn = tk.Button(master = root, text="Stop", width=14, command=stop)
    stopBtn.pack()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()