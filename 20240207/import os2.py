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

ftp = ftplib.FTP()
ftp.encoding = 'utf-8'

ftp.connect("210.119.12.108", 10005)
ftp.login('admin1', '1234')
ftp.cwd("/")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('210.119.12.108', 8080))
user = "boyun"
count = 0 


def receive():
    message = client.recv(1024).decode('utf-8')
    while True:
        try:
            if message == 'NICKNAME':
                client.send(user.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def send_message(message):
    global count 
    client.send(message.encode('utf-8'))
    count +=1
    
def write():
    while True:
        message = '{}: {}'.format(user, input(''))
        send_message(message)    
    

def train_check(message):
    global count
    while True:
        try:
            now = datetime.now()
            datetime_1 = now.strftime("%Y%m%d%H%M%S")
            filelist = glob.glob('C:\\study\\20240213\\*.jpg')
            a = 0
            for i in filelist:
                try:
                    shutil.move(i, f'C:\\study\\image\\{datetime_1}_{a}.jpg')
                    a += 1
                except (FileExistsError, FileNotFoundError):
                    pass
            
            send_message(user)
            send_message('okay')
            
            filelist2 = glob.glob('C:\\study\\image\\*.jpg')

            for e in filelist2:
                send_message(e +'\n')
                time.sleep(0.5)
                if count >52:
                    break
                
            try:
                con = sqlite3.connect('send.db')
                cur = con.cursor()
                for i in filelist2:
                    path = i
                    name = os.path.basename(i)
                    date = datetime_1
                    cur.execute('CREATE TABLE IF NOT EXISTS NewTable (id INTEGER PRIMARY KEY AUTOINCREMENT, path TEXT NOT NULL, name TEXT NOT NULL, date TEXT NOT NULL)')
                    cur.execute(f"INSERT OR IGNORE INTO NewTable (path, name, date) VALUES (?, ?, ?)", (path, name, date))
                con.commit()
                con.close()
            except sqlite3.OperationalError as e:
                print("SQLite error", e)
            except sqlite3.DatabaseError as e:
                print('DatabaseError', e)
            
            if message.startswith('okay'):
                try:
                    con = sqlite3.connect('send.db')
                    cur = con.cursor()
                    cur.execute('SELECT path FROM NewTable WHERE path IS NULL')
                    a = cur.fetchone()
                    if a:
                        with open(a[0], 'rb') as myfile:
                            fname = os.path.basename(a[0])
                            ftp.storbinary('STOR ' + fname, myfile)
                        send_message('보냈습니다')
                except sqlite3.Error as e:
                    print("SQLite error:", e)
                finally:
                    con.close()
            
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