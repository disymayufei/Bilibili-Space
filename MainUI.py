# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class CUi_MainWindow(object):
    def CsetupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setWindowFlags(QtCore.Qt.Widget)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-120, -50, 1271, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon/bg.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, -10, 341, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icon/bilibiliLogo.png"))
        self.label_2.setObjectName("label_2")
        self.UserShow = QtWidgets.QLabel(self.centralwidget)
        self.UserShow.setGeometry(QtCore.QRect(710, 30, 261, 41))
        self.UserShow.setObjectName("UserShow")
        self.ImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageLabel.setGeometry(QtCore.QRect(730, 100, 161, 161))
        self.ImageLabel.setText("")
        self.ImageLabel.setObjectName("ImageLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 71, 21))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 230, 201, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.Level = QtWidgets.QLabel(self.centralwidget)
        self.Level.setGeometry(QtCore.QRect(300, 230, 161, 21))
        self.Level.setObjectName("Level")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 290, 71, 21))
        self.label_4.setObjectName("label_4")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(80, 350, 248, 197))
        self.calendar.setSelectedDate(QtCore.QDate(2021, 3, 2))
        self.calendar.setGridVisible(True)
        self.calendar.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(False)
        self.calendar.setObjectName("calendar")
        self.Timer = QtWidgets.QLabel(self.centralwidget)
        self.Timer.setGeometry(QtCore.QRect(120, 290, 231, 20))
        self.Timer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Timer.setObjectName("Timer")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 630, 141, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 630, 601, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 190, 91, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(730, 260, 54, 12))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(720, 350, 71, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(790, 350, 151, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(720, 400, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(800, 400, 161, 16))
        self.label_12.setObjectName("label_12")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(790, 500, 111, 101))
        self.dial.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.dial.setObjectName("dial")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(630, 540, 161, 21))
        font = QtGui.QFont()
        font.setFamily("??????")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 570, 411, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(720, 300, 71, 21))
        self.label_15.setObjectName("label_15")
        self.FansNum = QtWidgets.QLabel(self.centralwidget)
        self.FansNum.setGeometry(QtCore.QRect(790, 300, 151, 21))
        self.FansNum.setObjectName("FansNum")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(310, 140, 81, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(400, 140, 281, 21))
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.Logout = QtWidgets.QAction(MainWindow)
        self.Logout.setObjectName("Logout")
        self.LogoutWithClear = QtWidgets.QAction(MainWindow)
        self.LogoutWithClear.setObjectName("LogoutWithClear")
        self.menu.addAction(self.Logout)
        self.menu.addAction(self.LogoutWithClear)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bilibili????????? by Disy"))
        self.UserShow.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#f09920;\">User</span><span style=\" font-size:18pt;\">,????????????</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">?????????</span></p></body></html>"))
        self.Level.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">0/0</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">???????????????</span></p></body></html>"))
        self.Timer.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">1970???1???1??? | 00:00:00</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">?????????????????????</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">None</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#2c8bff;\">Level 0</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">????????????</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">0.0</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">???????????????</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">1970???1???1???</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff007f;\">????????????????????????</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ff5d0c;\">???????????????????????????000?????????</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#f18293;\">????????????</span></p></body></html>"))
        self.FansNum.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#f18293;\">0</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">????????????:</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">1970???01???01??? | 00:00:00</span></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "??????"))
        self.Logout.setText(_translate("MainWindow", "????????????????????????????????????"))
        self.LogoutWithClear.setText(_translate("MainWindow", "???????????????????????????"))
