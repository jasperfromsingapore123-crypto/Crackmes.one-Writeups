target = "arln_pra_dfgafcchsrb_l{ieeye_ea}"
length = len(target)
print(length)
array_1_length = 11
array_2_length = 11
array_3_length = 10

#The target is basically array_3+array_1+array_2
array_1 = ""
array_2 = ""
array_3 = ""
for i in range(array_3_length):
	array_3+=target[i]
for i in range(array_1_length):
	array_1+=target[array_3_length+i]
for i in range(array_2_length):
	array_2 += target[array_3_length+array_1_length+i]
correct_flag = ""
for i in range(length):
	if i%3 == 0:
		correct_flag+=array_1[i//3]
	elif i%3 == 1:
		correct_flag+=array_2[i//3]
	elif i%3 == 2:
		correct_flag+=array_3[i//3]
print(correct_flag)
