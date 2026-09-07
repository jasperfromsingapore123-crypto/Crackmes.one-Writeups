key = bytes.fromhex(
"00 05 54 10 36 f6 f1 03 17"
)
skey_original = 0x79629c8453602176
skey = skey_original.to_bytes(8,"little")

transformation_1 = []

for i in range(8):
	transformation_1.append(skey[i]^key[i+1])

print(bytes(transformation_1))



#Then, just run echo -n "<final output>" > secret_flag
#Flag: flag{this is your fight song}
