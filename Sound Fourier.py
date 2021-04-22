#%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
import soundfile as sf

data, samplerate = sf.read('Ensoniq-ESQ-1-Sympy-C4.wav')
time = np.arange(0, len(data)) / samplerate

plt.plot(time,data)
plt.show()
