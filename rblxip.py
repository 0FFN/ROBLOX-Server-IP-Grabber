import glob
import os
from time import sleep as wait
from os import system
system("title "+"Arc's ROBLOX Server IP Puller")

print(r'''
___     _    _           ___                        ___ ___   ___      _ _         
| _ \___| |__| |_____ __ / __| ___ _ ___ _____ _ _  |_ _| _ \ | _ \_  _| | |___ _ _ 
|   / _ \ '_ \ / _ \ \ / \__ \/ -_) '_\ V / -_) '_|  | ||  _/ |  _/ || | | / -_) '_|
|_|_\___/_.__/_\___/_\_\ |___/\___|_|  \_/\___|_|   |___|_|   |_|  \_,_|_|_\___|_|  

[-} By arc. 
[-] Wait for Roblox to fully load before using, otherwise you'll be getting the previous games IP.
''')

input("[!] -> Press [ENTER] to grab server IP! ")

username = os.getenv('username')
list_of_files = glob.glob(r'C:\users\{}\AppData\Local\Roblox\logs\*'.format(username))
latest_file = max(list_of_files, key=os.path.getctime)
roblox_log = open(latest_file, 'r')

for line in roblox_log:
    if 'Connection accepted from' in line:
        line = line.replace('Connection accepted from', '')
        line2 = line.replace('|', ':')
        line3 = line2[57:]
        print("\n>>> Server IP => " + line3)
        wait(99999)
