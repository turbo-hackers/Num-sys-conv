#!/usr/bin/env python3
# coded by TURB0
# github https://github.com/turbo-hackers

# hexadecimal to binary,decimal,octal

# colors
r ='\033[91m' # red
g ='\033[92m' # green
b = '\033[94m' # blue
y = '\033[93m' # yellow
s_b ='\033[96m' # sky_blue
pi = '\033[35m' # pink
reset = '\033[0m' # reset
blink = "\033[5;92m" # blink


def hexadecimal():
	
	def to_binary(num):
		num = num.strip().upper()
		point = False
		hex_table = { "0": "0000", "1": "0001", "2": "0010", "3": "0011",
			"4": "0100", "5": "0101", "6": "0110", "7": "0111",
			"8": "1000", "9": "1001", "A": "1010", "B": "1011",
			"C": "1100","D": "1101", "E": "1110", "F": "1111"}
		if '.' in num:
			point = True
			num_list = num.split('.')
		if point != True:
			ans = ""
			for i in num:
				ans += hex_table[i] + " "
			out_ans = ans
		else:
			ans = ""
			ans2 = "."
			for i in num_list[0]:
				ans += hex_table[i] + " "
			for j in num_list[1]:
				ans2 += hex_table[j] + " "
			total_ans = str(ans)+str(ans2)
			out_ans = total_ans
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"   "+s_b+"""Hexadecimal"""+reset+"""   """+pi+""">>>"""+reset+"""      """+g+"""Binary"""+reset+"""      """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""    """+pi+""">>>"""+reset+"""   """+g,out_ans,pi+"""
  +------------------+-------------------+"""+reset)
	
	def to_decimal(num):
		num = num.strip().upper()
		hex_table = {'0': 0, '1': 1, '2': 2, '3': 3,
				'4': 4, '5': 5, '6': 6, '7': 7,
				'8': 8, '9': 9, 'A': 10, 'B': 11,
				'C': 12, 'D': 13, 'E': 14, 'F': 15}
		t = -1
		l = len(num)
		opt = opt2 = 0
		point = False
		if '.' in num:
			point = True
			num_list = num.split(".")
			len_left = l-len(num_list[1])-1
		else:
			num_list = list(num)
			len_left = l
		if point != True:
			ans_list = []
			len_left -= 1
			for i in num_list:
				opt = hex_table[i]*16**len_left
				len_left -= 1
				ans_list.append(opt)
			ans = sum(ans_list)
		else:
			ans_list = []
			len_left -= 1
			for i in num_list[0]:
				opt = hex_table[i]*16**len_left
				ans_list.append(opt)
				len_left -= 1
			ans_list2 = []
			for j in num_list[1]:
				opt2 = hex_table[j]*16**t
				ans_list2.append(opt2)
				t-=1
			ans = sum(ans_list) + sum(ans_list2)
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"   "+s_b+"""Hexadecimal"""+reset+"""   """+pi+""">>>"""+reset+"""      """+g+"""Decimal"""+reset+"""     """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""     """+pi+""">>>"""+reset+"""    """+g,ans,pi+"""
  +------------------+-------------------+"""+reset)
	
	print(pi+"""
   +---------------------+
   |"""+s_b+""" From Hexadecimal To """+pi+"""|
   +---------------------+
   |"""+reset+"    "+s_b+"""1 """+y+"""->>"""+g+""" Binary"""+reset+"""     """+pi+"""|
   +---------------------+
   |"""+reset+"    "+s_b+"""2 """+y+"""->>"""+g+""" Decimal"""+reset+"""    """+pi+"""|
   +---------------------+"""+reset)

	to_choice = int(input(y+"""
   ┌──["""+b+"""Enter the option"""+y+"""]"""+reset+"""
   """+y+"""└─ᐳ  """+s_b))
	if to_choice <= 2 and to_choice != 0:
		num = input(y+"""
   ┌──["""+b+"""Enter the number to convert"""+y+"""]"""+reset+"""
   """+y+"""└─ᐳ  """+s_b)
		print(reset)
		if to_choice == 1:
			to_binary(num)
		elif to_choice == 2:
			to_decimal(num)
		else:
			print(s_b+"  ["+r+"Input-Error"+s_b+"]:"+reset+r+" Wrong Input !, try again"+reset)
	else:
		print(s_b+"  ["+r+"Input-Error"+s_b+"]:"+reset+r+" Wrong Input !, try again"+reset)
#hexadecimal()
