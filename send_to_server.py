import os
from PIL import Image
import ftplib
files = os.listdir()

def send_to_server(file):
	print(file)

	file = open('ftpData.txt')
	data = file.read().split('\n')

	session = ftplib.FTP(data[0],data[1],data[2])
	fil = open(file,'rb')# file to send
	session.storbinary(file, fil)# send the file
	fil.close()# close file and FTP
	file.close()
	session.quit()

	print("sent")

li=[]
for file in files:
	if file.endswith('.eps') or file.endswith('.png'):
		li.append(file)

for file in li:
	print(f'{li.index(file)+1}. {file}')

if len(li)>0:
	choice = input("Enter the file number(s) (seperated by ,. Eg-> 1,2,3) that you want to send to server: ")
	choice = choice.split(',')
	for ch in choice:
		send_to_server(li[int(ch)-1])
else:
	print("No file found")