from headerfile import *
from mainwindow import *
from tkinter import *
import multiprocessing as mp



def main():
    root = Tk()


    Help = Sensorik()
    WindowPop(root, Help)
    Help.setNoise()
    Help.setSignal()

    #Show Graph, if Value is activated
    Help.showGraph()




if __name__ == '__main__':
    main()
