

# Created by : Gokan Bektas
# Input      : This application will take input IP address and converts to binary and gets network brodcast from the binary strings 
# Output     : Print out network and broadcast address, wildcard mask and mask bit. 



#####Application Phase I


import random
import sys

def subnet_cal():
    try:
        print('\n')
        
        # Checking the IP address Validity:
        while True:
            ip_address = input("Enter an IP Address: ")
            
            # Checking octets
            ad = ip_address.split('.')
    
            if (len(ad) == 4) and (1<= int(ad[0]) <= 223) and (int(ad[0]) != 127) and (int(ad[0]) != 169 or int(ad[1]) != 254) and (0 <= int(ad[1]) <= 255 and 0 <= int(ad[2]) <= 255 and 0 <= int(ad[2]) <= 255 and 0 <= int(ad[3]) <= 255):
                break
            
            #if (len(ad) == 4) and (1<= int(ad[0]) <= 223) and (int(ad[0]) != 127) and (int(ad[0]) != 169 or int(ad[1]) != 254) and (0 <= int(ad[1]) <= 255 and 0 <= int(ad[2]) <= 255 and 0 <= int(ad[2]) <= 255 and 0 <= int(ad[3]) <= 255):
                #break
            
            else:
                print('\n The IP Adress is INVALID! Please try again ')
                continue
            
            
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
            
                  
         # Cheking Subnet Mask Validity
        while True:
            subnet_mask = input('Enter a Subnet Mask: ')
            
            # checking octets
            b = subnet_mask.split('.')
            
            if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
                break
            
            else:
                print('\nThe Subnet Mask is INVALID! Please try again!')
                continue
            
##### Application phase II
        # Create a process or algorthm for the identification of a subnet based on IP abd subnet mask.
        # Conver mask to binary str
        mask_octets_padded =[]
        mask_octets_decimal = subnet_mask.split('.')
        #print(mask_octets_decimal)
        
        for octet_index in range(0, len(mask_octets_decimal)):
            
            #print bin(int(mask_octets_decimal[octet_index]))
            
            binary_octet = bin(int(mask_octets_decimal[octet_index])).split('b')[1]
            #print(binary_octet)
            
            if len(binary_octet) == 8:
                mask_octets_padded.append(binary_octet)
                
            elif len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8) 
                mask_octets_padded.append(binary_octet_padded)
                
        #print(mask_octets_padded)
        
        decimal_mask = ''.join(mask_octets_padded)
        # print(decimal_mask) 
        # e.g. for 255.255.255.0 => 1111111111111111111111100000000
        
        # Count host bits in the mask and the calculate number of host/subnet
        
        no_of_zeros = decimal_mask.count('0')
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2) #return positive value for mask /32
        
        # print(no_of_zeros)
        # print(no_of_ones)
        # print(no_of_hosts)
        
        #Obtaining wildcard mask
        '''
        A wildcard mask is similar to a subnet in that it uses the ANDing process to itendify which bots in an IPv4 address to match.
        However, a wildcard mask and a subnet differ in the way they match binary is and 8s.
        '''
        
        
        wildcard_octets = []
        for w_octet in mask_octets_decimal:
            wild_octet = 255 - int(w_octet)
            wildcard_octets.append(str(wild_octet))
          #print(wildcard_octets)  
                    
        wildcard_mask = '.'.join(wildcard_octets)    
          #print wildcard_mask  
            
##### Application phase III

        #Convert IP to binary string
        ip_octets_padded = []
        ip_octets_decimal = ip_address.split('.')
        
        for octet_index in range(0, len(ip_octets_decimal)):
            
            binary_octet = bin(int(ip_octets_decimal[octet_index])).split('b')[1]
            
            if len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                ip_octets_padded.append(binary_octet_padded)
                
            else:
                ip_octets_padded.append(binary_octet)
                
        # print(ip_octet_padded)  
        
        binary_ip = ''.join(ip_octets_padded)
        
    
        #print(binary_ip) #e.g. for 192.168.2.100 ==>  1111111111111111111111100000000
        
        # Get the network address and broadcast address from the binary string obtained above
        
        network_address_binary = binary_ip[:(no_of_ones)] + '0' * no_of_zeros
        #print(network_address_binary)
        
        broadcast_address_binary = binary_ip[:(no_of_ones)] + '1' * no_of_zeros
        #print(broadcast_address_binary)
        
        net_ip_octets = []
        for octet in range(0, len(network_address_binary), 8):
            net_ip_octet = network_address_binary[octet:octet+8]
            net_ip_octets.append(net_ip_octet)
            
        #print(net_ip_octets)
        
        net_ip_address = []
        for each_octet in net_ip_octet:
            net_ip_address.append(str(int(each_octet, 2)))
            
        #print(net_ip_adress)
        
        network_address = '.'.join(net_ip_address)
        
        #print(network_address)
        
        
        
        bst_ip_octets = []
        for octet in range(0, len(broadcast_address_binary), 8):
            bst_ip_octet = broadcast_address_binary[octet:octet + 8]
            bst_ip_octets.append(bst_ip_octet)
        #print(bst_ip_address)
            
        bst_ip_address = []
        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))
            
        #print(bst_ip_address)
        
        broadcast_address = '.'.join(bst_ip_address)
        #print(broadcast_address)
        
        ###Results for the selected IP/Mask
        print('\n')
        print(f'Network address is : {network_address} ')
        print(f'Broadcast address is: {broadcast_address} ')
        print(f'Number of valid host per subnet: {no_of_hosts} ')
        print(f'Wildcard mask: {wildcard_mask} ')
        print(f'Mask bit: {no_of_ones} ')
        print('\n')
    
    

####Application Phase IV 
        # Generation of random IP in subnet
        while True:
            generate = input(' Do you want to generate random IP address from subnet? (y/n) ')
            
            if generate == 'y':
                generated_ip = []
                # Obtain avaliable adress in range based on the difference between octets in broadcast address and network address
                for indexb, oct_bst in enumerate(net_ip_address):
                    #print(indexb, oct_bst)
                    for indexn, oct_net in enumerate(net_ip_address):
                        # print(indexn, oct_net)  
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                # add identical octerts to generated ip list 
                                generated_ip.append(oct_bst)
                            
                            else:
                                # generate random numbers from within octet intervals and append them to the list
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))    
                                
                                
                # IP address generated from the subnet pool
                # print(generated_ip)
                y_iaddr = '.'.join(generated_ip)
                #print(y_iaddr)
                
                print(f'Random IP address is: {y_iaddr}')
                print('\n')
                continue
            
            else:
                print('Thank you for trying our app .... Have a Good Day!!! ... Cheers ')
                break
            
                         
                         
                
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#### Application Phase V
    
        
        
                                        
    except KeyboardInterrupt:
        print('\n\nProgram aborted by the user, Exiting now...')
        sys.exit()
        
        
        

subnet_cal()