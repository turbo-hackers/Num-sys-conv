#!/usr/bin/env python3
# coded by TURB0
# github https://github.com/turbo-hackers

# octal to binary,decimal

# colors
r ='\033[91m' # red
g ='\033[92m' # green
b = '\033[94m' # blue
y = '\033[93m' # yellow
s_b ='\033[96m' # sky_blue
pi = '\033[35m' # pink
reset = '\033[0m' # reset
blink = "\033[5;92m" # blink


def octal():
	
	def to_binary(num):
		num = num.strip().upper()
		point = False
		oct_table = { "0": "000", "1": "001",
			"2": "010", "3": "011",
			"4": "100", "5": "101",
			"6": "110", "7": "111"}
		
		if '.' in num:
			point = True
			num_list = num.split('.')
		if point != True:
			ans = ""
			for i in num:
				ans += oct_table[i] + " "
			out_ans = ans
		else:
			ans = ""
			ans2 = "."
			for i in num_list[0]:
				ans += oct_table[i] + " "
			for j in num_list[1]:
				ans2 += oct_table[j] + " "
			total_ans = str(ans)+str(ans2)
			out_ans = total_ans
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"      "+s_b+"""Octal"""+reset+"""      """+pi+""">>>"""+reset+"""      """+g+"""Binary"""+reset+"""      """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""    """+pi+""">>>"""+reset+"""   """+g,out_ans,pi+"""
  +------------------+-------------------+"""+reset)
	
	def to_decimal(num):
		l = len(num)
		t = -1
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
				opt = int(i)*8**len_left
				len_left -= 1
				ans_list.append(opt)
			ans = sum(ans_list)
		else:
			ans_list = []
			len_left -= 1
			for i in num_list[0]:
				opt = int(i)*8**len_left
				len_left -= 1
				ans_list.append(opt)
			ans_list2 = []
			for j in num_list[1]:
				opt2 = int(j)*8**t
				t-=1
				ans_list2.append(opt2)
			ans = sum(ans_list) + sum(ans_list2)
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"      "+s_b+"""Octal"""+reset+"""      """+pi+""">>>"""+reset+"""     """+g+"""Decimal"""+reset+"""      """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""     """+pi+""">>>"""+reset+"""    """+g,ans,pi+"""
  +------------------+-------------------+"""+reset)
	
	print(pi+"""
   +---------------------+
   |"""+reset+"""    """+s_b+"""From Octal To"""+reset+"""    """+pi+"""|
   +---------------------+
   |"""+reset+"    "+s_b+"""1 """+y+"""->>"""+g+""" Binary"""+reset+"""     """+pi+"""|
   +---------------------+
   |"""+reset+"    "+s_b+"""2 """+y+"""->>"""+g+""" Decimal"""+reset+"""    """+pi+"""|
   +---------------------+"""+reset)

	to_choice = int(input(y+"""
   ┌──["""+b+"""Enter the option"""+y+"""]"""+reset+"""
   """+y+"""└─ᐳ  """+s_b))
	print(reset)
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
#octal()
