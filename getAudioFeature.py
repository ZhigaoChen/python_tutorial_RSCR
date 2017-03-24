from scipy.io.wavfile import read

from calcChroma import calcChroma
from  calcMFCC import calcMFCC

# mfcc
fs, signal = read('test.wav')
calcMFCC(signal, fs)
# chroma
calcChroma('test.wav')
