#!/usr/bin/python3

#Ping with sonar effect. A submarine feeling under the water of net
#For realistic experience, please, use headphones!

import os
import time
from tkinter import *

window = Tk()
window.title("Ping with sonar effect")
window.geometry("300x200+30+50")

def submit():
	host = host_name.get()
	return host

label = Label(window, text="Host or IP:")
label.pack(side=TOP)
host_name = Entry(window, bd=5)
host_name.pack()

def ping(event):
	host = submit()
	try:
		ping_message = []
		ping_message.append(os.system("ping %s -c 1" % host))
		if ping_message.__contains__(512) or ping_message.__contains__(256): #These numbers are ping error codes. 
			print("Input data error. Please, give a real hostname or IP!")
		else:
			os.system("mplayer sonar_ping.mp3") #instead of mplayer, you can use any other mp3 player starting from command line
			os.system("ping %s -c 1 > ping_data.txt" % host) #if you would like to preserve the earlier data, write '>>' instead of '>'
			time.sleep(1) #for a longer time to catch answer, use a bigger integer than '1'
			os.system("mplayer sonar_ping_back.mp3")
			os.system("cat ping_data.txt")
	except:
		print("Something went wrong. Please, try it later.")

def report(event):
	os.system("nano ping_data.txt")	#if you like can use your favorite editor instead of nano

def quit(event):
	window.destroy()

button1 = Button(window, text="Ping", fg="black", bd=5)
button1.place(x=116, y=80)
button1.bind("<Button-1>", ping)

button2 = Button(window, text="Report", fg="black", bd=5)
button2.place(x=10, y=150)
button2.bind("<Button-1>", report)

button3 = Button(window, text="Quit", fg="black", bd=5)
button3.place(x=210, y=150)
button3.bind("<Button-1>", quit)

mainloop()


