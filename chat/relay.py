from threading import Thread
import json
import socket
import rooms
from encryption import *

def online():
    #checks if server online and updates the list of rooms
    return



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',81))
s.listen(5)


checkOnline = Thread(target=online,args=[])
checkOnline.start()


while True:
    conn , addr = s.accept()
    data = decrypt(conn.recv(1024))
    data = json.loads(data)
    print('new connection ',data,' ',addr)

    if data['action']  == 'newroom':
        if rooms.exists(data['room']):
            conn.send(encrypt('False'))
        else:
            rooms.add(data['room'],addr[0])
            conn.send(encrypt('True'))        

    elif data['action'] == 'joinroom':
        if rooms.exists(data['room']):
            conn.send(encrypt(rooms.get(data['room'])))
        else:
            conn.send(encrypt('0.0.0.0'))

    
    elif data['action'] == 'close':
        rooms.remove(data['room'],addr[0])

    conn.close()


# this module is functional
# implement online function