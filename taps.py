"""
Original I/O code from FlamingLasrSwrd (https://github.com/FlamingLasrSwrd/taps)
This version leverages librosa to capture more accurate timing information
"""


import os
import logging
import csv
import librosa
import numpy as np
import matplotlib.pyplot as plt

from clargs import parser
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.ERROR)

#collect files from user input
files = []
if args.input:
    [files.append(i) for i in args.input]
else:
    all_files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in all_files:
        root, ext = os.path.splitext(f)
        if ext == '.wav':
            files.append(f)

#audio processing
big_data = []

for f in files:
    audio_time_series, sampling_rate = librosa.load(f)
    tempo, beats = librosa.beat.beat_track(y=audio_time_series, sr=sampling_rate, units='time')

    ioi = np.diff(beats)

    # some basic info about each file
    logging.info(f'For file: {f}')
    logging.info(f'Time between taps (s): {ioi}')
    logging.info(f'Average IOI +- std. dev.(s): {np.mean(ioi):.2} +- {np.std(ioi):.2}')

    data = [f]
    [data.append(d) for d in ioi]
    big_data.append(data)

#output to csv
if args.append:
    type = 'a'
else:
    type = 'w'
with open(args.out, type) as csv_file:
    writer = csv.writer(csv_file)
    if type != 'a':
        writer.writerow(['filename', 'Time between taps in seconds'])
    for d in big_data:
        writer.writerow(d)
