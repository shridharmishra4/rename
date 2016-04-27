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


class rename():
    def __init__(self):
        # self.data = []

    def Commondialog(self):
        self.root = Tkinter.Tk()
        self.root.withdraw()

        raw_input("Press enter to select the directory")

        dirname = tkFileDialog.askdirectory(parent=root, initialdir="/home/shridhar/Desktop",
                                            title='Please select a directory')
        print dirname
        extension = raw_input("Enter the file extension:")
        os.chdir(dirname)
        keyword = raw_input('enter string to be removed:')

        for filename in glob.glob("*." + extension):
            initialfilename = filename
            fln = filename.strip(keyword)

            os.rename(filename, fln)
            print filename
            print fln
            print "\n"


ui = new.Ui_MainWindow()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    mainWindow.show()
    sys.exit(app.exec_())
