import matplotlib
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import time
import gc
import multiprocessing



class Sensorik():
    def __init__(self,                              Leistung_Dichte_Sender=0.00,
                 Leistung_Dichte_Empfaenger=0.00,   Leistung_Rueckgestreut=0.00,
                 Leistung_Empfaenger=0.00,          Durchmesser_Apertur=0.00,
                 Oefnnungswinkel_Beta=0.00,         Querschnitt_Rueckgestreut=0.00,
                 SimulationTime=[0],                Activated=True,
                 Objekt=0,                          FoundObjektTime=[3,4,5,6],
                 Abstand = 20,                       FoundObjektAbstand=[100,98,95,93],
                 RelativGeschw = -1000,             FoundObjektRelativGeschw=[1,0.97,0.97,0.98]):

        self.Activated                   = Activated
        self.Leistung_Dichte_Sender      = Leistung_Dichte_Sender
        self.Leistung_Dichte_Empfaenger  = Leistung_Dichte_Empfaenger
        self.Leistung_Rueckgestreut      = Leistung_Rueckgestreut
        self.Leistung_Empfaenger         = Leistung_Empfaenger
        self.Durchmesser_Apertur         = Durchmesser_Apertur
        self.Oefnnungswinkel_Beta        = Oefnnungswinkel_Beta
        self.Querschnitt_Rueckgestreut   = Querschnitt_Rueckgestreut


        #Functions from MainWindow
        self.Noise = 0
        self.SensorRange = 20


        #Functions from WindowPlot
        self.SimulationTime              = SimulationTime
        self.FoundObjektTime = FoundObjektTime


        self.Objekt                      = Objekt

        self.FoundObjektAbstand          = FoundObjektAbstand
        self.Abstand                     = Abstand


        self.FoundObjektRelativGeschw    = FoundObjektRelativGeschw
        self.RelativGeschw                = RelativGeschw

        self.AbstandTime = [0]
        self.RelativGeschwTime = [0]
        self.FoundObjekt = [0]


    def setNoise(self, Noise):
        self.Noise = Noise
        print(self.Noise)


    def setSignal(self):
        # consts:
        tstart = 0  # start time
        tend = 10  # end time
        npoints = 500 # number of samples

        t = np.linspace(tstart, tend, npoints, endpoint=False)
        rechteck_signal = signal.square(2 * np.pi * 5 * t)

    def setActivated(self):
        self.Activated = False
        time.sleep(2)
        exit(0)




    def showGraph(self):
        #matplotlib.use('TkAgg')
        #print(len(self.FoundObjekt))
        #print(len(self.SimulationTime))
        #print(self.FoundObjekt)
        #print(self.SimulationTime)
        #gc.collect()

        fig, axs = plt.subplots(3)
        fig.suptitle('Ausgaben')

        #Erkanntes Objekt
        axs[0].plot(self.SimulationTime, self.FoundObjekt, color='green',
                 linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
        axs[0].set_title('Erkanntes Objekt')
        axs[0].set_xlabel('t[s]')
        axs[0].set_ylabel('Nicht Erkannt/Erkannt')
        axs[0].set_ylim([-0.5,1.5])

        if self.Objekt == 1:
            axs[0].text(0.2, 1, "Erkennung: Objekt erkannt")
        else:
            axs[0].text(0.2, 1, "Erkennung: kein Objekt erkannt")


        #Abstand zum Objekt
        axs[1].plot(self.SimulationTime, self.AbstandTime, color='green',
                 linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
        axs[1].set_title('Entfernung zu erkanntem Objekt')
        axs[1].set_xlabel('t[s]')
        axs[1].set_ylabel('Abstand in m')
        axs[1].set_ylim([-2,250])
        axs[1].text(0.2, 200, str('Entfernung [m]: ' + str(self.Abstand)))



        #Realtivgeschwindigkeit zum Objekt
        axs[2].plot(self.SimulationTime, self.RelativGeschwTime, color='green',
                 linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
        axs[2].set_title('Realtivgeschwindigkeit gegenueber erkanntem Objekt')
        axs[2].set_xlabel('t[s]')
        axs[2].set_ylabel('Relativgeschw. in m/s')
        axs[2].set_ylim([-2,20])
        axs[2].text(0.2, 15, str('Relativegschwindigkeit: ' + str(self.RelativGeschw)))



        plt.show()



        #Naechste Position setzen
        if self.FoundObjektTime[0] == len(self.SimulationTime):
            self.Objekt = 1
            self.Abstand = self.FoundObjektAbstand[0]
            self.RelativGeschw = self.FoundObjektRelativGeschw[0]
        elif self.FoundObjektTime[1] == len(self.SimulationTime):
            self.Objekt = 1
            self.Abstand = self.FoundObjektAbstand[1]
            self.RelativGeschw = self.FoundObjektRelativGeschw[1]
        elif self.FoundObjektTime[2] == len(self.SimulationTime):
            self.Objekt = 1
            self.Abstand = self.FoundObjektAbstand[2]
            self.RelativGeschw = self.FoundObjektRelativGeschw[2]
        elif self.FoundObjektTime[3] == len(self.SimulationTime):
            self.Objekt = 1
            self.Abstand = self.FoundObjektAbstand[3]
            self.RelativGeschw = self.FoundObjektRelativGeschw[3]
        else:   #Kein Objekt gefunden
            self.Objekt = 0
            self.Abstand = -1
            self.RelativGeschw = -1000




        self.SimulationTime.append(len(self.SimulationTime))

        self.FoundObjekt.append(self.Objekt)
        self.AbstandTime.append(self.Abstand)
        self.RelativGeschwTime.append(self.RelativGeschw)

        #Warten und erneut aufrufen
        #time.sleep(1)

        if(self.SimulationTime[len(self.SimulationTime)-1] < 20):
            self.showGraph()






