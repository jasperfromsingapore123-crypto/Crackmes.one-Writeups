transformed = "fhz4yhx|~g=5"
key = 0x7b1
result = ""
for c in transformed:
	temp = key*7
	trans_temp = temp>>0x1f>>0x10
	key = temp&0xffff
	result+= chr(ord(c)-key%10)
print(result)
