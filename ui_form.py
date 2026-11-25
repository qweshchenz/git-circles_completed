import sys
from PyQt6 import QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(220, 440, 160, 40)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Нарисовать")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Окружности")