def qword_bytes(value): #this function is initialised so that we ensure each variable is precisely 8 bytes
	return (value&0xffffffffffffffff).to_bytes(8,"little")

var_90 = -0x7035c86e54ec9be8
var_88 = -0x58ebc2c8d1cfc015
text = -0x33749a2d00a2daa5
var_58 = -0x58ebc2c8d18a8d60

encoded_bytes = (
qword_bytes(var_90)+
qword_bytes(var_88)
)

key = (
qword_bytes(text)+
qword_bytes(var_58)
)
password = ""

for idx,val in enumerate(encoded_bytes):
	password+=chr(val^key[idx])
print(password)
