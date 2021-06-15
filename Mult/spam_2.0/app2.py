import time
import tkinter as tk

import multiprocessing

root = tk.Tk()
spam_num = False
print('spam /: ',spam_num)
textSpam = tk.Entry(master = root, width=20)

def starter_gl_pr():
    global spam_num
    spam_num = widthSpam.get()
    print('Spam:', spam_num)




def play():
    threaded_run()
    

def spam(a, b, c, d):
    global spam_num
    textasda = textSpam.get()
    spam_num = int(spam_num)
    print('spam fun: ',spam_num)
    # time.sleep(5)
    while 0 <= spam_num:
        print(textasda, spam_num)
        spam_num = spam_num-1
        time.sleep(2)
    return

def threaded_run():
    starter_gl_pr()
    thr = multiprocessing.Process(target=spam, args=(1, 2), kwargs={"c": 3, "d": 4})
    thr.start()
    check_status(thr)
    return

def stop():
    global spam_num
    spam_num = 0

def check_status(mp):
    """ p is the multiprocessing.Process object """
    if mp.is_alive(): # Then the process is still running
        startBtn.config(state = "disabled")
        root.after(200, lambda mp=mp: check_status(mp)) # After 200 ms, it will check the status again.
    else:
        startBtn.config(state = "normal")
    return





if __name__ == "__main__":
    textSpam.pack()
    widthSpam = tk.Entry(master = root, width=20)
    widthSpam.pack()
    startBtn = tk.Button(master = root, text="Start", width=14, command=threaded_run)
    startBtn.pack()
    stopBtn = tk.Button(master = root, text="Stop", width=14, command=stop)
    stopBtn.pack()
    
    root.mainloop()