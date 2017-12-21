

from PyQt5 import*
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QFormLayout,QHBoxLayout,QPushButton,QComboBox,QLabel,QLineEdit,QTextBrowser,QMenuBar,QStatusBar

from scapy.all import *
import sys
#from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni
global no_of_packets
global selected_packet
global pkts
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

class Ui_OtherWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(802, 664)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, _fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(9, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)
        #self.pushButton_4 = QPushButton(self.centralwidget)
        #self.pushButton_4.setMaximumSize(QtCore.QSize(50, 16777215))
        #self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButton_2)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.pushButton_5)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.formLayout.setWidget(12, QFormLayout.SpanningRole, self.textBrowser)
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self.textBrowser_2)
        self.textBrowser_3 = QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.formLayout.setWidget(15, QFormLayout.SpanningRole, self.textBrowser_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "Capture", None))
        self.pushButton.setText(_translate("MainWindow", "Filter", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "None", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "tcp", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "http", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "http2", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "dns", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "udp", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "ip", None))
        self.pushButton_2.clicked.connect(self.Ok)
        self.label.setText(_translate("MainWindow", "no of packets", None))
        self.label_2.setText(_translate("MainWindow", "select packet no", None))
        #self.pushButton_4.setText(_translate("MainWindow", "Select", None))
        self.pushButton_5.setText(_translate("MainWindow", "Select", None))
        #self.pushButton_4.clicked.connect(self.select)
        self.pushButton_5.clicked.connect(self.select)
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
 

    def select(self):
        global selected_packet
        global pkts
        selected_packet = self.lineEdit_2.text()
        self.textBrowser_2.setText(str(pkts[int(selected_packet)-1].show(dump=True)))
        self.textBrowser_3.setText(str(hexdump(pkts[int(selected_packet)-1],dump=True)))
        
    
    def Ok(self):
        global no_of_packets
        global pkts
        no_of_packets = self.lineEdit.text()
        pkts= sniff(iface=conf.iface,filter=self.comboBox.currentText(),count=int(no_of_packets),prn = lambda x:\
        self.textBrowser.append(x.sprintf("Time: %IP.time% Source: %IP.src% Distination:  %IP.dst% Protocol %IP.proto% Length:  %IP.len% ID: %IP.id% Checksum: %IP.chksum%","\n")))
        #pkts= sniff(iface=conf.iface,filter=self.comboBox.currentText(),count= 2,prn = lambda x:\
	    #x.sprintf("Time: %IP.time% Source: %IP.src% Distination:  %IP.dst% Protocol %IP.proto% Length:  %IP.len% ID: %IP.id% Checksum: %IP.chksum%","\n"))
	    #self.textBrowser.setText(str(pkts))
        #self.textBrowser.setText(str(ni.interfaces()))
	

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    OtherWindow = QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

