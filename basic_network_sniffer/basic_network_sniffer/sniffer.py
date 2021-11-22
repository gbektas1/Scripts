# Importing libraries

''' 
This script uses the scapy sniff() funtion to capture network packets.

if we want to see a detailed lists of all the scapy methods available we should run the python repl 
and then run scapy.lsc() funtion.
'''

import logging
import subprocess
import sys
from datetime import datetime

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

try:
    from scapy.all import *
    
except:
    print("Scapy package for Python is not installed on your system. ")
    print("Get it from https://pypi.python.org/pypi/scapy and try again. ")
    sys.exit()

# In the next section, we must ask the user for some parameter: interface in which to perform the packets sniffing and the number 
# of packet to sniff. Also the time alloted to perform the operations. 

print('Make sure the application is running with root privileges!!! ')

#wikipedia: In computer networking, promiscuous mode or "promisc mode"[1] is a mode for a wired network
#interface controller (NIC) or wireless network interface controller (WNIC). 

#Section: asking the user for the Interface in which to perform the packets sniffing. 

net_iface = input("* Enter tje interface on which to run the sniffer (like 'eth1'): ")

subprocess.call(["ifconfig", net_iface, 'promisc'], stdout=None, stderr=None, shell=False)

print(f'Interface {net_iface} was se to PROMISC mode. ')

#section: asking the user for the summer of packets to sniff (the "count" parameter)

pkt_to_sniff = input('Enter the number of packets to campture (0 is infinity): ')

#considering if the user enters 0 (infinity)
if int(pkt_to_sniff) !=0:
    print(f'The program will capture {pkt_to_sniff} packets. ')
    print('\n')
elif int (pkt_to_sniff) ==0:
    print('The program will capture packets until the timeout expires. ')
    print('\n')
    
    
# Asking the user for the time intervakl to sniff (the "timeout" parameter)
time_to_sniff = input("* Enter the number if seconds to run the capture: ")

# Handling the value entered by the user
if int(time_to_sniff) !=0:
    print("\nThe program will capture packets for %d seconds.\n" % int(time_to_sniff))
    
#Asking the user for any protocol filter he might want to apply to the sniffing process
#For this example I choose three protocols: ARP, BOOTP, ICMP
#You can customixe this to add your own desired protocols
proto_sniff = input("* Enter the protocol to filter by (arp|bootp|icmp|0 is all): ")

#Considering the case when the user enters 0 (meaning all protocols)
if (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp"):
    print("\nThe program will capture only %s packets.\n" % proto_sniff.upper()) 
    
elif (proto_sniff) == "0":
    print("\nThe program will capture all protocols.\n")
  
#Asking the user to enter name and path of the log file to created
file_name = input("* Please give a name to log file: ")

#Creating the text file (if it doesn't exist) for packet logging and/or opening it for appending
sniffer_log = open(file_name, "a")

#This is the function that will be called for each captured packet
#The function will extract parameters from the packet and then log each packet to the lg file
def packet_log(packet):
    
    #Getting the current timestamp
    now = datetime.now()
    
    #Writing the packet information to the log, also considering the protocol or 0 for all protocols
    if proto_sniff == "0":
        #writing the date to the log file
        print("Time: " + str(now) + "Protocol: ALL:" + " SMAC: " + packet[0].src + " DMAC: " + packet[0].dst, file = sniffer_log)
        
    elif (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp"):
        #writing the data to the log file
        print("Time: " + str(now) + " Protocol: " + proto_sniff.upper() + " SMAC: " + packet[0].src + " DMAC: " + packet[0].dst, file = sniffer_log)
