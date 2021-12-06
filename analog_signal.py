import matplotlib.pyplot
import numpy as np
from matplotlib import pyplot as plt


def parameters():

      digital_lambda = 90.5
      digital_frequenz = 3/digital_lambda #Frequenz = Lambda/Lichtgeschwdt ; typische Werte
      digital_frequenz = 500
      digital_amplitude = 1
      digital_pulsdauer = digital_lambda/2
      """
      digital_signal = {"Frequenz": digital_frequenz, "Amplitude": digital_amplitude, "Pulsdauer": digital_pulsdauer}



      analog_amplitude = 2 # typischer Wert 2 Volt
      analog_lambda = 905*10^-9
      t = np.linspace(0, analog_lambda, 200)

      analog_signal = {
            "Frequenz": digital_signal["Frequenz"], "Pulsdauer": digital_signal["Pulsdauer"], "Amplitude": digital_signal["Amplitude"]
      }
      sendesignal = analog_amplitude * np.sin(2*np.pi*analog_signal["Frequenz"]*t)


      N = 100 # sample count
      P = 10  # period
      D = 5   # width of pulse
      sig = np.arange(N) % P < D
      matplotlib.pyplot.plot(sig)"""


      ######## sendesignal#########
      from scipy import signal
      import numpy as np
      import matplotlib.pyplot as plt

      # consts:
      tstart = 0  # start time
      tend = 1/digital_frequenz  # end time
      print(tend)
      npoints = 10*digital_frequenz # number of samples

      d = 0.1
      delta_t = d/3
      tstart2 = delta_t  # start time
      tend2 = tend + tstart2  # end time
      npoints2 = 10 * digital_frequenz  # number of samples


      t = np.linspace(tstart, tend, npoints, endpoint=False)
      t2 = np.linspace(tstart2, tend2, npoints2, endpoint=False)
      print("delta_t")
      print(delta_t)

      # plot signal:
      plt.plot(t, signal.square((2 * np.pi * digital_frequenz * t)))
      plt.plot(t2, signal.square((2 * np.pi * digital_frequenz * t2)))
      plt.ylim(-2, 2)
      plt.title('square - square.py')
      plt.xlabel('t[ns]')
      plt.ylabel('x(t)')
      plt.grid(True, which='both')
      plt.axhline(y=0, color='k')
      plt.show()
      print("test plot sig")
