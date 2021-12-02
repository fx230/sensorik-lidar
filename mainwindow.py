from headerfile import*
from main import *
import sys
from tkinter import *
from tkinter import ttk

def WindowPop(root, Help):
    content = ttk.Frame(root)

    frame = ttk.Frame(content, borderwidth=6, relief="ridge", width=400, height=200)
    namelbl = ttk.Label(content, text="LiDar Signalgenerator")
    namelbl_sensorrange = ttk.Label(content, text="Sensorrange")
    name = ttk.Entry(content)


    ##########Declarations########################
    i_number_of_layers = BooleanVar(value=False)
    b_reflexion = BooleanVar(value=False)
    b_cushioning = BooleanVar(value=False)
    b_doppler = BooleanVar(value=False)
    f_sensorrange = 70.00
    f_field_of_view = 1.00

    ########### Slider ###########################
    sensorrange = Scale(content, from_=20.00, to=70.00, orient=HORIZONTAL, variable=f_sensorrange)
    #filedofview = Scale(content, from_=0.00, to=10.00, variable=f_field_of_view)

    ###########Radiobuttons#####################
    one = ttk.Checkbutton(content, text="Two layer", variable=i_number_of_layers, onvalue=True)
    two = ttk.Checkbutton(content, text="Reflexion", variable=b_reflexion, onvalue=True)
    three = ttk.Checkbutton(content, text="Cushioning", variable=b_cushioning, onvalue=True)
    four = ttk.Checkbutton(content, text="Doppler", variable=b_doppler, onvalue=True)

    ############Buttons###################
    ok = ttk.Button(content, text="Generate", command=Help.showGraph)
    cancel = ttk.Button(content, text="Exit", command=sys.exit)



    ###############position#################
    content.grid(column=0, row=0)
    namelbl.grid(column=0, row=0, columnspan=2)
    #name.grid(column=0, row=1, columnspan=2)

    sensorrange.grid(column=1, row=2)
    one.grid(column=1, row=3, sticky=W)
    two.grid(column=1, row=4, sticky=W)
    three.grid(column=1, row=5, sticky=W)
    # four.grid(column=1, row=6, sticky=W)  doppler
    ok.grid(column=2, row=7, sticky=E)
    cancel.grid(column=3, row=7, sticky=E)

    root.mainloop()


