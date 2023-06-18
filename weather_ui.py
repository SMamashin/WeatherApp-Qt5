# ui interface by s-mamashin

# This UI interface is a copy of my interface made in a web* application.

# I repeated this with Qt5, the brains are still left in Python

# eel/js + css3(Weather App Web - https://github.com/SMamashin/WeatherApp/)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 772)
        MainWindow.setMinimumSize(QtCore.QSize(714, 0))
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.00568182 rgba(6, 129, 131, 255), stop:1 rgba(24, 99, 157, 255));\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 80, 571, 61))
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setStyleSheet(".QLineEdit {\n"
"    display: flex;\n"
"    margin-left: auto;\n"
"    margin-right: auto;\n"
"    border: none;\n"
"    background: #d0f0e2;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    width: 90%;\n"
"    outline: none;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"    opacity: 0.9;\n"
"}\n"
"")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setFrame(True)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(70, 150, 571, 81))
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setTabletTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    display: block;\n"
"    margin-left: auto;\n"
"    margin-right: auto;\n"
"    margin-top: 10px;\n"
"    border: none;\n"
"    background: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 146, 127, 255), stop:1 rgba(52, 113, 255, 255));\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"    padding: 20px;\n"
"    width: 93%;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:#cbe7f5;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 124, 212, 255), stop:1 rgba(4, 144, 136, 255));\n"
"}")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 250, 621, 401))
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    display: flex;\n"
"    margin-top: 50px;\n"
"    justify-content: center;\n"
"    color: #fff;\n"
"    font-size: 15px;\n"
"    padding: 5%;\n"
"}\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WeatherApp"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите сюда ваш город"))
        self.pushButton.setText(_translate("MainWindow", "Посмотреть погоду"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><h6 align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">WeatherApp - ещё один бесполезный маленький проект <br/>Приятного использования by </span><a href=\"https://vk.com/evangelion1995\"><span style=\" font-size:12pt; text-decoration: underline; color:#f79797;\">S-Mamashin</span></a><span style=\" font-size:12pt;\"><br/><br/>Чтобы узнать детальный прогноз на данный момент - введите нужный<br/>существующий* город/страну. </span></h6><hr><h6 align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br/></h6><h6 align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Версия с WebUI - </span><span style=\" font-size:12pt; color:#f79797;\"><a style=\"text-decoration: underline; color:#f79797;\"  href=\"https://github.com/SMamashin/WeatherApp\">github.com/SMamashin/WeatherApp</a></span></h6><h6 align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Qt5 версия - </span><span style=\" font-size:12pt; color:#f79797;\"><a style=\"text-decoration: underline; color:#f79797;\" href=\"https://github.com/SMamashin/WeatherApp-Qt5\">github.com/SMamashin/WeatherApp-Qt5</a></span></h6><h6 align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"><br/><br/><br/></span><span style=\" font-size:9pt;\">Open Source Local Project. <br/>Author - </span><span style=\" font-size:9pt; color:#f79797;\">S-Mamashin/Mamashin.</span></h6></body></html>"))
