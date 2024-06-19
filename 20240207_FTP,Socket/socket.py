# x = int(input("x : "))
# y = int(input("y : "))
# z = int(input("1(더하기),2(곱하기),3(빼기),4(나누기) 중에 고르시오 : "))

# if z==1:
#     print(x,'+',y,'=',x+y)
    
# elif z==2:
#     print(x,'x',y,'=',x*y)
    
# elif z==3:
#     print(x,'-',y,'=',x-y)
    
# elif z==4:
#     print(x,'%',y,'=',x/y)
    
# else:
#     print("fail")

# def minus():
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print('x+y=',x%y)
    
# def plus():
#     c = a*b
#     print("더하기 결과:", c)
    
from socket import*

clientSock =  socket(AF_INET, SOCK_STREAM)
clientSock.connect(('210.119.12.8', 8080))

print("연결 확인 되었습니다.")
clientSock.send('안뇽'.encode('utf-8'))

print("메세지를 전송했습니다.")

data = clientSock.recv(1024)
print("받은 데이터 : ", data.decode('utf-8'))

from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',8080))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속이 확인되었습니다.')

data = connectionSock.recv(1024)
print("받은데이터: ", data.decode('utf-8'))

connectionSock.send('바보'.encode('utf-8'))
print('메시지를 보냈습니다.')