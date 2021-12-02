#from tkinter import *
#tk = Tk()


#tk.title("LiDAR Signalgenerator")
#tk_mainwindow = Button(tk, text="Generate")
#tk_mainwindow.pack(padx=500, pady=500)
#tk.mainloop()
import sys
from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

i_number_of_layers = 1
b_reflexion = BooleanVar(value=False)
b_cushioning = BooleanVar(value=True)
b_doppler = BooleanVar(value=True)

one = ttk.Checkbutton(content, text="Number of Layers", variable=i_number_of_layers, onvalue=True)
two = ttk.Checkbutton(content, text="Reflexion", variable=b_reflexion, onvalue=True)
three = ttk.Checkbutton(content, text="Cushioning", variable=b_cushioning, onvalue=True)
four = ttk.Checkbutton(content, text="Doppler", variable=b_doppler, onvalue=True)
ok = ttk.Button(content, text="Generate")
cancel = ttk.Button(content, text="Exit", command=sys.exit)

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.mainloop()

