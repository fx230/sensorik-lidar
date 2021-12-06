from headerfile import *
from mainwindow import *
from tkinter import *
import multiprocessing as mp



def main():
    root = Tk()


    Help = Sensorik()
    #WindowPop(root, Help)
    Help.setNoise()
    Help.setSignal()

    #Show Graph, if Value is activated
    #Help.showGraph()


    from multiprocessing import Pool
    pool = Pool()
    result1 = pool.apply_async(WindowPop, [root, Help])    # evaluate "solve1(A)" asynchronously
    result2 = pool.apply_async(Help.showGraph())    # evaluate "solve2(B)" asynchronously
    result1.get(timeout=10)
    result2.get(timeout=10)



if __name__ == '__main__':
    main()
