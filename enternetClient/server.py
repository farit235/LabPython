import socket
import smtplib
import uuid

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode("utf-8")
            email, message = data.split("|")
            if not email or not message:
                print("Error!")
                conn.sendall(b'Error!')
                break
            else:
                id_user = str(uuid.uuid4())
                sendmail("Subject:" + id_user + message)
                sendmail("Sibject:" + id_user)
                break
