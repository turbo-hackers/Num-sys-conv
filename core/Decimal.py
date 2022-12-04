#!/usr/bin/env python3
# coded by TURB0
# github https://github.com/turbo-hackers

#   decimal to binary,octal,hexadecimal

# colors
r ='\033[91m' # red
g ='\033[92m' # green
b = '\033[94m' # blue
y = '\033[93m' # yellow
s_b ='\033[96m' # sky_blue
pi = '\033[35m' # pink
reset = '\033[0m' # reset
blink = "\033[5;92m" # blink


def decimal():
	
	def to_binary(num):
		num_l1= []
		def to_bin(n):
			if n > 1:
				to_bin(n//2)
			num_l1.append(n%2)
		point = False
		if '.' in num:
			point = True
			num = num.strip()
			num_list = num.split(".")
			num_mod = '0.'+num_list[1]
			del num_list[1]
			num_list.append(num_mod)
		else:
			num = int(num)
		if point != True:
			to_bin(num)
			ans = ""
			for i in num_l1:
				ans += str(i)
			out_ans = ans
		else:
			to_bin(int(num_list[0]))
			ans = ""
			for i in num_l1:
				ans += str(i)
			times = 0 # 0-5
			ans_p_l = []
			ans1 = float(num_list[1])
			opt_st = True
			while (times!=5) and (opt_st == True):
				times += 1
				opt = float(ans1*2)
				ans_p_l.append(int(opt))
				ans1 = opt-int(opt)
				if ans1 == 0.0 or ans1 == 0:
					opt_st = False
			ans2 = "."
			for j in ans_p_l:
				ans2 += str(j)
			total_ans = str(ans)+str(ans2)
			out_ans = total_ans
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"     "+s_b+"""Decimal"""+reset+"""     """+pi+""">>>"""+reset+"""     """+g+""" Binary"""+reset+"""      """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""    """+pi+""">>>"""+reset+"""    """+g,out_ans,pi+"""
  +------------------+-------------------+"""+reset)
	
	def to_octal(num):
		point = False
		def to_octa(num):
			global ans
			ans_l1 = []
			while (num/8>=1):
				opt = num/8
				if type(opt) == float:
					opt1 = (opt - int(opt)) * 8
					ans_l1.append(int(opt1))
					num = int(opt)
					if opt < 8:
						ans_l1.append(int(opt))
						num = 1
				else:
					ans_l1.append(int(opt))
					num = int(opt)
			ans_l1.reverse()
			ans = ""
			for i in ans_l1:
				ans += str(i)
		if '.' in num:
			point = True
			num = float(num)
		else:
			num = int(num)
		if point != True:
			to_octa(num)
			out_ans = ans
		else:
			to_octa(num)
			times = 0 # 0-5
			ans_p_l = []
			opt_st = True
			ans1 = num - int(num)
			while (times!=5) and (opt_st == True):
				times += 1
				opt = float(ans1*8)
				ans_p_l.append(int(opt))
				ans1 = opt-int(opt)
				if ans1 == 0.0 or ans1 == 0:
					opt_st = False
			ans2 = "."
			for j in ans_p_l:
				ans2 += str(j)
			total_ans = str(ans)+str(ans2)
			out_ans = total_ans
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"     "+s_b+"""Decimal"""+reset+"""     """+pi+""">>>"""+reset+"""     """+g+""" Octal"""+reset+"""       """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""     """+pi+""">>>"""+reset+"""    """+g,out_ans,pi+"""
  +------------------+-------------------+"""+reset)
	
	def to_hexadecimal(num):
		
		point = False
		hex_table = {'0': 0, '1': 1, '2': 2, '3': 3,
			'4': 4, '5': 5, '6': 6, '7': 7,
			'8': 8, '9': 9, 'A': 10, 'B': 11,
			'C': 12, 'D': 13, 'E': 14, 'F': 15}
			
		def to_hexa(num):
			global ans
			ans_l1 = []
			while (num/16>=1):
				opt = num/16
				if type(opt) == float:
					opt1 = (opt - int(opt)) * 16
					ans_l1.append(int(opt1))
					num = int(opt)
					if opt < 16:
						ans_l1.append(int(opt))
						num = 1
				else:
					ans_l1.append(int(opt))
					num = int(opt)
			ans_l1.reverse()
			ans = ""
			for i in ans_l1:
				ans += str(list(hex_table.keys())[list(hex_table.values()).index(i)])
		if '.' in num:
			point = True
			num = float(num)
		else:
			num = int(num)
		if point != True:
			to_hexa(num)
			out_ans = ans
		else:
			to_hexa(num)
			times = 0 # 0-5
			ans_p_l = []
			opt_st = True
			ans1 = num - int(num)
			while (times!=5) and (opt_st == True):
				times += 1
				opt = float(ans1*16)
				ans_p_l.append(int(opt))
				ans1 = opt-int(opt)
				if ans1 == 0.0 or ans1 == 0:
					opt_st = False
			ans2 = "."
			for j in ans_p_l:
				ans2 += str(list(hex_table.keys())[list(hex_table.values()).index(j)])
			total_ans = str(ans)+str(ans2)
			out_ans = total_ans
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"     "+s_b+"""Decimal"""+reset+"""     """+pi+""">>>"""+reset+"""   """+g+"""Hexadecimal"""+reset+"""    """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""     """+pi+""">>>"""+reset+"""    """+g,out_ans,pi+"""
  +------------------+-------------------+"""+reset)
	
	print(pi+"""
   +------------------+
   |"""+reset+"""  """+s_b+"""From Decimal To"""+reset+""" """+pi+"""|
   +------------------+-------------------+
   |"""+reset+"   "+s_b+"""1 """+y+"""->>"""+g+""" Binary"""+reset+"""   """+pi+"""|"""+reset+"""  """+s_b+"""2 """+y+"""->>"""+g+""" Octal"""+reset+"""      """+pi+"""|
   +------------------+-------------------+
   |"""+reset+"          "+s_b+"""3 """+y+"""->>"""+g+""" Hexadecimal"""+reset+"""           """+pi+"""|
   +------------------+-------------------+"""+reset)

	to_choice = int(input(y+"""
   ┌──["""+b+"""Enter the option"""+y+"""]"""+reset+"""
   """+y+"""└─ᐳ  """+s_b))
	print(reset)
	if to_choice <= 3 and to_choice != 0:
		num = input(y+"""
   ┌──["""+b+"""Enter the number to convert"""+y+"""]"""+reset+"""
   """+y+"""└─ᐳ  """+s_b)
		print(reset)
		if to_choice == 1:
			to_binary(num)
		elif to_choice == 2:
			to_octal(num)
		elif to_choice == 3:
			to_hexadecimal(num)
		else:
			print(s_b+"  ["+r+"Input-Error"+s_b+"]:"+reset+r+" Wrong Input !, try again"+reset)
	else:
		print(s_b+"  ["+r+"Input-Error"+s_b+"]:"+reset+r+" Wrong Input !, try again"+reset)
#decimal()
