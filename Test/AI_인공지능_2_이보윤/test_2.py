from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

class secondwindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 730)

        self.centralwidget =QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label =QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 180, 120, 20))
        self.label.setObjectName("label")
        self.label.setText("Page 2")
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 730)
        self.centralwidget =QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label =QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 180, 120, 20))
        self.label.setObjectName("label")
        self.label.setText("Page 1")

        self.pushButton =QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 680, 75, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("NEXT")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.pressed.connect(self.rejult)

    def rejult(self):
        self.window =QtWidgets.QWidget()
        self.ui =secondwindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
    
if __name__=="__main__":
    import sys
    app =QtWidgets.QApplication(sys.argv)
    MainWindow =QtWidgets.QMainWindow()
    ui =Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())