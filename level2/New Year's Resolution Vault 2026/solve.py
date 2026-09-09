resolution = input("[*] Input your NEW YEAR RESOLUTION YAEYYYY!!!!!!: ")
def rol64(value,amount):
	amount%=64
	return ((value<<amount)| (value>>(64-amount)))&0xffffffffffffffff

result = 0x7e9

for i in range(len(resolution)):
	result = rol64(result + ord(resolution[i])*(i+1),3)
	result^=0x20262026

print(result)

