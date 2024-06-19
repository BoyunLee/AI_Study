from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QInputDialog, QApplication, QWidget, QLabel, QPushButton, QListWidget, QMessageBox, QLineEdit, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import sys

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage, QPalette
from PyQt5 import QtWidgets, QtCore, QtGui

import configparser
import time
import cv2
import os

from PyQt5.QtCore import QThread
import sqlite3

gcount = 0
timecount = 0

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow           
        self.MainWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
        
        MainWindow.setObjectName("MainWindow") #if__name__main에서 상속받아서 앞으로는 MainWindow로 사용
        MainWindow.resize(1500, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow) #위젯 중앙을 설정을 하고 centralwidget에 MainWindow가 모두 넘겨줌(상속)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1500, 844))
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(QtGui.QPixmap("cctv.jpg"))
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(355, 123, 527, 230))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(932, 123, 527, 230))
        self.label_2.setObjectName("label_2")      
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(355, 405, 527, 230))
        self.label_4.setObjectName("label_4")   
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(932, 405, 527, 230))
        self.label_5.setObjectName("label_5")   
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(355, 360, 100, 15))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("color: black; background-color: gray; border: none;")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(932, 360, 100, 15))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("color: black; background-color: gray; border: none;")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(355, 642, 100, 15))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("color: black; background-color: gray; border: gray;")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(932, 642, 100, 15))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("color: black; background-color: gray; border: none;")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1170, 785, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Play Video")
        self.pushButton.clicked.connect(self.play_video)
        self.pushButton.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 0, 15, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_2.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1345, 785, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Stop Video")
        self.pushButton_3.clicked.connect(self.stop_video)
        self.pushButton_3.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def play_video(self):
        text1 = self.lineEdit.text()
        if text1:  # 입력된 텍스트가 있는지 확인
            self.th = Thread(self.lineEdit)  # 스레드 생성 및 시작
            self.th.changePixmap.connect(self.label.setPixmap)
            self.th.start()
            self.label.show()
        else:
            QMessageBox.warning(self, "Warning", "Please enter the ID.")
            
        text2 = self.lineEdit_2.text()
        if text2:  # 입력된 텍스트가 있는지 확인
            self.th2 = Thread(self.lineEdit_2)  # 스레드 생성 및 시작
            self.th2.changePixmap.connect(self.label_2.setPixmap)
            self.th2.start()
            self.label_2.show()
        else:
            QMessageBox.warning(self, "Warning", "Please enter the ID.")
            
        text3 = self.lineEdit_3.text()
        if text3:  # 입력된 텍스트가 있는지 확인
            self.th3 = Thread(self.lineEdit_3)  # 스레드 생성 및 시작
            self.th3.changePixmap.connect(self.label_4.setPixmap)
            self.th3.start()
            self.label_4.show()
        else:
            QMessageBox.warning(self, "Warning", "Please enter the ID.")
            
        text4 = self.lineEdit_4.text()
        if text4:  # 입력된 텍스트가 있는지 확인
            self.th4 = Thread(self.lineEdit_4)  # 스레드 생성 및 시작
            self.th4.changePixmap.connect(self.label_5.setPixmap)
            self.th4.start()
            self.label_5.show()
        else:
            QMessageBox.warning(self, "Warning", "Please enter the ID.")
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
    def stop_video(self):
        self.th.stop()
        self.th2.stop()
        self.th3.stop()
        self.th4.stop()
        self.label.hide()
        self.label_2.hide()
        self.label_4.hide()
        self.label_5.hide()
        
    def close(self):
       sys.exit()
        

class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, lineEdit, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True
        self.lineEdit = lineEdit

    def run(self):
            con = sqlite3.connect("cctv.db")
            cur = con.cursor()
            cur.execute("SELECT RTSP FROM cctv WHERE ID = '" + str(self.lineEdit.text()) + "'")
            result = cur.fetchone()
            
            image_files = result[0]
            cap = cv2.VideoCapture(image_files)
            
            if cap.isOpened() is False:
                self.isRunning = False
            else :
                self.isRunning = True
                
            while self.isRunning:
                ret, frame = cap.read()
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(527, 230, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
                if not ret:
                    self.isRunning = False
                    break

            cap.release()
            cv2.destroyAllWindows()
            con.close()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False

        
if __name__ == "__main__":
    import sys #object는 윈도의 최고 조상
    app = QtWidgets.QApplication(sys.argv) # sys.argv는 현재 작업중인.py 절대 경로를 인자로 넘겨줌
    MainWindow = QtWidgets.QMainWindow() #윈도우 UI를 연결하기 위한 상속
    ui = Ui_MainWindow() #위 클래스를 ui 변수에 넣는다 여기서 부터 클래스 개념 필요
    ui.setupUi(MainWindow) #위 QtWidgets.QMainWindows()에서 상속받아서 위 SetupUi함수 인자로 넘겨줌 즉 위젯 실행하라는 뜻
    MainWindow.show() #MainWindow를 화면에 표시
    sys.exit(app.exec_()) #무한루프


