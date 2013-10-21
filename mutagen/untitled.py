#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013 Shridhar Mishra <shridhar@shridhar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import mutagen
import sys
import os
import Tkinter
import tkFileDialog
import glob
from mutagen import id3
from glob import glob
from mutagen import *




#from mutagen.easyid3 import EasyID3
#print EasyID3.valid_keys.keys()
def Commondialog():
                root = Tkinter.Tk()
                root.withdraw()
                
                raw_input("Press enter to select the directory")
                
                dirname=tkFileDialog.askdirectory(parent=root,initialdir="/home/shridhar/Desktop",title='Please select a directory')
                print dirname
                #extension=raw_input("Enter the file extension:")
                #length=len(extension)
                os.chdir(dirname)
                
                
                
                
Commondialog()
files = []
filenames = []
start_dir = os.getcwd()
pattern   = "*.mp3"

for dir ,_,_ in os.walk(start_dir):
	files.extend(glob(os.path.join(dir,pattern)))   
for file in files:
	filenames.append(os.path.basename(file)) 
files.sort()
#filenames.sort()
print filenames


print """ 
         Number of songs in the folder ==> %s""" %(len(files))

	


    
     
         
        
length= len(files)
title=[]
artist=[]
album=[]                   



#from mutagen.mp3 import MP3
#audio = MP3("Aisha.mp3")
#print audio.info.length, audio.info.bitrate,audio.title
#id3.getall('TIT2') == [id3['TIT2']]
#m= mutagen.File(filenames[0], easy=True)
for i in xrange (length):
    m= mutagen.File(files[i], easy=True)
    title.append(m['title'])
    artist.append(m['artist'])
    album.append(m['album'])
    print """
             %s 
             %s  
             %s""" %(m['title'],m['artist'],m['album'])
 
      
def main():
    
    return 0

if __name__ == '__main__':
    main()

