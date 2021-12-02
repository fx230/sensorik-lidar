from headerfile import *
from mainwindow import *
from tkinter import *



def main():
    root = Tk()
    WindowPop(root)

    Help = Sensorik()
    Help.setNoise()
    Help.setSignal()

    #Show Graph, if Value is activated
    if Help.Activated == True:
        Help.showGraph()

    root.mainloop()


if __name__ == '__main__':
    main()
