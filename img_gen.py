! pip install ffmpeg

import IPython.display as ipd
import numpy as np
import pandas as pd
import librosa
import librosa.display
import math
import matplotlib.pyplot as plt
import wave
import sys
import os, os.path, shutil
import shutil
from scipy.io import wavfile as wav
from pydub import AudioSegment
from scipy import signal
from scipy.signal import butter, sosfilt, sosfreqz

files = os.listdir()
sounds = [e for e in files if e[-4:] == '.wav'];

#Bandpass Filter
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


#Arbitrary Interception
def truncate (original, start, end):
    newAudio = original[start*1000:end*1000]
    return newAudio


#Mel Spectrogram Image Generation
def sound_to_spec(audiofile):
    sample, sr = librosa.load(audiofile)
    Time = np.linspace(0, len(sample)/sr, num=len(sample))
    sr = float(sr)
    
    #normalize X
    X = list(sample)
    X_norm = X/max([abs(e) for e in X])
    
    #bandpass filter X
    fs = sr
    lowpass = 20.0
    highpass = 800.0
    filtered = butter_bandpass_filter(X_norm, lowpass, highpass, fs, order=3)
    
    #truncate filtered X
    start = 0
    end = 30 #seconds
    
    try:
        input_audio = truncate(filtered, start, end)
        filtered = input_audio
    except:
        pass
    
    
    """
    #regular spectrogram (I personally can't see anything so commenting out for now)
    frequencies, times, spectrogram = signal.spectrogram(input_audio, sr)
    plt.pcolormesh(times, frequencies, spectrogram)
    plt.imshow(spectrogram)
    """
    
    #mel spectrum
    n_fft = 2048
    hop_length = 512
    n_mels = 128
    
    S = librosa.feature.melspectrogram(filtered, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels, fmax=800)
    S_DB = librosa.power_to_db(S, ref=np.max)
    plt.figure();
    #add x_axis='time', y_axis='mel' in the function to see x = Time, y = Hertz
    librosa.display.specshow(S_DB, sr=sr, hop_length=hop_length); 
    
    
    #saving generated pic to folder
    plt.savefig(audiofile[:-4] + '.png',transparent = True);
    plt.close();

#Run through all sounds in the folder
current_directory = os.getcwd()
for sound in sounds:
    label = sound[:-4]+'.png'
    new_path = os.path.join(current_directory, label)
    if not os.path.exists(new_path):
        sound_to_spec(sound);
