
from tkinter import *
from tkinter.ttk import *

from cv2 import determinant
tk=Tk()
load=Progressbar(tk,orient=HORIZONTAL,length=400,mode="determinate")

def bar():
    import time
    load["value"]=20
    tk.update_idletasks()
    time.sleep(1)
    load["value"]=50
    tk.update_idletasks()
    time.sleep(1)
    load["value"]=100
    tk.update_idletasks()
    time.sleep(1)
    load["value"]=150
    tk.update_idletasks()
    time.sleep(1)
    load["value"]=200
    tk.update_idletasks()
    time.sleep(1)
    load["value"]=400
    tk.update_idletasks()
    time.sleep(1)
load.pack()
Button(tk,text="start",command=bar).pack()
mainloop()