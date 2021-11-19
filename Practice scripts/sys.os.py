import sys
import os
from termcolor import colored


print('\n')

if len(sys.argv) == 2:
    name_of_file = sys.argv[1]
    print(name_of_file)
    if os.path.isfile(name_of_file):
        print(colored(f'[+] The file named {name_of_file} exists ', 'green'))
        exit(0)
    else:
        print(colored(f'[-] The file named {name_of_file} DOES NOT EXIST', 'red'))
        exit(0)
    if not os.access(name_of_file, os.R_okfile):
        print(f'[-] Access to file {name_of_file} is DENIED ')
        exit(0)