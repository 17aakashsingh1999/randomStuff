import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',80))
s.listen()

header = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'

file = open('index.html','br')
html = file.read()
file.close()

while True:
    conn,addr=s.accept()
    print(conn.recv(10000))
    conn.send(header+html)
    conn.close()
    
    
