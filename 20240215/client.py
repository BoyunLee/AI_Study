import os
from datetime import datetime
import glob
import time
import shutil
import ftplib
from threading import Thread
from socket import socket
import socket
import threading
import sqlite3

# FTP 및 소켓 연결 설정
ftp = ftplib.FTP()
ftp.encoding = 'utf-8'

ftp.connect("210.119.12.108", 10005)
ftp.login('admin1', '1234')
ftp.cwd("/")

# 클라이언트 소켓 설정
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('210.119.12.108', 8080))
user = "boyun"
count =0 

# 서버로부터 메시지 수신 및 처리
def receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        try:
            if message == 'NICKNAME':
                client.send(user.encode('utf-8'))

            else:
                print(message)
                if message.startswith('id_'):
                    se = message.split('_')
                    con = sqlite3.connect('send.db')
                    cur = con.cursor()
                    cur.execute(f'SELECT path FROM NewTable WHERE id = {se[1]}')
                    a = cur.fetchone()
                    with open(a[0],'rb') as myfile:
                        fname = os.path.basename(a[0])
                        ftp.storbinary('STOR ' + fname, myfile)
                    send_message('보냈습니다') 
        except:
            print("An error occurred!")
            client.close()
            break
        
# 서버로 메시지 전송
def send_message(message):
    global count
    client.send(message.encode('utf-8'))
    count +=1

# 사용자 입력 메시지 전송    
def write():
    while True:
        message = '{}'.format(input(''))
        client.send(message.encode('utf-8'))    
    
# 이미지 파일 확인 및 업로드
def train_check():
    global count
    while True:
        try:
            now = datetime.now()
            datetime_1 = now.strftime("%Y%m%d%H%M%S")
            filelist = glob.glob('C:\\study\\20240213\\*.jpg')
            a = 0
            for i in filelist:
                if FileNotFoundError:
                    break
                else:
                    shutil.move(i,f'C:\\study\\image\\{datetime_1}_{a}.jpg')
                    a+=1
            
                    
            send_message(user)
            send_message('okay'+'\n')

            
            filelist2 = glob.glob('C:\\study\\image\\*.jpg')
            filelist2 =sorted(filelist2)
            
            for i in filelist2:
                if count <= 53:
                    send_message(str(i)+'\n')
                    time.sleep(0.5)
            send_message('경로 보냄 완료')

            try:
                con = sqlite3.connect('send.db')
                cur = con.cursor()
                for i in filelist2:
                    path = i
                    name = os.path.basename(i)
                    a=name.split('_')
                    cur.execute('CREATE TABLE IF NOT EXISTS NewTable (id INTEGER PRIMARY KEY, path TEXT NOT NULL, name TEXT NOT NULL, date TEXT NOT NULL)')
                    cur.execute(f"INSERT OR IGNORE INTO NewTable (path, name, date) VALUES (?, ?, ?)", (path, a[1], a[0]))
                con.commit()
                con.close()
            except sqlite3.OperationalError as e:
                print("SQLite error", e)
            except sqlite3.DatabaseError as e:
                print('DatabaseError', e)
            break
             
        except IOError as e:
            print("I/O error({0}) : {1}".format(e.errno, e.strerror))
            time.sleep(0.1)
            


# 스레드 생성
t1 = Thread(target=train_check) 
t1.start()

# 메시지 수신 및 전송 스레드 생성
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# 메시지 입력 및 전송 스레드 생성
write_thread = threading.Thread(target=write)
write_thread.start()
