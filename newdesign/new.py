# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created: Tue Sep 24 04:55:01 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(501, 662)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.browse = QtGui.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(400, 0, 101, 27))
        self.browse.setFlat(True)
        self.browse.setObjectName(_fromUtf8("browse"))
        self.scrollold = QtGui.QScrollArea(self.centralwidget)
        self.scrollold.setGeometry(QtCore.QRect(0, 30, 251, 561))
        self.scrollold.setWidgetResizable(True)
        self.scrollold.setObjectName(_fromUtf8("scrollold"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 559))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollold.setWidget(self.scrollAreaWidgetContents)
        self.verticalScrollBar = QtGui.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(250, 30, 21, 561))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.scrollnew = QtGui.QScrollArea(self.centralwidget)
        self.scrollnew.setGeometry(QtCore.QRect(270, 30, 231, 561))
        self.scrollnew.setWidgetResizable(True)
        self.scrollnew.setObjectName(_fromUtf8("scrollnew"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 229, 559))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollnew.setWidget(self.scrollAreaWidgetContents_2)
        self.rename = QtGui.QPushButton(self.centralwidget)
        self.rename.setGeometry(QtCore.QRect(0, 590, 501, 27))
        self.rename.setFlat(True)
        self.rename.setObjectName(_fromUtf8("rename"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit.selectAll)
        QtCore.QObject.connect(self.browse, QtCore.SIGNAL(_fromUtf8("clicked()")), self.browse.show)
        QtCore.QObject.connect(self.rename, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rename.click)
        QtCore.QObject.connect(self.rename, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rename.show)
        QtCore.QObject.connect(self.scrollnew, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), self.scrollnew.show)
        QtCore.QObject.connect(self.scrollold, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), self.scrollold.show)
        QtCore.QObject.connect(self.verticalScrollBar, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.verticalScrollBar.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Renamer!", None))
        self.browse.setText(_translate("MainWindow", "Browse", None))
        self.rename.setText(_translate("MainWindow", "Rename", None))

