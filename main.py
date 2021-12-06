from headerfile import *
from analog_signal import *


from tkinter import *
import multiprocessing as mp

from main import *
import sys
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk


def main():

    Help = Sensorik()

    ws = Tk()
    ws.title('Lidar Sensorik Projekt')
    ws.geometry('500x270')

    def isChecked():
        if cb.get() == 1:
            #btn['state'] = NORMAL
            #btn.configure(text='Noise')
            Help.setNoise(1)
        elif cb.get() == 0:
            #btn['state'] = DISABLED
            #btn.configure(text=Help.SensorRange)
            Help.setNoise(0)
        else:
            messagebox.showerror('Lidar Sensorik', 'Something went wrong!')

    def showErkannteObjekte():
       if int(Help.Abstand) < int(Help.SensorRange):
           Help.FoundObjektAbstand = [Help.Abstand, Help.Abstand, Help.Abstand, Help.Abstand]
           Help.FoundObjektTime = [3, 4, 5, 6]
       else:
           Help.FoundObjektAbstand = [-1,-1,-1,-1]
           Help.FoundObjektTime = [3000, 3001, 3002, 3003]
       Help.showGraph()

    def showRohdaten():
       #Help.Analog_Signal()
       if int(Help.Abstand) < int(Help.SensorRange):
           Help.Objekt = 1
           Help.FoundObjektAbstand = [Help.Abstand, Help.Abstand, Help.Abstand, Help.Abstand]
           Help.FoundObjektTime = [3, 4, 5, 6]
       else:
           Help.Objekt = 0
           Help.FoundObjektAbstand = [-1, -1, -1, -1]
           Help.FoundObjektTime = [3000, 3001, 3002, 3003]
       print(Help.Objekt)
       parameters(Help)

    def setRange(Range):
        Help.SensorRange = Range

    def setObjektRange(Range):
        Help.Abstand = Range
        Help.FoundObjektAbstand = [Range, Range, Range, Range]

    def Exit():
        sys.exit(0)


    cb = IntVar()

    separator = ttk.Separator(ws, orient='horizontal')
    separator.pack(fill='x')

    text = Text(ws, state='disabled', height=1)
    text.configure(state='normal')
    text.insert('end', 'Noise')
    text.configure(state='disabled')
    text.pack(side=TOP, anchor=W)

    Checkbutton(ws, text="Activate Noise", variable=cb, onvalue=1, offvalue=0, command=isChecked).pack(side=TOP, anchor=W)

    text = Text(ws, state='disabled', height=1)
    text.configure(state='normal')
    text.insert('end', 'Objektentfernung in [m]')
    text.configure(state='disabled')
    text.pack(side=TOP, anchor=W)

    Objektentfernung = Scale(ws, from_=0.00, to=70.00, orient=HORIZONTAL, command=setObjektRange)
    Objektentfernung.pack(side=TOP, anchor=W)


    text = Text(ws, state='disabled', height=1)
    text.configure(state='normal')
    text.insert('end', 'Sensorrange in [m]')
    text.configure(state='disabled')
    text.pack(side=TOP, anchor=W)

    SensorRange = Scale(ws, from_=0.00, to=200.00, orient=HORIZONTAL, command=setRange)
    SensorRange.pack(side=TOP, anchor=W)


    Rohdaten = Button(ws, text='Show <Rohdaten>', padx=20, pady=5, command=showRohdaten)
    Rohdaten.pack(padx=5, pady=15, side=tk.LEFT)

    ErkannteObjekte = Button(ws, text='Show <Erkannte Objekte>', padx=20, pady=5, command=showErkannteObjekte)
    ErkannteObjekte.pack(padx=5, pady=15, side=tk.LEFT)

    exit = Button(ws, text='EXIT', state=ACTIVE, padx=20, pady=5, command=Exit)
    exit.pack(padx=5, pady=15, side=tk.LEFT)


    ws.mainloop()

if __name__ == '__main__':
    main()
