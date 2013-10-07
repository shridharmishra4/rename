import os
import glob
count=0
start=raw_input('enter start value')
end=raw_input('enter end value')
for filename in glob.glob('*.mp3'):
	count+=1
    if len(filename) > 18:
        os.rename(filename, filename[start:end] + '.mp3')
