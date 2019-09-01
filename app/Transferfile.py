import io
from base64 import b64encode
import eel

import socket

eel.init('web')


@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

@eel.expose
def id_name():
    return socket.gethostname()

@eel.expose
def send_file(data):
    s = socket.socket()
    host = socket.gethostname()
    print(host)
    port = 8080
    s.bind((host,port))
    s.listen(1)
    print("wating for any incoming connections ...")
    conn, addr = s.accept()
    print(addr,"Has connected to the server")

    #filename = input(str("Plese enter a filename of the file : "))
    #filename = data[len("DATA:   C:\fakepath\\"):]
    filename = data[12:]
    #print(filename)
    file = open(filename , 'rb')
    #file_data = file.read(1024)
    #file_data = file.read()
    for line in file:
        conn.send(line)

    #conn.send(file_data)
    print("Data has been trasmitted successfuly")

@eel.expose
def receive_file(name,file_name):

    s = socket.socket()
    #host = input(str("Plese enter the host address of the sender"))
    host = name
    port = 8081
    s.connect((host,port))
    print("connected")


    #filename = input(str("Plese enter a filename for the incoming file : "))
    file = open(file_name , 'wb')
    file_data = s.recv(1024)
    while(len(file_data)>0):
        file.write(file_data)
        file_data = s.recv(1024)

    file.close()
    print("File has been recived successufluly")

#eel.start('index.html', size=(1000, 600))
#eel.start('Tfp2p.html', size=(1000, 600))
eel.start('init.html', size=(1000, 600))
