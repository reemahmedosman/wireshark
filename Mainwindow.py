# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import*
from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow import Ui_OtherWindow
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QFormLayout,QHBoxLayout,QPushButton,QComboBox,QLabel,QLineEdit,QTextBrowser,QMenuBar,QStatusBar

from scapy.all import *
import sys
from netifaces import AF_INET, AF_INET6, AF_LINK
import netifaces as ni
import binascii
import winreg as wr

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

    def get_connection_name(iface_guids):
        iface_names = ['(unknown)' for i in range(len(iface_guids))]
        reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
        reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
        for i in range(len(iface_guids)):
            try:
                reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
                iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
            except FileNotFoundError:
                pass
        return iface_names    

class Ui_MainWindow(object):
    def OpenWindow(self):
	    self.window=QMainWindow()
	    self.ui=Ui_OtherWindow()
	    self.ui.setupUi(self.window)
	    self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 256, 121))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 200, 256, 121))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 230, 191, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.active)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 60, 211, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.select)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 420, 451, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.OpenWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "show active interface", None))
        self.pushButton_2.setText(_translate("MainWindow", "show interface", None))
        self.pushButton_3.setText(_translate("MainWindow", "start", None))
   
    
    def select(self):
        x=ni.interfaces()
        s=get_connection_name(x)
        self.textBrowser.setText(str(s))
        
    def active(self):
        x1=conf.iface
        #s1=get_connection_name(x1)
        self.textBrowser_2.setText(str(x1))
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

