import os
from termcolor import colored

print('\n')

pwd = os.getcwd()
list_of_files= os.listdir(pwd)
for directory in list_of_files:
    print(colored(f'[+] {files}', 'green'))
    

print('\n')  