import os
from datetime import datetime
import glob
import time
import shutil
import ftplib
from threading import Thread

ftp = ftplib.FTP()
ftp.encoding = 'utf-8'

ftp.connect("210.119.12.121", 10005)
ftp.login('admin1', '1234')
ftp.cwd("/")

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
                if count > 50:
                    break
            now = time.time() - start
            print("걸린시간 =", now)
        except IOError as e:
            print("I/O error({0}) : {1}".format(e.errno, e.strerror))
            time.sleep(0.1)
            
t1 = Thread(target=train_check, args = 0.01)
t1.start()
train_check()
            


# print("Hello, \n world!")
# print("(35 + 1) * 2")

# x=10
# x+=1
# print(x)

# x, y, z, = 10, 20, 30
# print(x, y, z)


# x = int(input("0보다 큰 정수를 입력하시오 : "))
# y = int(input("10보다 작은 정수를 입력하시오 : "))
# print(x + y)


# for i in range(10):
#     for j in range(10):
#         if j <= i:
#             print("*", end='')
#     print()
    

# for i in range(5, 0):
#     for j in range(0, 5):
#         j += 1
#         if(i < j):
            
#             print('', end='')
            
#         elif(i == j):
#             print('*', end='')
            
#         else:
#             print('', end='')
#     print()

# a = [29, 21, 53, 62, 19] 
# print(a[0])

# count = 0

# now = datetime.now()
# datetime_1 = now.strftime("%Y년 %M월 %d일 %H시 %M분 %S초 %f")
# filelist = glob.glob("C:\\study\\image\\*.jpg")

# for i in filelist:
#     os.rename(i, f'C:/study/image/{datetime_1}_{count}.jpg')
#     count += 1

# now = datetime.now()
# datetime_1 = now.strftime("%Y년 %M월 %d일 %H시 %M분 %S초 %f")
# print(datetime_1)


# range(0,10)
# a = list(range(3, 10))
# print(a)
# b = list(range(5, 10))
# print(b)

# for i in range(5, 12):
#     print(i , end='')

# while True:
#     now = datetime.now()
#     datetime1 = now.strftime("%Y년")
#     datetime2 = now.strftime("%m월")
#     datetime3 = now.strftime("%d일")
#     datetime3 = now.strftime("%H시")
#     datetime5 = now.strftime("%M분")
    
#     os.makedirs(f'C:\\study\\image\\{datetime1}\\{datetime2}\\{datetime3}\\{datetime4}\\{datetime5}')
#     time.sleep(60)

# while True:    
#     now = datetime.now()
#     datetime_1 = now.strftime("%Y년 %m월 %d일 %H시 %M분")
#     filelist = glob.glob("C:\\study\\20240130\\*.jpg")

#     for i in filelist:
#         os.rename(i, f'C:/study/20240130/{datetime_1}.jpg')
#         time.sleep(60)
        
# filelist = glob.glob("C:\\study\\20240130\\*.jpg")
# filename = 0

# while True:
#     for i in filelist:
#         now = datetime.now()
#         datetime1 = now.strftime("%Y년")
#         datetime2 = now.strftime("%m월")
#         datetime3 = now.strftime("%d일")
#         datetime4 = now.strftime("%H시")
#         datetime5 = now.strftime("%M분")
#         os.makedirs(f'C:\\study\\image\\{datetime1}\\{datetime2}\\{datetime3}\\{datetime4}\\{datetime5}',exist_ok=True)
#         # j = i
#         # i = os.path.basename(i)
#         # mofile = "C:\\study\\20240130" + '\\' + i
#         shutil.copy(i,f'C:\\study\\image\\{datetime1}\\{datetime2}\\{datetime3}\\{datetime4}\\{datetime5}\\' + str(datetime5) + '.jpg')
    
#         time.sleep(60)



# while True:

#     now = datetime.now()
#     datetime1 = now.strftime("%Y년")
#     datetime2 = now.strftime("%m월")
#     datetime3 = now.strftime("%d일")
#     datetime4 = now.strftime("%H시")
#     datetime5 = now.strftime("%M분")
#     datetime6 = now.strftime("%S초")
#     os.makedirs(f'C:\\study\\image\\{datetime1}\\{datetime2}\\{datetime3}\\{datetime4}\\{datetime5}' + str(datetime6) + '.txt',exist_ok=True)

#     time.sleep(1)
    
# while True:
#     now = datetime.now()
#     datetime_1 = now.strftime(f'log:\\study\\image\\%Y\\%m\\%d\\%H\\%M\\%S'+ '.jpg')
#     filelist = [datetime_1]
#     f = open("C:\\study\\20240206\\log.txt", "a")
#     for i in filelist:
#         f.write(i + "\n")
#         time.sleep(1)

# filelist = glob.glob("C:\\study\\image\\*.jpg")
# filename = 0

# while True:
#     count = 0
#     for i in filelist:
#         try:
#             now = datetime.now()
#             datetime1 = now.strftime("%Y년")
#             datetime2 = now.strftime("%m월")
#             datetime3 = now.strftime("%d일")
#             datetime4 = now.strftime("%H시")
#             datetime5 = now.strftime("%M분")
#             datetime6 = now.strftime("%S초")
            
#             destination_folder = f'C:\\study\\image\\{datetime1}\\{datetime2}\\{datetime3}\\{datetime4}\\{datetime5}'
#             os.makedirs(destination_folder, exist_ok=True)
            
#             new_file_name = f'{datetime1}_{datetime2}_{datetime3}_{datetime4}_{datetime5}_{datetime6}_{count}.jpg'
#             destination_path = os.path.join(destination_folder, new_file_name)

#             shutil.copy(i, destination_path)
            
#             datetime_1 = now.strftime(f'log:\\study\\image\\%Y\\%m\\%d\\%H\\%M\\%S_{count}'+'.jpg')
#             count +=1
            
#             filelist = [datetime_1]
#             f = open("C:\\study\\image\\log.txt", "a")
#             for i in filelist:
#                 f.write(i + "\n")
#                 time.sleep(1)
#         except:
#             break
        
#         f = open("C:\\study\\image\\log.txt", "r")
#         ff = f.read()
#         print(ff)
        
#         print(ff.find("_4"))
        
#     break
