import socket

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        email = str(input("Введите email: "))
        message = str(input("Введите сообщение: "))
        s.sendall((email+"|"+message).encode("utf-8"))
        data = s.recv(1024)
        print('Received', repr(data))
    except Exception as e:
        print(e)
s.close()
