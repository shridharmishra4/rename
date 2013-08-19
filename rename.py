import os
import glob
for filename in glob.glob('*.mp3'):
    if len(filename) > 18:
        os.rename(filename, filename[:-18] + '.mp3')
