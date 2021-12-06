import matplotlib.pyplot
import numpy as np
from matplotlib import pyplot as plt


def parameters():

      digital_lambda = 905*10^-9

      digital_frequenz = digital_lambda/2.99792458*10**8 #Frequenz = Lambda/Lichtgeschwdt ; typische Werte
      digital_amplitude = 1
      digital_pulsdauer = digital_lambda/2

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
      matplotlib.pyplot.plot(sig)
      print("test plot sig")
