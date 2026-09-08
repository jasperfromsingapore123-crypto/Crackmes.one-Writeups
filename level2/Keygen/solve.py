from itertools import product

#password = ['A']*13
#password[3] = '-'

def add_sums(ch):
	if ord(ch)>=ord('0') and ord(ch)<=ord('9'):
		return ord(ch) - ord('0')
	else:
		return 0xffffffff
def func1(input,start,end):
	var = 0
	arg2 = start
	while arg2<start+end:
		result = add_sums(input[arg2])
		if result == 0xffffffff:
			return 0xffffffff
		arg2+=1
		var+=result
	return var

def final(input):
	if len(input)!=13 or input[3]!='-':
		return False
	var = func1(input,0,3)

	if var == 0xffffffff:
		return False
	variable = 4

	while True:
		if (variable>12):
			return True
		rax_16 = func1(input,variable,3)

		if rax_16 == 0xffffffff:
			return False

		if add_sums(input[(variable-3)//3])^(var%3)!=rax_16%9:
			return False
		variable+=3
	return 0

solved = 0
passwords = []
for digits in product("0123456789", repeat = 12):
	s = ''.join(digits[:3])+ '-' + ''.join(digits[3:])
	if final(s):
		print(f"Valid Key found!")
		passwords.append(s)
		solved+=1
		if solved == 5:
			print(passwords)
			exit()
	else:
		print("Tried key but failed")
