import tkinter as tk

root = tk.Tk()
root.title('Конвертатор')

def f_in_c():
    # (°F − 32) × 5/9
    f = float(f_entry.get())
    result = (f - 32) * 5/9
    label_fc['text'] = f'{round(result, 2)} \N{DEGREE CELSIUS}'

def c_in_f():
    # (°C × 9/5) + 32
    c = float(c_entry.get())
    result = (c * 9/5) + 32
    label_cf['text'] = f'{round(result, 2)} \N{DEGREE FAHRENHEIT}'
frame_f_in_c = tk.Frame(master=root)
frame_c_in_f = tk.Frame(master=root)

f_entry = tk.Entry(master=frame_f_in_c, width=10) # 1
label_f_temp = tk.Label(master=frame_f_in_c, text='\N{DEGREE FAHRENHEIT}') # 2
btn_convert_f = tk.Button(master=frame_f_in_c, text='\N{RIGHTWARDS BLACK ARROW}', command=f_in_c) # 3
label_fc = tk.Label(master=frame_f_in_c, text='\N{DEGREE CELSIUS}') # 4


c_entry = tk.Entry(master=frame_c_in_f, width=10) # 1
label_c_temp = tk.Label(master=frame_c_in_f, text='\N{DEGREE CELSIUS}') # 2
btn_convert_c = tk.Button(master=frame_c_in_f, text='\N{RIGHTWARDS BLACK ARROW}', command=c_in_f) # 3
label_cf = tk.Label(master=frame_c_in_f, text='\N{DEGREE FAHRENHEIT}') # 4


f_entry.grid(row=0, column=0, padx=15, pady=15)
label_f_temp.grid(row=0, column=1)
btn_convert_f.grid(row=0, column=2)
label_fc.grid(row=0, column=3, padx=15)

c_entry.grid(row=1, column=0, padx=15, pady=15)
label_c_temp.grid(row=1, column=1)
btn_convert_c.grid(row=1, column=2)
label_cf.grid(row=1, column=3, padx=15)

if __name__ == '__main__':
#     f.pack()
#     c.pack()
#     # label_c.pack()
    frame_f_in_c.pack()
    frame_c_in_f.pack()
    root.mainloop()