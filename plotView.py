from matplotlib import pyplot as plt
from scipy.io.wavfile import read
from calcChroma import calcChroma
from calcMFCC import calcMFCC
import numpy as np
wav_path = 'reading5-m-yxx.wav'
sr, data = read(wav_path)
chroma_feat=calcChroma(wav_path)
chroma_feat=np.array(chroma_feat)
mfcc_feat=calcMFCC(data,sr)
plt.figure()
plt.subplot(311)
plt.plot(data)
plt.subplot(312)
plt.imshow(mfcc_feat.T, origin='lower', aspect='auto', interpolation='nearest')
plt.subplot(313)
plt.imshow(chroma_feat[:100].T)
plt.show()
