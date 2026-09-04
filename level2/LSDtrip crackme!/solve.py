import string #required library for us to loop thru all the alphabets,digits and punctuations
total = 945
length = 5
#a null byte's value = 10
#hence, the total value of the password is 945-5*10, because your null byte will be the last char of your input anyways, so its "5"
total -=5*10
length -=1

chars = string.ascii_letters + string.digits + string.punctuation # our possible values

for a in chars:
	for b in chars:
		for c in chars:
			for d in chars:
				value1 = ord(a)*1
				value2 = ord(b)*2
				value3 = ord(c)*3
				value4 = ord(d)*4
				if value1+value2+value3+value4 == total:
					print(f"The characters are: ",a,b,c,d) # this is a f string u can go search it up
					exit()
				else:
					continue



