# this module handles all client side work

from threading import Thread
import json
import socket
import getpass
from encryption import *

ip = "0.0.0.0"
relayServer = "127.0.0.1"
port = 82


def draw():
    #this function draws the chat window
    #maybe use tkinter
    return

def listener(conn):
    while True:
        data = json.loads(decrypt(conn.recv(1024)))
        msg = data['user']+': '+data['message']
        print(msg)

conn = socket.create_connection((relayServer,81))

payload = {'action':'joinroom','room':input('Input name of room you want to join: ')}

while True:             #get a valid room
    conn.send(encrypt(json.dumps(payload)))
    ip = decrypt(conn.recv(1024))
    if ip == '0.0.0.0':
        payload['room']=input('room doesnt exist. Input name of room you want to join: ')
        continue
    else:
        conn.close()
        break

payload.clear()
payload={'user':input('Enter your username: '),'passw':getpass.getpass('Enter the server password: ')}

conn = socket.create_connection((ip,port))

while True:              #login to server
    conn.send(encrypt(json.dumps(payload)))
    if decrypt(conn.recv(1024)) == 'False':
        payload['passw']=getpass.getpass('wrong password. Enter the server password: ')
        continue
    else:
        break


payload.clear()
payload={'type':'msg','msg':''}

Thread(target=listener,args=[conn,]).start()


while True:
    payload['msg'] = input('')
    # add string processing and sendfile mode
    conn.send(encrypt(json.dumps(payload)))