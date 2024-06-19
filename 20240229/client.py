import socket
import random

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('210.119.12.117', 8080))  # 서버 주소와 포트 설정

    
    # 메시지 전송
while True:
    # 랜덤 값 생성
    random_value = random.randint(0, 100)
    
    # 랜덤 값을 서버로 전송
    data = f"{random_value}\n"
    client_socket.sendall(data.encode())