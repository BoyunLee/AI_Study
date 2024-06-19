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

ftp.connect("210.119.12.108", 10005)
ftp.login('admin1', '1234')
ftp.cwd("/")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('210.119.12.108', 10007))
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
        
def train_check():
    while True:
        try:
            fileList = glob.glob("C:\\study\\20240207\\*.jpg")
            count = 0
            start = time.time()
            for image in fileList:
                myfile = open(image, 'rb')
                fname = image
                fname = fname.split("\\")
                ftp.storbinary('STOR ' + str(fname[3]), myfile)
                print(fname[3])
                myfile.close()
                count = count + 1
                
                if count == 2:
                    client.send('보냈습니다'.encode('utf-8'))
            break
                    
        except IOError as e:
            print("I/O error({0}) : {1}".format(e.errno, e.strerror))
            time.sleep(0.1)
            
t1 = Thread(target=train_check, args = 0.01)
t1.start()
train_check()




# def receive():
#     while True:
#         try:
#             message = client.recv(1024).decode('utf-8')
#             if message == 'NICKNAME':
#                 client.send(nickname.encode('utf-8'))
#             else:
#                 print(message)
#         except:
#             print("An error occured!")
#             client.close()
#             break


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