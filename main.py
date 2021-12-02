from headerfile import *


def main():
    print("test1")
    Help = Sensorik()
    Help.setNoise()
    Help.setSignal()
    Help.showGraph()


if __name__ == '__main__':
    main()
