import os
from subprocess import call

print('Current path is ', os.getcwd())
print('PATH Emviroment Variable: ', os.getenv('PATH'))
print("List files with the IS Module: ")
os.system('ls , -la')
print('List files with Subprocess Module: ')
call(['ls', '-la'])

