import librosa
#import numpy as np

#read in data
filename = './data/audio/Y11-K1.wav'
audio_time_series, sampling_rate = librosa.load(filename)

tempo, beats = librosa.beat.beat_track(y=audio_time_series, sr=sampling_rate)

print(tempo)
