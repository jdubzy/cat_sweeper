import curses
import random
from time import sleep
import sys
print(b'\33]0;cat sweeper\a')
def Help():
	stdscr = curses.initscr()
	stdscr.addstr(0,0,"hello everybody, welcome to cat sweeper.I hope you enjoy your time playing this game.")
	stdscr.addstr(3,0,"the goal is to get all the boxes --> # without hitting a box that contains")
	stdscr.addstr(4,0,"a bomb. If you hit a bomb you lose.")
	stdscr.addstr(6,0,"^._.^  good luck! ^._.^") 
	stdscr.addstr(8,0,"movement keys are: w,s,a,d")
	stdscr.addstr(10,0,"ps sometimes on the winner and loser screens you have to hit y or n twice.")
	stdscr.addstr(12,0,"press any key to cotinue...")
	stdscr.getch()
	stdscr.clear()
	stdscr.refresh()
	
def intro():
	stdscr = curses.initscr()
	stdscr.addstr(0,0,"           _                            ")
	stdscr.addstr(1,0,"          | |                           ")
	stdscr.addstr(2,0,"  ___ __ _| |_                          ")
	stdscr.addstr(3,0," / __/ _` | __|                         ")
	stdscr.addstr(4,0," |(_| (_| | |_                          ")
	stdscr.addstr(5,0," \___\__,_|\__|                         ")
	stdscr.addstr(6,0,"")
	stdscr.addstr(7,0," _____      _____  ___ _ __   ___ _ __  ")
	stdscr.addstr(8,0,"/ __\ \ /\ / / _ \/ _ \ '_ \ / _ \ '__| ")
	stdscr.addstr(9,0," \__ \\ V  V /  __/  __/ |_) |  __/ |    ")
	stdscr.addstr(10,0," |___/\_/\_/ \___|\___| .__/ \___|_|    ")
	stdscr.addstr(11,0,"                      | |               ")
	stdscr.addstr(12,0,"                      |_|")
	stdscr.addstr(14,0,"press any key to cotinue...")
	stdscr.getch()
	stdscr.clear()
	stdscr.refresh()
def iswinner(hit):
	stdscr = curses.initscr()
	curses.curs_set(0)
	if hit == "win":
		stdscr.clear()
		stdscr.refresh()
		stdscr.addstr(0,0,"                              _       _ ")
		stdscr.addstr(1,0,"                             (_)     | |")
		stdscr.addstr(2,0," _   _  ___  _   _  __      ___ _ __ | |")
		stdscr.addstr(3,0,"| | | |/ _ \| | | | \ \ /\ / / | '_ \| |")
		stdscr.addstr(4,0,"| |_| | (_) | |_| |  \ V  V /| | | | |_|")
		stdscr.addstr(5,0," \__, |\___/ \__,_|   \_/\_/ |_|_| |_(_)")
		stdscr.addstr(6,0,"  __/ |                                 ")
		stdscr.addstr(7,0," |___/                                  ")
		stdscr.addstr(8,10,"play again? [Y/N]")
		stdscr.noecho()
		while True:
				stdscr.noecho()
				c = stdscr.getch()
				if c == ord("y") or c == ord("Y"):
					stdscr.clear()
					stdscr.refresh()
					game()
				if c == ord("n") or c == ord("N"):
					sys.exit()
					endwin()
	if hit == "bomb":
		stdscr.clear()
		stdscr.refresh()
		stdscr.addstr(0,0," _                     _ _")
		stdscr.addstr(1,0,"| |                   | | |")
		stdscr.addstr(2,0,"| | ___  ___  ___ _ __| | |")
		stdscr.addstr(3,0,"| |/ _ \/ __|/ _ \ '__| | |")
		stdscr.addstr(4,0,"| | (_) \__ \  __/ |  |_|_|")
		stdscr.addstr(5,0,"|_|\___/|___/\___|_|  (_|_)")
		stdscr.addstr(8,0,"play again? [Y/N]")
		stdscr.getch()
		while True:
				curses.noecho()
				c = stdscr.getch()
				if c == ord("y") or c == ord("Y"):
					stdscr.clear()
					stdscr.refresh()
					game()
					break
				if c == ord("n") or c == ord("N"):
					stdscr.clear()
					stdscr.refresh()
					sys.exit()
					stdscr.endwin()
def game():
	X = 30
	Y = 15
	
	stdscr = curses.initscr()
	# the play pices
	one = [random.randint(5,5),random.randint(12,16),"#"]
	two = [random.randint(7,8),random.randint(14,20),"#"]
	three = [random.randint(8,8),random.randint(20,22),"#"]
	four =[random.randint(9,10),random.randint(23,26),"#"]
	five = [random.randint(4,4),random.randint(24,25),"#"]
	six = [random.randint(6,6),random.randint(20,22),"#"]
	seven = [random.randint(5,5),random.randint(30,35),"#"]
	eight = [random.randint(6,6),random.randint(33,38),"#"]
	nine = [random.randint(14,14),random.randint(20,22),"#"]
	ten = [random.randint(12,12),random.randint(20,22),"#"]
	eleven = [random.randint(11,11),random.randint(18,20),"#"]
	twelve = [random.randint(6,6),random.randint(25,27),"#"]
	thirteen = [random.randint(8,8),random.randint(26,26),"#"]
	fourteen = [random.randint(8,8),random.randint(35,40),"#"]
	fitheen = [random.randint(9,9),random.randint(40,45),"#"]
	sixteen = [random.randint(11,11),random.randint(35,40),"#"]
	seventeen = [random.randint(11,11),random.randint(18,20),"#"]
	eighteen = [random.randint(5,5),random.randint(40,45),"#"]
	
	LIST = [one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fitheen,sixteen,eighteen]
	bomb = random.sample(LIST,4)
	while True:
		meow = stdscr.addstr(17,13,"^._.^  meow")
		curses.curs_set(0)
		
		#drawing the borad
		stdscr.addstr(Y,X,"C")
		for wall in range(3,16):
			stdscr.addstr(wall,10,"|")
		stdscr.addstr(16,10,"--------------------------------------------")
		stdscr.addstr(2,10,"--------------------------------------------")
		for wall in range(3,16):
			stdscr.addstr(wall,53,"|")
			
		# the playing pices
		for pice in LIST:
			stdscr.addstr(pice[0],pice[1],pice[2])
		curses.noecho()
		c = stdscr.getch()
		
		# the movement keys
		if c == ord("w") or c == ord("W"):
			if Y == 3:
				Y = 4
			stdscr.clear()
			Y= Y - 1
			stdscr.addstr(Y,X,"C")
		if c == ord("s") or c == ord("S"):
			if Y == 15:
				Y = 14
			stdscr.clear()
			Y= Y + 1
			stdscr.addstr(Y,X,"C")
		if c == ord("a") or c == ord("A"):
			if X == 11:
				X = 12 
			stdscr.clear()
			X= X - 1
			stdscr.addstr(Y,X,"C")
		if c == ord("d") or c == ord("D"):
			if X == 52:
				X = 51
			stdscr.clear()
			X= X + 1
			stdscr.addstr(Y,X,"C")
		if c == ord("h") or c == ord("H"):
			stdscr.clear()
			stdscr.refresh()
			Help()
			
		# checks if you are winner or loser
		for i in LIST:
			if len(bomb) == len(LIST) and all(i in bomb for i in LIST):
				iswinner("win")
			elif Y == i[0] and X == i[1] and i in bomb:
				Y = Y 
				X = X
				sleep(.5)
				iswinner("bomb")
			elif Y == i[0] and X == i[1] and i[2] != "win":
				LIST.remove(i)
intro()
Help()
game()
