from scipy.io import wavfile
from scipy import interpolate
import wave
import numpy as np
import unittest
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
"second part: change the filter to the spline filter"
fs_2, audio_2 = wavfile.read("degraded.wav")
fsc_2, audioc_2 = wavfile.read("clean.wav")
audio_2 = audio_2 / 32678
audioc_2 = audioc_2 / 32678
print(fs_2)
t_2 = range(len(audio_2))
print(audio_2)
plt.subplot(3,1,1)
plt.plot(t_2, audio_2)
plt.subplot(3,1,2)
plt.plot(t_2, audioc_2)
plt.show()
print(fsc_2)
print(audioc_2)
audio_error = 2 * audio_2 - audioc_2
print(2 * audio_2)
COUNT = 0
detection = []
x_origin = []
x_interp = []
for i in range (0, (len(audio_error) - 1)):
    if (abs(audio_error[i]) < 0.1):
        detect = 0
        x = i
        x_origin.append(x)
    else:
        detect = 1
        COUNT = COUNT + 1
        x_in = i
        x_interp.append(x_in)
    detection.append(detect)
    
    
print(detection)
print(COUNT)
block_size = 3
actual_error = 0
y_origin = []
for i in range (0, len(detection)):
    if (detection[i] != 0):
        a = i
    else:    
        y = audio_2[i]
        y_origin.append(y)   

print(len(x_origin))
print(len(y_origin))
print(x_origin)
print(y_origin)
#y_interp = np.interp(x_interp, x_origin, y_origin)
cs = CubicSpline(x_origin, y_origin)
y_interp = cs(x_interp)
for i in range (0, len(x_interp)):
    audio_2[x_interp[i]] = y_interp[i]

plt.subplot(3,1,1)
plt.plot(x_origin, y_origin, 'o', label='data')
plt.plot(x_interp, y_interp, label='cubic spline')
plt.legend()



print(audio_2)
print(min(audio_2))
plt.subplot(3,1,2)
plt.plot(t_2, 2 * audio_2)
audio_error = 2 * audio_2 - audioc_2
plt.subplot(3,1,3)
plt.plot(t_2, audio_error)
plt.show()
print(2 * audio_2)
MSE = np.sum((((audio_2 * 2) - audioc_2) ** 2)) / COUNT
print("MSE = ", MSE)
f = wave.open('output_2.wav','wb')
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(fs_2)
f.writeframes(audio_2)

