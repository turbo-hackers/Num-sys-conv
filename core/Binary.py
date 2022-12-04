#!/usr/bin/env python3
# coded by TURB0
# github https://github.com/turbo-hackers

# binary to decimal,octal,hexadecimal

# colors
r ='\033[91m' # red
g ='\033[92m' # green
b = '\033[94m' # blue
y = '\033[93m' # yellow
s_b ='\033[96m' # sky_blue
pi = '\033[35m' # pink
reset = '\033[0m' # reset
blink = "\033[5;92m" # blink


def binary():
	
	def to_decimal():
		l = len(num)
		t = -1
		point = False
		if '.' in num:
			point = True
			num_list = num.split(".")
			p_l = l-len(num_list[0])-1
			len_left = l-len(num_list[1])-1
		else:
			num_list = list(num)
			len_left = l
		if point != True:
			ans_list = []
			for i in num_list:
				len_left -= 1
				opt = int(i)*2**len_left
				ans_list.append(opt)
			ans = sum(ans_list)
		else:
			ans_list = []
			for i in num_list[0]:
				len_left -= 1
				opt = int(i)*2**len_left
				ans_list.append(opt)
			ans_list2 = []
			for j in num_list[1]:
				opt2 = int(j)*2**t
				t-=1
				ans_list2.append(opt2)
			ans = sum(ans_list) + sum(ans_list2)
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"      "+s_b+"""Binary"""+reset+"""     """+pi+""">>>"""+reset+"""     """+g+""" Decimal"""+reset+"""     """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""    """+pi+""">>>"""+reset+"""    """+g,ans,pi+"""
  +------------------+-------------------+"""+reset)
	
	def to_octal():
		def createMap(bin_oct_map):
			bin_oct_map["000"] = '0'
			bin_oct_map["001"] = '1'
			bin_oct_map["010"] = '2'
			bin_oct_map["011"] = '3'
			bin_oct_map["100"] = '4'
			bin_oct_map["101"] = '5'
			bin_oct_map["110"] = '6'
			bin_oct_map["111"] = '7'
		def BinToOct(num):
			l = len(num)
			t = -1
			if '.' in num:
				t = num.index('.')
				len_left = t
			else:
				len_left = l
			for i in range(1, (3 - len_left % 3) % 3 + 1):
				num = '0' + num
			# if decimal point exists
			if (t != -1):
				# length of string after '.'
				len_right = l - len_left - 1
				for i in range(1, (3 - len_right % 3) % 3 + 1):
					num = num + '0'
			bin_oct_map = {}
			createMap(bin_oct_map)
			i = 0
			octal = ""
			while (True) :
				octal += bin_oct_map[num[i:i + 3]]
				i += 3
				if (i == len(num)):
					break
				# if '.' is encountered add it to result
				if (num[i] == '.'):
					octal += '.'
					i += 1
			return octal
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"     "+s_b+"""Binary"""+reset+"""      """+pi+""">>>"""+reset+"""     """+g+""" Octal"""+reset+"""       """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""    """+pi+""">>>"""+reset+"""    """+g,BinToOct(num),pi+"""
  +------------------+-------------------+"""+reset)
	
	def to_hexadecimal():
		def createMap(bin_hex_map):
			bin_hex_map["0000"] = '0'
			bin_hex_map["0001"] = '1'
			bin_hex_map["0010"] = '2'
			bin_hex_map["0011"] = '3'
			bin_hex_map["0100"] = '4'
			bin_hex_map["0101"] = '5'
			bin_hex_map["0110"] = '6'
			bin_hex_map["0111"] = '7'
			bin_hex_map["1000"] = '8'
			bin_hex_map["1001"] = '9'
			bin_hex_map["1010"] = 'A'
			bin_hex_map["1011"] = 'B'
			bin_hex_map["1100"] = 'C'
			bin_hex_map["1101"] = 'D'
			bin_hex_map["1110"] = 'E'
			bin_hex_map["1111"] = 'F'
		def BinToHex(num):
			l = len(num)
			t = -1
			if '.' in num:
				t = num.index('.')
				len_left = t
			else:
				len_left = l
			for i in range(1, (4 - len_left % 4) % 4 + 1):
				num = '0' + num
			# if decimal point exists
			if (t != -1):
				# length of string after '.'
				len_right = l - len_left - 1
				for i in range(1, (4 - len_right % 4) % 4 + 1):
					num = num + '0'
			bin_hex_map = {}
			createMap(bin_hex_map)
			i = 0
			hexa = ""
			while (True) :
				hexa += bin_hex_map[num[i:i + 4]]
				i += 4
				if (i == len(num)):
					break
				# if '.' is encountered add it to result
				if (num[i] == '.'):
					hexa += '.'
					i += 1
			return hexa
		print("\n")
		print(pi+"""
               +------------+
               |"""+reset+"""   """+b+"""Answer"""+reset+"""   """+pi+"""|
  +------------+-----+------+------------+
  |"""+reset+"     "+s_b+"""Binary"""+reset+"""      """+pi+""">>>"""+reset+"""   """+g+""" Hexadecimal"""+reset+"""   """+pi+"""|
  +------------------+-------------------+"""+reset+"""
        """+s_b,num,reset+"""    """+pi+""">>>"""+reset+"""    """+g,BinToHex(num),pi+"""
  +------------------+-------------------+"""+reset)
	
	print(pi+"""
   +------------------+
   |"""+reset+"""  """+s_b+"""From Binary To"""+reset+"""  """+pi+"""|
   +------------------+-------------------+
   |"""+reset+"  "+s_b+"""1 """+y+"""->>"""+g+""" Decimal"""+reset+"""   """+pi+"""|"""+reset+"""  """+s_b+"""2 """+y+"""->>"""+g+""" Octal"""+reset+"""      """+pi+"""|
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
			to_decimal()
		elif to_choice == 2:
			to_octal()
		elif to_choice == 3:
			to_hexadecimal()
		else:
			print(s_b+"  ["+r+"Input-Error"+s_b+"]:"+reset+r+" Wrong Input !, try again"+reset)
	else:
		print(s_b+"  ["+r+"Input-Error"+s_b+"]:"+reset+r+" Wrong Input !, try again"+reset)
#binary()
