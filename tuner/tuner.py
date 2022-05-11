from random import sample
import sounddevice as sd
import numpy as np


class Tuner:

    def __init__(self):
        pass

    def tune(self):
        '''
        Active tuner that listens to input
        '''
        def callback(indata, frames, time, status):
            inputData = np.array([])
            if status:
                print(status)

            if indata.any():
                inputData = np.concatenate((inputData, indata[:, 0]))
                inputData = inputData[len(indata[:, 0]):]
                print(inputData)
        with sd.InputStream(callback=callback):

            while True:
                response = input()
                if response in ('', 'q', 'Q'):
                    break

    def play_fequency(self, note, octave=None):
        '''
        play the note and octave if specified
        '''
        pass
