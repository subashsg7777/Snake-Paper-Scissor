import random 
from tkinter import *
import tkinter as tkk
#  creating the root file of GUI 
dashboard = tkk.Tk()
# setting up the root file 
dashboard.geometry("300x300")
dashboard.title("Snake Water Gu Game (Mark1)")
'''bg_image = tkk.PhotoImage(file = "C:\\Users\\Subash_G Mark2\\Pictures\\Saved Pictures\\O.ppm")
limg = Label(dashboard,i = bg_image)
limg.pack()'''
dashboard.configure(bg='gold') 
winning_choice = ""
def decision():
	#creating the random choice 
	global winning_choice
	winning_choice = random.choice(['S','P','SC'])
	print("decision is made sucessfully!",winning_choice)
# dashboard.gb()
message = Label(dashboard,text = "Please Select Choice from Below ")
message.configure(bg='orange') 
options = Label(dashboard,text=" S-stone,P- paper ,SC-scissor")
options.configure(bg='purple') 
# creating the global variables
soption = ""
def stone_option():
	global soption
	global winning_choice
	soption ="S"
	pass
	decision()
	s1 = play(soption)
def paper_option():
	global soption
	global winning_choice
	soption = "P"
	pass
	decision()
	s1 = play(soption)
def sc_option():
	global soption
	global winning_choice
	soption = "SC"
	pass
	decision()
	s1 = play(soption)
def play(schoice):
	global winning_choice
	if(schoice == winning_choice):
		result = Label(dashboard,text="Tied!")
		result.pack()
		dashboard.configure(bg='pink')
	elif(schoice == "S" and winning_choice == "SC"):
		result = Label(dashboard,text="You Won the Game!")
		result.pack()
		dashboard.configure(bg='green')

	elif(schoice =="P" and winning_choice == "S"):
		result = Label(dashboard,text="You Won the Game!")
		result.pack()
		dashboard.configure(bg='green')

	elif(schoice == "SC" and winning_choice == "P"):
		result = Label(dashboard,text="You Won the Game!")
		result.pack()
		dashboard.configure(bg='green')
	else :
		result = Label(dashboard,text="You Loosed!")
		result.pack()
		dashboard.configure(bg='red')
stone_button = Button(dashboard,text = "Stone",command = stone_option,width = 40,bg ="brown")
paper_button = Button(dashboard,text = "Paper",command = paper_option,width = 40,bg ="white")
sc_button = Button(dashboard,text = "Scissor",command = sc_option,width = 40,bg ="orange")
#secret_button = Button(dashboard,text = "",command = play)

# here we pack all of our componets
message.pack()
options.pack()
stone_button.pack()
paper_button.pack()
sc_button.pack()
dashboard.mainloop()