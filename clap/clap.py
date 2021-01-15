import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

def count_claps(signal, min_threshold, max_threshold):

    result = []

    for i in signal:
        if min_threshold < i > max_threshold:
            result.append(round(signal.index(i), -4))
 
    final_result = len(set(result))

    return final_result
    

def main():

    raw_content = wave.open("clap_sound.wav", "r")

    # Extract Raw Audio from Wav File
    signal = raw_content.readframes(-1)

    # convert signal to numpy array
    signal = np.fromstring(signal, "Int16")

    # visualize signal
    # plt.figure(1)
    # plt.title("clap waves")
    # plt.plot(signal)
    # plt.show()
    
    # code
    signal = list(signal)

    res = count_claps(signal, 0, 1000)
    print("No. of claps = ",res)

    return 

if __name__ == "__main__":
    main()

