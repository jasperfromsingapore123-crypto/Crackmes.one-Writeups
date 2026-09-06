pw = bytes.fromhex(
"4e 49 1d 42 7c 41 7c 33 75 6a 6b 3c 7e 7f cb"
)

r14 = 0
r15 = 2
correct = ""
character = 0
while character!=10:
	character = ((pw[r14]^0x27)+r15)&0xff
	correct+=chr(character)
	r14 +=1
	r15+=2

print(correct)
