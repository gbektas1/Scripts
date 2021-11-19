import socket    
import psutil
host_name = socket.gethostname()    
IPAddress = socket.gethostbyname(host_name)    
print("Your Computer Name is:" + host_name)    
print("Your Computer IP Address is:" + IPAddress) 
#How to get the IP address of a client using socket module

ip = socket.gethostbyname (socket.gethostname())
for port in range(10):      #check for all available ports
    try:
   
        serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
        serv.bind((ip,port)) # bind socket with address
              
    except:
  
        print('[OPEN] Port open :',port) #print open port number
    serv.close() #close connection
#How to check ports are open or not. 
    

hostname, aliases, addresses = socket.gethostbyaddr('192.168.122.124')
print ('Hostname:', hostname)
print ('Aliases :', aliases)
print ('Addresses:', addresses)
#how to get dns information



print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting % usage of virtual_memory ( 3rd field)