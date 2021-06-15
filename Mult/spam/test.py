import time
from tkinter import messagebox, Tk, Entry, Button, END, Label, LEFT
from threading import Thread

def threaded_run(func):
    def wrapped(*args, **kwargs):
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
        return thr
    return wrapped

root =Tk()
e = Entry(width=20)
l = Entry(width=20)
p = Button(text="Play", width=14)
s = Button(text="Stop", width=14)

def play(event):
    threaded_run(spam(event, True))
    

def spam(event, gh):
    text = e.get()
    num = int(l.get())
    # time.sleep(5)
    for i in range(100):
        if gh:
            print(text)
            time.sleep(2)
        else:
            break

def stop(event):
    threaded_run(spam(event, False))

p.bind('<Button-1>', play)
s.bind('<Button-1>', stop)

e.pack()
l.pack()
p.pack()
s.pack()

# root.resizable(False, False)
root.mainloop()