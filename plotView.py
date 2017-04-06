from matplotlib import pyplot as plt
from scipy.io.wavfile import read

wav_path = 'reading5-m-yxx.wav'
sr, data = read(wav_path)
plt.figure()
plt.plot(data)
plt.show()
