from django.shortcuts import render
import socket
import sys
import logging

logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
logger.info('info message')

path = "file.txt"
def read_txt(path):
    with open(path,'r') as file:
        data = file.read().split(' ')
        return data

def read_str(MSG):
    data = MSG.split(' ')
    return data

def server_program(data):
    host = socket.gethostname()
    port = 6000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    conn, address = server_socket.accept()

    print("To connected user: " + str(data))

    conn.send(data.encode())
    conn.close()

def split(data,NUMOFCL):
    r =[]
    s=""
    n,i=0,0
    while(n < NUMOFCL):
        for i in range (n, len(data), NUMOFCL):
            if(i<len(data)):
                s+=data[i]
        n+=1
        r.append(s)
        s=""
    return r




    # data = read_txt(path)
    #
    # print(f"Your messages: {data}")
    # flage = True
    # while(flage):
    #     try:
    #         NUMOFCL = int(input("Input num of clients: "))
    #         flage = False
    #     except ValueError:
    #         print("That's not an int!")
    # l_mes = (list(split(data)))
    # for s in l_mes:
    #     server_program(s)

global MSG,data,NUMOFCL,rec_data

def client_program():
    global rec_data
    host = socket.gethostname()
    port = 6000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    rec_data = client_socket.recv(1024).decode()
    print('Received from server: ' + rec_data)
    client_socket.send('message'.encode())

    client_socket.close()

def index_page(requests):
    global MSG,NUMOFCL
    NUMOFCL = requests.POST.get('api', False)
    MSG = requests.POST.get('secret', False)
    print('---------------------------------')
    print(NUMOFCL, MSG)
    print('---------------------------------')
    return render(requests, 'Server.html',{'title':"Server",'NUMOFCL':str(NUMOFCL),'MSG':str(MSG),'INFO':"ABRAMIAN"})

def CON(requests):
    global data
    data = read_str(str(MSG))
    l_mes = (list(split(data,int(NUMOFCL))))
    for s in l_mes:
        server_program(s)
        logger.info(str(" SENT: ") + str(s))
    return render(requests, 'Server.html',{'Title':"Server"})


def info(requests):
    return render(requests, 'new.html',{'NUM':str('ABRAMIAN')})


def CLI(requests):
    host = socket.gethostname()
    port = 6000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    rec_data = client_socket.recv(1024).decode()
    print('Received from server: ' + rec_data)
    client_socket.send('message'.encode())
    # logger.log(1,rec_data)
    logger.info(str(" ACCEPTED: ") + rec_data)

    client_socket.close()
    return render(requests, 'Client.html', {'Title': "Client", 'DATA': rec_data})