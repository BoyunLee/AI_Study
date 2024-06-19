import socket
import random
import time
import matplotlib.pyplot as plt

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 8080))  # 호스트와 포트 설정
server_socket.listen(1)  # 최대 접속 수
client_socket, addr = server_socket.accept()

# 초기 데이터
x_data = []
y_data = []

# 그래프 초기 설정
plt.ion()
fig, ax = plt.subplots()

while True:
    x = time.time()

    # 클라이언트로부터 데이터 수신
    data = client_socket.recv(1024).decode()  # 데이터 수신
    numbers = data.strip().split('\n')  # 데이터를 개행 문자로 분할하여 리스트로 변환
    int_numbers = [int(num) for num in numbers]  # 각 숫자를 정수로 변환하여 리스트로 저장

    # 리스트에서 첫 번째 숫자를 추출하여 y에 저장
    y = int_numbers[0]

    print(y)

    # 데이터 추가
    x_data.append(x)
    y_data.append(y)

    # 그래프 업데이트
    ax.clear()
    ax.plot(x_data, y_data)
    
    ax.set_xlim(max(0, x - 10), x + 1)  # 최근 10초 데이터만 표시
    ax.set_ylim(0, 100)

    # 그래프 보여주기
    plt.show()
    plt.pause(0.1)