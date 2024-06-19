# 서버
# 단체 채팅방(서버)


import socket
import argparse
import threading
import time
import sqlite3
from datetime import datetime
import ftplib
from threading import Thread
import glob

host = "210.119.12.108"
port = 8080
user_list = {}
notice_flag = 0

def msg_func(msg):
    print(msg)
    for con in user_list.values():
        try:
            con.send(msg.encode('utf-8'))
        except:
            print("연결이 비 정상적으로 종료된 소켓 발견")



def handle_receive(client_socket, addr, user):
    msg = "---- %s님이 들어오셨습니다. ----"%user
    msg_func(msg)
    while 1:
        data = client_socket.recv(1024)
        string = data.decode('utf-8')

        if "/종료" in string:
            msg = "---- %s님이 나가셨습니다. ----"%user
            #유저 목록에서 방금 종료한 유저의 정보를 삭제
            del user_list[user]
            msg_func(msg)
            break
        elif  "보냈습니다" in string:
            filename = ""
            #파일 보내기
            ftp = ftplib.FTP()
            ftp.encoding = 'utf-8'   
            # ftp.encoding = 'CP949'  # 둘 중 하나 찾아야 함
            ftp.connect("210.119.12.109", 10006)
            ftp.login('admin', '1234')
            ftp.cwd("/")
            def train_check():
                global filename
                while True:
                    try:
                        fileList = glob.glob("C:\\*.jpg")
                        count = 0
                        start = time.time()
                        for image in fileList:
                            myfile = open(image, 'rb')
                            fname = image
                            fname = fname.split("\\")
                            ftp.storbinary('STOR ' + str(fname[1]) , myfile)
                            print(fname[1])
                            myfile.close()
                            f = open("C:\\study\\20240206\\log.txt", "a")
                            f.write( str(fname) + "\n")
                            filename = fname
                            time.sleep(0.1)
                            count = count + 1
                            if count > 50:
                                break
                        # print('retry = ', retry)
                        #retry = True
                        now = time.time() - start
                        # print("걸린시간 = ", now) 
                    except IOError as e:
                        print ("I/0 error({0}): {1}".format(e.errno, e.strerror))
                        retry = True
                        time.sleep(0.1)
            t1 = Thread(target= train_check, args = 0.01)
            t1.start()
            train_check()
        elif string == "okay":
            client_socket.sendall("okay".encode('utf-8'))
        elif "들어오셨습니다." not in string:
            filepath = string
            last_slash_idx = filepath.rfind("\\")
            filename = filepath[last_slash_idx + 1:]
            now = datetime.now()
            datetime_1 = now.strftime("%Y-%m-%d-%H_%M_%S")
            conn = sqlite3.connect("boyun.db")
            cur = conn.cursor()
            cur.execute("INSERT OR IGNORE INTO bbbb Values('" + datetime_1 + "', '" + string + "', '" + filename + "')")
            conn.commit()
            conn.close()
        
        string = "%s : %s"%(user, string)
        msg_func(string)
    client_socket.close()
def handle_notice(client_socket, addr, user):
    while 1:
        # 서버에서 메시지를 입력받아 모든 유저에게 전송
        msg = input("[SERVER] 메시지 입력: ")
        msg_func(msg)

def accept_func():
    #IPv4 체계, TCP 타입 소켓 객체를 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #포트를 사용 중 일때 에러를 해결하기 위한 구문
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #ip주소와 port번호를 함께 socket에 바인드 한다.
    #포트의 범위는 1-65535 사이의 숫자를 사용할 수 있다.
    server_socket.bind((host, port))

    #서버가 최대 5개의 클라이언트의 접속을 허용한다.
    server_socket.listen(5)

    while 1:
        try:
            #클라이언트 함수가 접속하면 새로운 소켓을 반환한다.
            client_socket, addr = server_socket.accept()
        except KeyboardInterrupt:
            for user, con in user_list:
                con.close()
            server_socket.close()
            print("Keyboard interrupt")
            break
        user = client_socket.recv(1024).decode('utf-8')
        user_list[user] = client_socket

        #accept()함수로 입력만 받아주고 이후 알고리즘은 핸들러에게 맡긴다.
        notice_thread = threading.Thread(target=handle_notice, args=(client_socket, addr, user))
        notice_thread.daemon = True
        notice_thread.start()

        receive_thread = threading.Thread(target=handle_receive, args=(client_socket, addr,user))
        receive_thread.daemon = True
        receive_thread.start()


if __name__ == '__main__':
    #parser와 관련된 메서드 정리된 블로그 : https://docs.python.org/ko/3/library/argparse.html
    #description - 인자 도움말 전에 표시할 텍스트 (기본값: none)
    #help - 인자가 하는 일에 대한 간단한 설명.
    parser = argparse.ArgumentParser(description="\nJoo's server\n-p port\n")
    parser.add_argument('-p', help="port")

    args = parser.parse_args()
    try:
        port = int(args.p)
    except:
        pass
    accept_func()







