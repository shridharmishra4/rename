import os
from glob import glob
import Tkinter
import tkFileDialog
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

for dir,_,_ in os.walk(start_dir):
	files.extend(glob(os.path.join(dir,pattern)))
for file in files:
	filenames.append(os.path.basename(file))


filenames.sort()
print filenames

	


print len(files)



length= len(flienames)
title=[]
artist=[]
album=[]                   



#from mutagen.mp3 import MP3
#audio = MP3("Aisha.mp3")
#print audio.info.length, audio.info.bitrate,audio.title
#id3.getall('TTTT') == []
m= mutagen.File(filenames[0], easy=True)
for i in xrange (length):
    m= mutagen.File(filenames[i], easy=True)
    #title.append(m['title'])
    #artist.append(m['artist'])
    #album.append(m['album'])
    print """
             %s 
             %s  
             %s""" %(m['title'],m['artist'],m['album'])




    

#for e in os.walk(os.getcwd()):
    #print e
