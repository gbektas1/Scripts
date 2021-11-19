import socket

'''
This script will create a socket and will connect target host and send and recieve data.

'''

print('Creating a socket.....')
print('\n')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('\n')
print('Socket Created! ')
print('\n')
print('Connecting to a remote host...')
print('\n')
target_host = 'www.google.com'
port_host = 80
sock.connect((target_host, port_host))
print('.....Connection okay!! ')
print('\n')

request ="GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
sock.send(request.encode())

data = sock.recv(4096)
print('Data', str(bytes(data)))
print('\n')
print('Length', len(data))
print('\n')
print('Closing the socket')
socket.close(0)