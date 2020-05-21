import csv
import os, os.path, shutil

#Dictionary of sound labels
with open('REFERENCE.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('REFERENCE_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}



#Filter all files to leave only .wav
current_directory = os.getcwd()
sounds = [e for e in os.listdir("current_directory") if os.path.isfile(os.path.join(current_directory, e))]
wav_filter = []
for sound in sounds:
    if sound[-4:] == ".wav" and sound not in wav_filter:
        wav_filter.append(sound)


for wav in wav_filter:
    
    label = mydict[wav[:-4]]
    new_directory = os.path.join(current_directory, label)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    
    old_wav_path = os.path.join(current_directory, wav)
    new_wav_path = os.path.join(new_directory, wav)
    shutil.move(old_wav_path, new_wav_path)