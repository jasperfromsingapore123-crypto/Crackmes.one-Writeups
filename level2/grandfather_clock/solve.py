target = b"]\x10\x14LC\x10CNM\x14?GL4#&A[(R\x10\x11?S\x11LTR"

n = len(target)
password = [' ']*n
positions = list(range(n-1,0,-2))+list(range(0,n,2))
for idx,val in enumerate(positions):
	password[val] = chr((target[idx]+0x20)&0xff)

print("".join(password))
