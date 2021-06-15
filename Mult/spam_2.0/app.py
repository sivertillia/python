import time
from tkinter import Tk, Entry, Button

from my_threading import myThread

root =Tk()
textSpam = Entry(width=20).pack()
widthSpam = Entry(width=20).pack()
startBtn = Button(text="Start", width=14)
stopBtn = Button(text="Stop", width=14)

def play(event):
    myThread(spam(event, True))
    

def spam(event, gh):
    text = textSpam.get()
    num = int(widthSpam.get())
    # time.sleep(5)
    for i in range(100):
        if gh:
            print(text)
            time.sleep(2)
        else:
            break

def stop(event):
    myThread(spam(event, False))



startBtn.bind('<Button-1>', play)
startBtn.pack()
stopBtn.bind('<Button-1>', stop)
stopBtn.pack()
root.mainloop()