import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

audio_file = 'Y11-K1.wav'

audio_time_series, sampling_rate = librosa.load(audio_file)
tempo, beats = librosa.beat.beat_track(y=audio_time_series,
                                        sr=sampling_rate, units='time')

ioi = np.diff(beats)


R_ioi = librosa.segment.recurrence_matrix(ioi)
# Use time-delay embedding to get a cleaner recurrence matrix
ioi_stack = librosa.feature.stack_memory(ioi, delay=3)
R_stack = librosa.segment.recurrence_matrix(ioi_stack)


# Plotting
fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True)
imgsim = librosa.display.specshow(R_ioi, x_axis='s', y_axis='s',
                        ax=ax[0])
ax[0].set(title='IOI recurrence')
imgaff = librosa.display.specshow(R_stack, x_axis='s', y_axis='s',
                        cmap='magma_r', ax=ax[1])
ax[1].set(title='Stacked IOI recurrence')
ax[1].label_outer()
plt.show()
