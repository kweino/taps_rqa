# taps_rqa
 taps.py transforms audio files of tempo taps into CSV files of inter-onset intervals (IOIs). 
 
 rqa_plot.py performs RQA analyses on the IOIs from audio files and plots the results.

# Using taps.py
 From the root directory:

 ```bash
 python taps.py
 ```
 The basic use of `taps.py` will scan the calling directory for any file with the `.wav` extension and attempt to find the peaks. A `.csv` file will be made with the time differential of the detected taps.

 ```bash
 python taps.py -o new_filename.csv
 ```
 Outputs to `new_filename.csv` instead of the default file: `output.csv`.

 ```bash
 python taps.py -i file1.wav file2.wav
 ```
 Only processes `file1.wav` and `file2.wav`.

 ```bash
 python taps.py -i file3.wav -a
 ```
 Append the results of `file3.wav` processing to the `output.csv` file instead of overwriting. Useful for processing files individually without losing all your work.

 ```bash
 python taps.py -v
 ```
 Prints some information about the analysis of each file to the screen.

 # Testing
 A sample wave file is included for testing the installation:

 ```bash
 python taps.py -i test.wav
 ```
