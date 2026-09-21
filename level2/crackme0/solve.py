import string
def check(s):
	if len(s)%2 == 1:
		return False
	if len(s)<=7:
		return False
	var = 0
	sum = 0
	for idx, val in enumerate(s):
		if idx%2 == 0:
			var+=ord(val)&0xf

	for idx,val in enumerate(s):
		if idx%2 == 0:
			continue;
		if val>= 'a' and val<='f':
			value = ord(val)-ord('a')+10
			sum+=value
		elif val >= 'A' and val<='F':
			value = ord(val)-ord('A')+10
			sum+=value
		else: return False
	final = 0
	temp  = var+len(s)
	variable = len(s)+sum
	if var>= sum:
		final = temp%variable
	else:
		final = variable%temp
	if final == 0:
		return True
	else:
		return False


for a in string.ascii_letters:
	for b in "abcdefABCDEF":
		candidate = (a+b)*4 # i did this to narrow down the search range
		if check(candidate):
			print(f"Found: {candidate}")
