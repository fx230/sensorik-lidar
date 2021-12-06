from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


def parameters():

      digital_lambda = 90.5
      # digital_frequenz = 3/digital_lambda #Frequenz = Lichtgeschwdt/lambda ; typische Werte
      digital_frequenz = 240 # gigaHz
      digital_amplitude = 1
      digital_pulsdauer = digital_lambda/2


      ######## sendesignal#########

      # consts:
      tstart = 0  # start time
      tend = 1 / digital_frequenz  # end time
      print(tend)
      npoints = 10 * digital_frequenz  # number of samples

      d = 40
      delta_t = d / 3
      tstart2 = delta_t  # start time
      tend2 = tend + tstart2  # end time
      npoints2 = 10 * digital_frequenz  # number of samples

      t = np.linspace(tstart, tend, npoints, endpoint=False)
      t2 = np.linspace(tstart2, tend2, npoints2, endpoint=False)
      print("distanz:")
      calc_distanz = 2 * (tstart2 - tstart) * 1.5
      print(calc_distanz)

      Noise = False

      if Noise:
            noisepeak = 0.1
            noise = np.random.uniform(-noisepeak, noisepeak, npoints2)
            # plot signal:
            plt.plot(t, signal.square((2 * np.pi * digital_frequenz * t)))
            plt.plot(t2, signal.square((2 * np.pi * digital_frequenz * t2)) + noise)
            plt.ylim(-2, 2)
            plt.title('square - square.py')
            plt.xlabel('t[ns]')
            plt.ylabel('x(t)')
            plt.grid(True, which='both')
            plt.axhline(y=0, color='k')
            plt.show()
            print("test plot sig")

      else:

            noisepeak = 0.1
            noise = np.random.uniform(-noisepeak, noisepeak, npoints2)
            # plot signal:
            plt.plot(t, signal.square(2 * np.pi * digital_frequenz * t))
            plt.plot(t2, signal.square(2 * np.pi * digital_frequenz * t2))
            plt.ylim(-2, 2)
            plt.title('square - square.py')
            plt.xlabel('t[ns]')
            plt.ylabel('x(t)')
            plt.grid(True, which='both')
            plt.axhline(y=0, color='k')
            plt.show()
            print("test plot sig")


