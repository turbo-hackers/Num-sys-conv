#!/usr/bin/python3
# coded by TURB0
# github https://github.com/turbo-hackers

from core import Binary
from core import Decimal
from core import Octal
from core import Hexadecimal
import os

# colors
r ='\033[91m' # red
g ='\033[92m' # green
b = '\033[94m' # blue
y = '\033[93m' # yellow
s_b ='\033[96m' # sky_blue
pi = '\033[35m' # pink
reset = '\033[0m' # reset
blink = "\033[5;92m" # blink

def main():
	
	def banner():
		os.system("clear")
		print(b+"""
  __                _______ """+g+"""    _______ __     __ _______"""+b+"""
 |  \\    /||\\    /|(       )"""+g+"""   (  _____\\\\ \   / /(  _____\\"""+b+"""
 | (\\\\  ( || |  | || () () |"""+y+"""___"""+g+"""| (_____  \\ \\ / / | (_____"""+b+"""
 | | \\\\ | || |  | || |(_)| """+y+"""(___)"""+g+"""_____  )  \\( )/  (_____  )"""+b+"""
 | )  \\\\) || (__) || )   ( |"""+g+"""    _____) |   | |    _____) |"""+b+"""
 |/    \\__| \\____/ |/     \|"""+g+"""   \\_______)   \\_/   \\_______)"""+reset+"""
             """+s_b+""" ____"""+reset+"""
             """+s_b+"""(  __| _          __ _ ___ __ _"""+reset+"""
             """+s_b+"""| (___/.\|\ |(  )|_ |_) | |_ |_)"""+reset+"""
             """+s_b+"""(____/\_/| \| \/ |__| \ | |__| \ """+b+"""v1.0"""+reset)
		print("")
		print("          "+y+"<========[[ "+b+"coded by "+blink+"TURB0"+reset+y+" ]]========>"+reset)
		print("       "+y+"<--------( "+r+"Github : turbo-hackers"+y+" )-------->"+reset)

	banner()
	print(pi+"""
   +------------------+
   |"""+reset+"""       """+s_b+"""From"""+reset+"""       """+pi+"""|
   +------------------+-------------------+
   |"""+reset+"  "+s_b+"""1 """+y+"""->"""+g+""" Binary"""+reset+"""     """+pi+"""|"""+reset+"""  """+s_b+"""2 """+y+"""->"""+g+""" Decimal"""+reset+"""     """+pi+"""|
   +------------------+-------------------+
   |"""+reset+"  "+s_b+"""3 """+y+"""->"""+g+""" Octal"""+reset+"""      """+pi+"""|"""+reset+"""  """+s_b+"""4 """+y+"""->"""+g+""" Hexadecimal"""+reset+""" """+pi+"""|
   +------------------+-------------------+"""+reset)

	choice = int(input(y+"""
   ┌──["""+b+"""Enter the option"""+y+"""]"""+reset+"""
   """+y+"""└─ᐳ  """+s_b))
	print(reset)
	if choice == 1:
		banner()
		Binary.binary()
	elif choice == 2:
		banner()
		Decimal.decimal()
	elif choice == 3:
		banner()
		Octal.octal()
	elif choice == 4:
		banner()
		Hexadecimal.hexadecimal()
	else:
		print(s_b+"  ["+r+"Input-Error"+s_b+"]"+reset+r+" Wrong Input !, try again"+reset)
try:
	main()
except:
	print(s_b+"  ["+r+"Main-Code-Error"+s_b+"]"+reset+r+" Something Wrong !, try again"+reset)
