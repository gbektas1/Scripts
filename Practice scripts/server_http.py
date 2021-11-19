import socket

'''
The purpose of this script is to create an HTTP Server in order to connect, send and recieve data!

'''


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))

sock.listen(5)
while True:
    print('Awating for connections.....! ')
    (recvSocket, Address) = sock.accept()
    print('HTTP reguest recieved: ')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes('HTTP/1.1 200 ok\r\n\r\n <html><body><h1>Hi There.... You are up, good luck</h1></body></html> \r\n ', 'utf-8'))
    recvSocket.close(0)