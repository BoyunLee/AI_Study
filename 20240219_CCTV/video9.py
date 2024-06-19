from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import sys
import cv2
import os

from PyQt5.QtCore import QThread
import sqlite3
from datetime import datetime


gcount = 0
timecount = 0

class InputDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(InputDialog, self).__init__(parent)
        self.setWindowTitle("Enter CCTV ID")
        
        layout = QtWidgets.QVBoxLayout()
        
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_3 = QtWidgets.QLineEdit()
        self.lineEdit_4 = QtWidgets.QLineEdit()
    
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.lineEdit_2)
        layout.addWidget(self.lineEdit_3)
        layout.addWidget(self.lineEdit_4)
        
        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)
        
        self.setLayout(layout)

    def getValue(self):
        if self.exec_() == QtWidgets.QDialog.Accepted:
            return self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text()
        else:
            return None, None, None, None

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow           
        self.MainWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.pushButton.clicked.connect(self.show_input_dialog)
        
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
        
    def show_input_dialog(self):
        input_dialog = InputDialog()
        id_value = input_dialog.getValue()
        print("Entered ID:", id_value)
        if id_value[0]:
            self.lineEdit.setText(id_value[0])
        if id_value[1]:
            self.lineEdit_2.setText(id_value[1])
        if id_value[2]:
            self.lineEdit_3.setText(id_value[2])
        if id_value[3]:
            self.lineEdit_4.setText(id_value[3])

    def play_video(self):
        now = datetime.now()
        datetime1 = now.strftime("%Y-%m-%d-%H")
        a = datetime1.split('-')
        
        text1 = self.lineEdit.text()
        if text1:
            os.makedirs(f'C:\\study\\{a[0]}\\{a[1]}\\{a[2]}\\{a[3]}', exist_ok = True)
            recording_file1 = f'C:/study/{a[0]}/{a[1]}/{a[2]}/{a[3]}/A.avi'
            conn = sqlite3.connect('Video.db') 
            cur = conn.cursor() # 커서 객체 생성
            cur.execute("CREATE TABLE if not exists Address (Year, Month, Day, Time, Name PRIMARY KEY);") # 테이블이 존재하면 에러 발생 
            cur.execute("INSERT OR IGNORE INTO Address (Year, Month, Day, Time, Name) VALUES (?, ?, ?, ?, ?)", (a[0], a[1], a[2], a[3], recording_file1) )
            conn.commit() # 저장
            conn.close() 
            self.th = Thread(self.lineEdit, recording_file1)  # 스레드 생성 및 시작
            self.th.changePixmap.connect(self.label.setPixmap)
            self.th.start()
            self.label.show()
            if not text1:
                QMessageBox.warning(self, "Warning", "Please enter the ID.")
                return
                    
            
        text2 = self.lineEdit_2.text()
        if text2:
            os.makedirs(f'C:\\study\\{a[0]}\\{a[1]}\\{a[2]}\\{a[3]}', exist_ok = True)
            recording_file2 = f'C:/study/{a[0]}/{a[1]}/{a[2]}/{a[3]}/B.avi'
            conn = sqlite3.connect('Video.db') 
            cur = conn.cursor() # 커서 객체 생성
            cur.execute("CREATE TABLE if not exists Address (Year, Month, Day, Time, Name PRIMARY KEY);") # 테이블이 존재하면 에러 발생 
            cur.execute("INSERT OR IGNORE INTO Address (Year, Month, Day, Time, Name) VALUES (?, ?, ?, ?, ?)", (a[0], a[1], a[2], a[3], recording_file2) )
            conn.commit() # 저장
            conn.close() 
            self.th2 = Thread(self.lineEdit_2, recording_file2)  # 스레드 생성 및 시작
            self.th2.changePixmap.connect(self.label_2.setPixmap)
            self.th2.start()
            self.label_2.show()
            if not text2:
                QMessageBox.warning(self, "Warning", "Please enter the ID.")
                return
            
        text3 = self.lineEdit_3.text()
        if text3:
            os.makedirs(f'C:\\study\\{a[0]}\\{a[1]}\\{a[2]}\\{a[3]}', exist_ok = True)
            recording_file3 = f'C:/study/{a[0]}/{a[1]}/{a[2]}/{a[3]}/C.avi'
            conn = sqlite3.connect('Video.db') 
            cur = conn.cursor() # 커서 객체 생성
            cur.execute("CREATE TABLE if not exists Address (Year, Month, Day, Time, Name PRIMARY KEY);") # 테이블이 존재하면 에러 발생 
            cur.execute("INSERT OR IGNORE INTO Address (Year, Month, Day, Time, Name) VALUES (?, ?, ?, ?, ?)", (a[0], a[1], a[2], a[3], recording_file3) )
            conn.commit() # 저장
            conn.close() 
            self.th3 = Thread3(self.lineEdit_3, recording_file3)  # 스레드 생성 및 시작
            self.th3.changePixmap.connect(self.label_4.setPixmap)
            self.th3.start()
            self.label_4.show()
            if not text3:
                QMessageBox.warning(self, "Warning", "Please enter the ID.")
                return
            
        text4 = self.lineEdit_4.text()
        if text4:
            os.makedirs(f'C:\\study\\{a[0]}\\{a[1]}\\{a[2]}\\{a[3]}', exist_ok = True)
            recording_file4 = f'C:/study/{a[0]}/{a[1]}/{a[2]}/{a[3]}/D.avi'
            conn = sqlite3.connect('Video.db') 
            cur = conn.cursor() # 커서 객체 생성
            cur.execute("CREATE TABLE if not exists Address (Year, Month, Day, Time, Name PRIMARY KEY);") # 테이블이 존재하면 에러 발생 
            cur.execute("INSERT OR IGNORE INTO Address (Year, Month, Day, Time, Name) VALUES (?, ?, ?, ?, ?)", (a[0], a[1], a[2], a[3], recording_file4) )
            conn.commit() # 저장
            conn.close() 
            self.th4 = Thread4(self.lineEdit_4, recording_file4)  # 스레드 생성 및 시작
            self.th4.changePixmap.connect(self.label_5.setPixmap)
            self.th4.start()
            self.label_5.show()
            if not text4:
                QMessageBox.warning(self, "Warning", "Please enter the ID.")
                return
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
    def stop_video(self):
        self.label.hide()
        self.label_2.hide()
        self.label_4.hide()
        self.label_5.hide()
        
    def close(self):
       sys.exit()
        
class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, lineEdit, recording_file, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True
        self.lineEdit = lineEdit
        self.recording_file = recording_file

    def run(self):
        now = datetime.now()
        datetime1 = now.strftime("%Y-%m-%d-%H")
        a = datetime1.split('-')
        
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
            
        os.makedirs(f'C:\\study\\{a[0]}\\{a[1]}\\{a[2]}\\{a[3]}', exist_ok = True)
        recording_file1 = f'C:/study/{a[0]}/{a[1]}/{a[2]}/{a[3]}/A.avi'
        conn = sqlite3.connect('Video.db') 
        cur = conn.cursor() # 커서 객체 생성
        cur.execute("CREATE TABLE if not exists Address (Year, Month, Day, Time, Name PRIMARY KEY);") # 테이블이 존재하면 에러 발생 
        cur.execute("INSERT OR IGNORE INTO Address (Year, Month, Day, Time, Name) VALUES (?, ?, ?, ?, ?)", (a[0], a[1], a[2], a[3], recording_file1) )
        conn.commit() # 저장
        conn.close() 
        
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))    
        out = cv2.VideoWriter(self.recording_file, cv2.VideoWriter_fourcc(*'XVID'), 20, (frame_width, frame_height))
            
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(527, 230, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
                out.write(frame)  # 녹화
            else:
                self.isRunning = False
                
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        con.close()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread2(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, lineEdit, recording_file, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True
        self.lineEdit = lineEdit
        self.recording_file = recording_file

    def run(self):
        now = datetime.now()
        datetime1 = now.strftime("%Y-%m-%d-%H")
        a = datetime1.split('-')
        
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
            
        os.makedirs(f'C:\\study\\{a[0]}\\{a[1]}\\{a[2]}\\{a[3]}', exist_ok = True)
        recording_file2 = f'C:/study/{a[0]}/{a[1]}/{a[2]}/{a[3]}/B.avi'
        conn = sqlite3.connect('Video.db') 
        cur = conn.cursor() 
        cur.execute("CREATE TABLE if not exists Address (Year, Month, Day, Time, Name PRIMARY KEY);") # 테이블이 존재하면 에러 발생 
        cur.execute("INSERT OR IGNORE INTO Address (Year, Month, Day, Time, Name) VALUES (?, ?, ?, ?, ?)", (a[0], a[1], a[2], a[3], recording_file2) )
        conn.commit()
        conn.close()
        
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))    
        out = cv2.VideoWriter(self.recording_file, cv2.VideoWriter_fourcc(*'XVID'), 20, (frame_width, frame_height))
            
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(527, 230, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
                out.write(frame) 
            else:
                self.isRunning = False

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        con.close()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread3(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, lineEdit, recording_file, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True
        self.lineEdit = lineEdit
        self.recording_file = recording_file

    def run(self):
        now = datetime.now()
        datetime1 = now.strftime("%Y-%m-%d-%H")
        a = datetime1.split('-')
        
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
            
        os.makedirs(f'C:\\study\\{a[0]}\\{a[1]}\\{a[2]}\\{a[3]}', exist_ok = True)
        recording_file3 = f'C:/study/{a[0]}/{a[1]}/{a[2]}/{a[3]}/C.avi'
        conn = sqlite3.connect('Video.db') 
        cur = conn.cursor() 
        cur.execute("CREATE TABLE if not exists Address (Year, Month, Day, Time, Name PRIMARY KEY);") # 테이블이 존재하면 에러 발생 
        cur.execute("INSERT OR IGNORE INTO Address (Year, Month, Day, Time, Name) VALUES (?, ?, ?, ?, ?)", (a[0], a[1], a[2], a[3], recording_file3) )
        conn.commit() 
        conn.close() 
        
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))    
        out = cv2.VideoWriter(self.recording_file, cv2.VideoWriter_fourcc(*'XVID'), 20, (frame_width, frame_height))
            
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(527, 230, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
                out.write(frame)  
            else:
                self.isRunning = False

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        con.close()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread4(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, lineEdit, recording_file, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True
        self.lineEdit = lineEdit
        self.recording_file = recording_file

    def run(self):
        now = datetime.now()
        datetime1 = now.strftime("%Y-%m-%d-%H")
        a = datetime1.split('-')
        
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
            
        os.makedirs(f'C:\\study\\{a[0]}\\{a[1]}\\{a[2]}\\{a[3]}', exist_ok = True)
        recording_file4 = f'C:/study/{a[0]}/{a[1]}/{a[2]}/{a[3]}/D.avi'
        conn = sqlite3.connect('Video.db') 
        cur = conn.cursor() 
        cur.execute("CREATE TABLE if not exists Address (Year, Month, Day, Time, Name PRIMARY KEY);") # 테이블이 존재하면 에러 발생 
        cur.execute("INSERT OR IGNORE INTO Address (Year, Month, Day, Time, Name) VALUES (?, ?, ?, ?, ?)", (a[0], a[1], a[2], a[3], recording_file4) )
        conn.commit()
        conn.close() 
        
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))    
        out = cv2.VideoWriter(self.recording_file, cv2.VideoWriter_fourcc(*'XVID'), 20, (frame_width, frame_height))
            
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(527, 230, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
                out.write(frame) 
            else:
                self.isRunning = False

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        con.close()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False

        
if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda: ui.play_video())
    MainWindow.show() 
    sys.exit(app.exec_())


