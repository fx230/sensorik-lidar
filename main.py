from headerfile import *
from mainwindow import *
from tkinter import *
from multiprocessing import Process



def main():
    root = Tk()


    Help = Sensorik()
    WindowPop(root, Help)
    Help.setNoise()
    Help.setSignal()

    #Show Graph, if Value is activated
    p1 = Process(target=Help.showGraph)
    p1.start()
    p1.join()




if __name__ == '__main__':
    main()
