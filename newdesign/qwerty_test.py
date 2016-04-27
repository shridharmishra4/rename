# !/usr/bin/env python
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
import Tkinter
import glob
import new
import os
import sys
import tkFileDialog

from PyQt4 import QtGui


class rename(object):
    def __init__(self):
        self.filename = []
        self.fln = []
        ui1 = rename()

        def Commondialog(self):
            self.root = Tkinter.Tk()
            self.root.withdraw()

            raw_input("Press enter to select the directory")

            dirname = tkFileDialog.askdirectory(parent=root, initialdir="/home/shridhar/Desktop",
                                                title='Please select a directory')
            print dirname
            extension = raw_input("Enter the file extension:")
            os.chdir(dirname)

        def strdelete():
            keyword = raw_input('enter string to be removed:')
            return (keyword)

        def renamen(self):
            for filename in glob.glob("*." + extension):
                initialfilename.append(filename)
                fln.append((filename.strip(keyword)))
                os.rename(filename, fln)

        def printinititalfilename():
            return (filename)

        def printfinalfilename():
            return (fln)

        ui1.pushButton.clicked.connect(commondialog)


ui1 = new.Ui_MainWindow()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui1.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
