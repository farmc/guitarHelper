import sounddevice as sd
import numpy as np
import scipy.fftpack
duration = 5.5  # seconds


audio_data = [0 for _ in range(44100)]  # 44100 is the freq


def callback(indata, outdata, frames, time, status):
    global audio_data
    if status:
        print(status)
    outdata[:] = indata
    audio_data = np.concatenate((audio_data, indata[:, 0]))
    audio_data = audio_data[len(indata[:, 0]):]
    pitch = abs(scipy.fftpack.fft(audio_data)[:len(audio_data)//2])
    max_pitch = np.argmax(pitch)

    print(max_pitch)


with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))
