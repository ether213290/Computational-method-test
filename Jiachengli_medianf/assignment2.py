#import soundfile as sf
from scipy.io import wavfile
from scipy import interpolate
import wave
import numpy as np
import unittest
import matplotlib.pyplot as plt
from tqdm import tqdm
fs, audio = wavfile.read("degraded.wav")
fsc, audioc = wavfile.read("clean.wav")
audio = audio / 32678
audioc = audioc / 32678
print(fs)
t = range(len(audio))

print(audio)
plt.subplot(4,1,1)
plt.plot(t, audio)
plt.subplot(4,1,2)
plt.plot(t, audioc)
print(fsc)
print(audioc)
audio_error = 2 * audio - audioc
plt.subplot(4,1,3)
plt.plot(t, audio_error)
plt.show()
print(2 * audio)
detection = []
for i in range (0, (len(audio_error) - 1)):
    if (abs(audio_error[i]) < 0.01):
        detect = 0
    else:
        detect = 1
    detection.append(detect)
print(detection)

def mid_filter(x, d):
    """take several numbers, return several middle numbers
    
    Args:
        x: an array of several numbers
        d: a natural number

    Returns: 
        output: returns the array of several numbers

    
    
    """
    filter_x = np.zeros((1, len(x)))
    if d % 2 == 0:
        return 'incorrect d'

    else:
        output = []
        for i in range (0, len(x) - 1):
            e = min((i + d), len(x))
            x_block = x[i : e]
            x_block = sorted(x_block)
            if (d // 2 == 0):
                filter_x[0, i] = (x[(d // 2) + i] + x[(d  // 2) + 1 + i]) / 2
            else: 
                middle = x_block[((len(x_block) ) // 2)]
                output.append(middle)
    return output

block_size = 3
actual_error = 0
COUNT = 0
for i in tqdm(range (0, len(detection))):
    if (detection[i] != 0):
        COUNT = COUNT + 1
        total_l  = 4
        s = max((i - total_l // 2) , 0)
        e = min((i + total_l // 2), len(detection))
        #print("s = ",s)
        #print("e = ",e)
        pre_x = audio[s : e]
        #audio[i] = np.mean(mid_filter(pre_x, block_size))
        array =  mid_filter(pre_x, block_size)
        audio[i] = array[total_l // 2 - 1]
print(COUNT)
print("\n" + 'DONE')
print(audio)
print(min(audio))
plt.subplot(2,1,1)
plt.plot(t, audio)
audio_error = 2 * audio - audioc
plt.subplot(2,1,2)
plt.plot(t, audio_error)
plt.show()
print(2 * audio)
MSE = np.sum((((audio * 2) - audioc) ** 2)) / COUNT
print("MSE = ", MSE)
f = wave.open('output.wav','wb')
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(fs)
f.writeframes(audio)


