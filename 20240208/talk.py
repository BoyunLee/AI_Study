import os
from datetime import datetime
import glob
import time
import shutil
import ftplib
from threading import Thread
import random
import string
import socket, threading

ftp = ftplib.FTP()
ftp.encoding = 'utf-8'

ftp.connect("210.119.12.121", 10005)
ftp.login('', '')
ftp.cwd("/")

def train_check():
    while True:
        try:
            fileList = glob.glob("C:\\study\\20240207\\*.jpg")
            
            start = time.time()
            for image in fileList:
                myfile = open(image, 'rb')
                fname = image
                fname = fname.split("\\")
                ftp.storbinary('STOR ' + str(fname[3]), myfile)
                print(fname[3])
                myfile.close()
                
                if myfile.close:
                    receive(open)
                    
            now = time.time() - start
            print("걸린시간 =", now)
        except IOError as e:
            print("I/O error({0}) : {1}".format(e.errno, e.strerror))
            
t1 = Thread(target=train_check, args = 0.01)
t1.start()
train_check()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('210.119.12.121', 10005))
nickname = input("Choose your nickname: ")


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))


# 멀티 클라이언트용 쓰레드
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# 메시지 보내기
write_thread = threading.Thread(target=write)
write_thread.start()

# list2 = list(map(str,[i for i in range(13)]))   

# list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

# i = 0
# while True:
#     print(list_1[i])
#     i += 1
     
#     if i == 10:
#         break
  