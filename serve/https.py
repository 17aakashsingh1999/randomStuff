import socket
import ssl

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss=ssl.wrap_socket(s,certfile='cert.cer',keyfile='key.pem',server_side=True)

ss.bind(('',443))
ss.listen()

header = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'

file = open('index.html','br')
html = file.read()
file.close()

while True:
    conn,addr=ss.accept()
    print(addr,'connected  ')
    print(ss.recv(10000))
    conn.sendall(header+html)
    conn.close()
    print(addr,'disconnected')

