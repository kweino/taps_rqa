import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

audio_file = 'Y11-K1.wav'

audio_time_series, sampling_rate = librosa.load(audio_file)
tempo, beats = librosa.beat.beat_track(y=audio_time_series,
                                        sr=sampling_rate, units='time')
pulse = librosa.beat.plp(y=audio_time_series,sr=sampling_rate, tempo_min=50, tempo_max=70)
beats_plp = np.flatnonzero(librosa.util.localmax(pulse))
times = librosa.times_like(pulse, sr=sr)

ioi_bt = np.diff(beats)
ioi_plp = np.diff(beats_plp)

print(ioi_bt, ioi_plp)

# R_ioi = librosa.segment.recurrence_matrix(ioi)
# #Test time-delay embedding for cleaner recurrence matrices
# ioi_stack = librosa.feature.stack_memory(ioi, delay=3)
# R_stack = librosa.segment.recurrence_matrix(ioi_stack)
#
#
# # Plotting
# fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True)
# imgsim = librosa.display.specshow(R_ioi, x_axis='s', y_axis='s',
#                         ax=ax[0])
# ax[0].set(title='IOI recurrence')
# imgaff = librosa.display.specshow(R_stack, x_axis='s', y_axis='s',
#                         cmap='magma_r', ax=ax[1])
# ax[1].set(title='Stacked IOI recurrence')
# ax[1].label_outer()
# plt.show()
