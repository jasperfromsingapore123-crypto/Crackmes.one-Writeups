target = "sCPZSUPgTG@G^C]"
final = "CrackmePassword"

password = ""

for i in range(len(target)):
        password+=chr(ord(target[i])^ord(final[i]))
print(password)
