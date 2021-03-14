# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class LUi_MainWindow(object):
    def LsetupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(600, 450))
        MainWindow.setMaximumSize(QtCore.QSize(600, 450))
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setWindowFlags(QtCore.Qt.Widget)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 451))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon/bgLoading.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Loading = QtWidgets.QLabel(self.centralwidget)
        self.Loading.setGeometry(QtCore.QRect(150, 20, 260, 260))
        self.Loading.setText("")
        self.Loading.setObjectName("Loading")
        self.gif = QMovie('icon/Loading_Logo.gif')
        self.Loading.setMovie(self.gif)
        self.Loading.setScaledContents(True)
        self.gif.start()
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 290, 511, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.LoadStatus = QtWidgets.QLabel(self.centralwidget)
        self.LoadStatus.setGeometry(QtCore.QRect(60, 330, 451, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.LoadStatus.setFont(font)
        self.LoadStatus.setObjectName("LoadStatus")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 400, 541, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bilibili小空间 by Disy | Loading..."))
        self.progressBar.setFormat(_translate("MainWindow", "%p%  Loading..."))
        self.LoadStatus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#1942c8;\">加载中...</span></p></body></html>"))
        self.label_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>TIPS小贴士</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#e70000;\">Tips:界面的所有数据都是实时更新的，你的动作可以立刻看到哦！</span></p></body></html>"))
