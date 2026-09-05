falsePassword = "1d47faf54f84dc393a4a015a8f190e36"
correct_password = ["A"]*6
correct_password[0] = falsePassword[0]
correct_password[1] = falsePassword[5]
correct_password[2] = falsePassword[8]
correct_password[3] = falsePassword[9]
correct_password[4] = correct_password[1]
correct_password[5] ='@'
print("".join(correct_password))
