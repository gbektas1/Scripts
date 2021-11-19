import sys
from termcolor import colored

print('\n')
print(colored(f"The name of this script is: {sys.argv[0]}", 'blue' ))
print(colored(f'\n The number of this particular argument or parameter is: {len(sys.argv[0])}', 'red' ))
print(colored(f"\n The list of argument are: {str(sys.argv)}", "cyan" ))
print(colored(f'\n My first argument is: {str(sys.argv[1])}', 'green' ))
print(colored(f'\n My second argument is: {str(sys.argv[2])}' 'yellow' ))
print(colored(f'\n My third argument is: {str(sys.argv[3])}' 'orange' ))
print('\n')

print(colored(f'\n The name of this OS platform is: {sys.platform}' 'blue'))
print(colored(f'\n The Current Python version is: {sys.version}' 'blue'))
print(colored(f'\n The Path to the Python interpreter is: {sys.path}' 'blue'))


        
 

