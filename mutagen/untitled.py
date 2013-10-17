#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013 shridhar <shridhar@shridhar>
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
                 
filenames=glob.glob("*.mp3")
#for files in filenames:
    #print files
    #filenames.append(files)
    
    
     
         
        

title=[]
artist=[]
album=[]                   


length=len(filenames)
#from mutagen.mp3 import MP3
#audio = MP3("Aisha.mp3")
#print audio.info.length, audio.info.bitrate,audio.title
#id3.getall('TTTT') == []
m= mutagen.File(filenames[0], easy=True)
print m['title']
for i in range (0,length):
    m= mutagen.File(filenames[i], easy=True)
    #title.append(m['title'])
    #artist.append(m['artist'])
    #album.append(m['album'])
    print """
             %s 
             %s  
             %s""" %(m['title'],m['artist'],m['album'])




    
    



def main():
    
    return 0

if __name__ == '__main__':
    main()

