import requests
from os import system
import time
import warnings
import pyfiglet
from colorama import init
from termcolor import colored

result1 = pyfiglet.figlet_format("Ping Trace")
result2 = pyfiglet.figlet_format("By Samrat Sarkar", font = "digital" )

init()
print(colored(result1, 'green'))
print(colored(result2, 'green'))
init()
print(colored('Enter Website URL :', 'red'))
abc = input()
cbd = 'https://' + abc
warnings.filterwarnings("ignore")

x = requests.get(cbd, verify = False)
y = (x.status_code)

print("URL : ",cbd)
if y == 200:
    init()
    system("ping " + abc)
    print(colored('Website is Reachable', 'green'))
else:
    init()
    system("ping " + abc)
    print(colored('Website is not reachable', 'red'))
 
time.sleep(100000)

