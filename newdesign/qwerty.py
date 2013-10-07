
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MainClientWindow.py
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
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSignal,pyqtSlot
import sys
import os
import Tkinter
import tkFileDialog
import re
import glob
import new

class rename():
    def __init__(self):
    #self.data = []
    
        
        
        
        
        
        def Commondialog(self):
                self.root = Tkinter.Tk()
                self.root.withdraw()
                
                raw_input("Press enter to select the directory")
                
                dirname=tkFileDialog.askdirectory(parent=root,initialdir="/home/shridhar/Desktop",title='Please select a directory')
                print dirname
                extension=raw_input("Enter the file extension:")
                #length=len(extension)
                os.chdir(dirname)
        #def renamen(self       
                keyword=raw_input('enter string to be removed:')
                
                
                    
                for filename in glob.glob("*."+extension):
                    #if end=='0':
                        #end=str(len(filename))
                    initialfilename = filename
                    fln=filename.strip(keyword)
                   
                    os.rename(filename, fln)
                    #newfilename=filename[:-(length+1)]
                    ##print newfilename
                    #os.rename(newfilename, (newfilename[int(start):int(end)] + '.'+extension))
                    print filename
                    print fln
                    print "\n"
                    
                
                #newfilename=[]    
                    
                #for filename in glob.glob("*."+extension):
                    #if end=='0':
                        #end=str(len(filename))
                    #initialfilename = filename
                    
                    #os.rename(filename, filename[:-(length+1)])
                    #newfilename=filename[:-(length+1)]
                    ##print newfilename
                    #os.rename(newfilename, (newfilename[int(start):int(end)] + '.'+extension))
                    #print filename
                    #print newfilename
                    #print "\n"
                    
                
                                        
                    
                
                    
                

                
                
  #              k=glob.glob(dirname+"/*."+extension)
 
                
                
  #              print k
##                
##                for i in range(0,3):
##                        newnames=tkFileDialog.askopenfilenames(parent=root)
##                        filenames+=newnames+'\n'
##                        
##                        #print filenames
##                initialfilename = re.split("\}\W\{", filenames[1:-1])
##                print filenames
##                return(filenames)
##        oldfilenames=[]
##        for i in range(0,3):
##               oldfilenames.append(Commondialog(0,0))
##               
##        print oldfilenames
                
                


        
        #def start():
               #start=raw_input()
                
                
        #def end():
               #end=raw_input()
                
                
        #def printinititalfilename():
                #print initialfilename
        
        
        #def printfinalfilename():
                #print finalfilename
        
#        c=Commondialog(0)
##        a=Ui_MainWindow
##        b=a.setupUi
##        exec c
        
        ##        renamen.Ui_MainWindow.setupUi(a,b)

        
##        a.start.clicked.connect(self.start)
##        a.end.clicked.connect(self.end)                      



ui=new.Ui_MainWindow()

if __name__=="__main__":    
        
        app = QtGui.QApplication(sys.argv)
        mainWindow=QtGui.QMainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        mainWindow.show()
#        comm = MainClientWindow()
#        comm.show()
        sys.exit(app.exec_())
        


