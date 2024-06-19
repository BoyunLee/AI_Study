import ftplib
import random
import string
import glob
import time
from threading import Thread

def connect_ftp():
    ftp = ftplib.FTP()
    ftp.encoding = 'utf-8'

    while True:
            random_number = random.randint(920, 999)
            # 세 자리로 만들기 위해 문자열로 변환하고, zfill() 함수로 채움
            random_number_str = str(random_number).zfill(3)
            print("Random Password:", random_number_str)

            try:
                ftp.connect("210.119.12.114", 12345)
                ftp.login('aaa', str(random_number_str))
                ftp.cwd("/")
                print("Connected to FTP server with random credentials.")
                return ftp
            except ftplib.all_errors as e:
                print("Failed to connect to FTP server:", e)

def train_check(ftp):
    while True:
        try:
            fileList = glob.glob("C:\\study\\20240207\\*.jpg")
            count = 0
            start = time.time()
            for image in fileList:
                myfile = open(image, 'rb')
                fname = image.split("\\")[-1]
                ftp.storbinary('STOR ' + fname, myfile)
                print("Uploaded:", fname)
                myfile.close()
                count += 1
                
                if count > 50:
                    break
            now = time.time() - start
            print("Time taken =", now)
        except IOError as e:
            print("I/O error({0}) : {1}".format(e.errno, e.strerror))
            time.sleep(0.1)

# FTP 서버에 랜덤한 사용자 이름과 비밀번호로 접속
ftp = connect_ftp()

# 파일 업로드 작업을 별도의 스레드로 실행
t1 = Thread(target=train_check, args=(ftp,))
t1.start()

# 메인 스레드에서도 파일 업로드 작업 실행
train_check(ftp)
