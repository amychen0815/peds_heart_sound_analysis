import librosa
import numpy as np
import scipy.io.wavfile
import os, os.path, shutil
import argparse
from time_stretch import main, stretch

def pitch_shift(audiofile,label, n_steps):
	y, sr = librosa.load(audiofile, sr=16000) # y is a numpy array of the wav file, sr = sample rate
	y_shifted = librosa.effects.pitch_shift(y, sr, n_steps)
	scipy.io.wavfile.write(label,sr,y_shifted)

# new = 'a0002_new.wav'
# y_shifted.export(new, format = "wav")

files = os.listdir()
sounds = [e for e in files if e[-4:] == '.wav'];

current_directory = os.getcwd()
 #KNOWN TO WORK 

n_steps = 10
factors = 4

for sound in sounds:
	label = sound[:-4]+'_p.wav'
	new_path = os.path.join(current_directory, label)
    if not os.path.exists(new_path):
    	pitch_shift(sound,label,n_steps);
	    stretched_sound = main(sound, factor, label = label[:-5]+'t.wav')

"""


n_steps = [4,10]
factors = [1/4,4]
for sound in sounds:
	for step in n_steps:
	    label = sound[:-4]+'_p'+str(steps)+'.wav'
	    new_path = os.path.join(current_directory, label)
    	if not os.path.exists(new_path):
	        pitch_shift(sound,label,n_steps);
	        stretched_sound = main(sound, factor, label = label[:-5]+'t'+str(factor)+'.wav')

	for factor in factors:
		stretched_sound = main(sound, factor, label = label[:-5]+'t'+str(factor)+'.wav')
# for sound in sounds:
#     label = sound[:-4]+'_stretched.wav'
#     factor = 4
#     new_path = os.path.join(current_directory, label)
#     if not os.path.exists(new_path):
#         stretched_sound = main(sound, factor, label)


"""