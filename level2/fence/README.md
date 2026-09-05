The challenge is sourced from:
https://crackmes.one/crackme/5ea7133233c5d47611746483

Information is correct at the time of publishing 5 September 2026

We are given a program that takes ONE argument, then transforms it before returning it.
Lets open it in a decompiler, and in my case its Binary Ninja.

We are greeted by a huge chunk of formidable code, with things like "std::allocator<char>" and "std::string::size_type"
However, it is not actually that hard. We can take them as their names, to understand them. 
After some thinking, I derived at this pseudocode

```text
password = input()
array_1 = ""
array_2 = ""
array_3 = ""
for i in range(0,len(password),3):
	array_1+=password[i]

for i in range(1,len(password),3):
	array_2+=password[i]

for i in range(2,len(password),3):
	array_3+=password[i]

temp = array_3+array_1
correct_password = temp + array_2
print(correct_password)
```
^ Higher level and more readable

What it does is that it takes every third item from the string, then adds it to another string
(in my case I like to call it an array)
Then, they put them together in the above showed format
(note its not array_1+array_2+array_3)

However, what the decompiler shows is a bit different:

(btw, I hope you can rename the variable names yourself, I am just explaining whats the argv)

```text
004012a4        ref var_68.32 = std::operator+<char>(&var_88, argv)
004012be        class std::string var_48
004012be        ref var_48._M_dataplus.32 = std::operator+<char>(&var_68, &var_a8)
004012e6        std::ostream::operator<<(this: std::operator<<(__os: &std::cout), 

```
Now, with proper renaming, var_88, var_68 and var_a8 can easily be understood. However, what is argv?

We have to realise that decompilers are not always accurate, and here, we can make it an educated guess, that argv is a misrepresentation of array_1, since the program has used array_3 and array_2. You can refer to the pseudocode I put above.

Hence, we can reverse this program, and derive the flag. Refer to solve.py


Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
