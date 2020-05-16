import IPython.display as ipd
import numpy as np
import pandas as pd
import librosa
import math
import matplotlib.pyplot as plt
import wave
import sys
import os
import shutil
from scipy.io import wavfile as wav
from pydub import AudioSegment
from scipy.signal import butter, sosfilt, sosfreqz


def butter_bandpass(lowpass, highpass, fs, order=3):
    nyq = 0.5 * fs
    low = lowpass / nyq
    high = highpass / nyq
    sos = butter(order, [low, high], analog=False, btype='band', output='sos')
    return sos


def butter_bandpass_filter(data, lowpass, highpass, fs, order=3):
    sos = butter_bandpass(lowpass, highpass, fs, order=order)
    y = sosfilt(sos, data)
    return y


def shannon_energy(dataset, sr):


	samples = math.floor(sr*0.001) #sr = samples/sec, need to move in 10 ms intervals
	start_frame = 0 
	end_frame = start + 2*samples

	Es = []
	
	while end_frame <= len(X):

		curr = dataset[start_frame:end_frame]
		
		Es_now = (-1/len(curr))*np.sum(np.square(curr)*np.log(np.square(curr)));
		Es.append(Es_now)

		start_frame = start_frame + samples
		end_frame = end_frame + samples


	P_t = [x - mean(Es) for x in Es]



def preprocess(audiofile):
	#original soundfile
	X, sr = librosa.load(audiofile)
	Time = np.linspace(0, len(X)/sr, num=len(X))
	X = list(X)
	sr = float(sr)

	#normalizing amplitude 
	X_norm = X/max([abs(e) for e in X])
	

	#implementation of bandpass filter

	"""
	Sample rate and desired cutoff frequencies (in Hz). 
	In the first stage, we apply a 40–500 Hz bandpass filter...
	Most heart murmurs of approximately 110–786 Hz"""

	fs = sr
	lowpass = 20.0
	highpass = 800.0

	filtered = butter_bandpass_filter(X_norm, lowpass, highpass, fs, order=3)

	#plotting side by side
	fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
	ax1.plot(Time, X_norm)
	ax1.set_title('Original sound')
	ax2.plot(Time, filtered,'red')
	ax2.set_title('After bandpass filter')
	ax2.set_xlabel('Time')
	plt.tight_layout()
	plt.show()

	return filtered


preprocess('a0002.wav')




#Plotting

# plt.figure(2)
#     plt.clf()
#     plt.plot(t, x, label='Noisy signal')