import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

raw_content = wave.open("/content/drive/MyDrive/Recording_5.wav", "r")

# Extract Raw Audio from Wav File
signal = raw_content.readframes(-1)

# convert signal to numpy array
signal = np.fromstring(signal, "Int16")

# plt.figure(1)
# plt.title("clap waves")
# plt.plot(signal)
# plt.show()

test_list = list(signal)

local_maxima = []
local_minima = []

for index in range(len(test_list)+2):
    if test_list[index - 1] > test_list[index] < test_list[index + 1]:
        local_minima.append(i)
        print(local_minima)
    elif test_list[index - 1] < test_list[index] > test_list[index + 1]:
        local_maxima.append(i)