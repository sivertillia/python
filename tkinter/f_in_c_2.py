import tkinter as tk
from typing import Text

root = tk.Tk()
root.title('Конвертатор')

def f_in_c():
    # (°F − 32) × 5/9
    try:
        print('Try')
        f = float(f_entry.get())
        result = (f - 32) * 5/9
        label_fc['text'] = f'{round(result, 2)} \N{DEGREE CELSIUS}'
        return True
    except:
        print('Error')
        return False

def c_in_f():
    # (°C × 9/5) + 32
    c = float(c_entry.get())
    result = (c * 9/5) + 32
    label_cf['text'] = f'{round(result, 2)} \N{DEGREE FAHRENHEIT}'


frame_f_in_c = tk.Frame(master=root)
frame_c_in_f = tk.Frame(master=root)

f_entry = tk.Entry(master=frame_f_in_c, width=10, validate='key', validatecommand=f_in_c, invalidcommand=ValueError) # 1
f_entry.insert(tk.END, 0)
label_f_temp = tk.Label(master=frame_f_in_c, text='\N{DEGREE FAHRENHEIT}') # 2
label_fc = tk.Label(master=frame_f_in_c, text='-17.78 \N{DEGREE CELSIUS}') # 4


c_entry = tk.Entry(master=frame_c_in_f, width=10, text='0') # 1
c_entry.insert(tk.END, 0)

label_c_temp = tk.Label(master=frame_c_in_f, text='\N{DEGREE CELSIUS}') # 2
label_cf = tk.Label(master=frame_c_in_f, text='32.0 \N{DEGREE FAHRENHEIT}') # 4


f_entry.grid(row=0, column=0, padx=15, pady=15)
label_f_temp.grid(row=0, column=1)
label_fc.grid(row=0, column=2, padx=15)

c_entry.grid(row=1, column=0, padx=15, pady=15)
label_c_temp.grid(row=1, column=1)
label_cf.grid(row=1, column=2, padx=15)

if __name__ == '__main__':
#     f.pack()
#     c.pack()
#     # label_c.pack()
    frame_f_in_c.pack()
    frame_c_in_f.pack()
    root.mainloop()