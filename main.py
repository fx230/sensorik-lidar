from headerfile import *
from mainwindow import *
from tkinter import *



def main():
    root = Tk()


    Help = Sensorik()
    WindowPop(root, Help)
    Help.setNoise()
    Help.setSignal()

    #Show Graph, if Value is activated
    if Help.Activated:
        Help.showGraph()




if __name__ == '__main__':
    main()
