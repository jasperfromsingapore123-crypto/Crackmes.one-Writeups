Challenge source is derived from:
https://crackmes.one/crackme/5e4ec05c33c5d4439bb2dbea

Information is correct at the time of publishing 5 September 2026

We are given a password checker program.

Let us first open up main() in our decompiler, and in my case, its Binary Ninja.
It looks pretty scary.. with the "std::string::operator[]"
However, what it basically represents is the "[]" operator.

```text

00401119        
00401119        if (strLength u<= 3)
004011c6            rax_18 = 0
00401119        else if (*std::string::operator[](this: &input, __pos: 0)
00401119                != *std::string::operator[](this: &falsePassword[abi:cxx11], __pos: 0))

```
The length of the input must >3(btw the u means unsigned comparison)

we are comparing our input to falsePassword. 

Hence, after much simplication, we can derive at this:
```text
correct_password[0] = falsePassword[0] //I will talk about how I derived falsePassword
correct_password[1] = falsePassword[5]
correct_password[2] = falsePassword[8]
correct_password[3] = falsePassword[9]

```

However, if we were to open up falsePassword, we will realise it is initialised with 0s. Hence, the best way to do it would be dynamic analysis, and for me its gdb(with gef)

In Binary Ninja, flasePassword is initialised at 0x602320. Lets go check it out.

We are given:
```text
gef➤  x/4gx 0x602320
0x602320 <_Z13falsePasswordB5cxx11>:	0x0000000000615020	0x0000000000000020
0x602330 <_Z13falsePasswordB5cxx11+16>:	0x0000000000000020	0x0000000000000000
gef➤ 
```
Now, lets check 0x615020.

gef➤  x/s 0x615020
0x615020:	"1d47faf54f84dc393a4a015a8f190e36"

So here we are, given the content of falsePassword.

However, if you were to input the password now, it will be REJECTED. Lets go see why.







--------------------------------------------------------------------------------------------------------------------------------------------


Lets check where "main" is called. Pressing "x" on binary ninja, I am led to another function:
_static_initialization_and_destruction()

lets now reverse this

```text
00401281    void _static_initialization_and_destruction() __noreturn

0040128d        int32_t var_3c = 2
004012a0        void dummy
004012a0        int32_t rax = main(argc: 2, argv: &dummy, envp: &dummy)
004012a8        int32_t var_1c = 5
004012af        int32_t var_20 = 6
004012b6        char i = 1
004012b6        
004012be        while (i != 0)
004012ce            for (int32_t j = 0; j u<= 0x174d; j += 1)
004012d3                var_1c += j
004012d6                var_20 ^= 5
004012d6            
004012ee            for (int32_t j_1 = 0x15d0; j_1 u<= 0x15d5; j_1 += 1)
004012f0                i = 0
004012f0        
004012fa        int32_t var_44 = 5
00401301        int32_t var_48 = 6
00401314        int32_t var_4c = 5
00401314        
0040131b        if (rax != 1)
00401322            exit(status: 0)
00401322            noreturn
00401322        
00401327        char var_a8
00401327        __builtin_memcpy(dest: &var_a8, 
00401327            src: "\x2f\x1d\x14\x14\x58\x08\x14\x19\x01\x1d\x1c\x59\x58\x2c\x10\x11\x0b\x58\x11\x"
00401327        "0b\x58\x0c\x10\x1d\x58\x17\x16\x14\x01\x58\x0e\x19\x14\x11\x1c\x58\x1e\x14\x19\x1f"
00401327        "56", 
00401327            count: 0x29)
0040143a        __alloc_traits<std::allocator<char> >::value_type rbx =
0040143a            *std::string::operator[](this: &input, __pos: 4)
0040144c        __alloc_traits<std::allocator<char> >::value_type rax_4 =
0040144c            *std::string::operator[](this: &input, __pos: 1)
00401451        __alloc_traits<std::allocator<char> >::value_type rax_6
00401451        
00401451        if (rbx == rax_4)
00401462            rax_6 = *std::string::operator[](this: &input, __pos: 5)
00401462        
00401467        char rax_7
00401467        
00401467        rax_7 = rbx != rax_4 || rax_6 != 0x40 ? 0 : 1
00401467        
00401477        if (rax_7 != 0)
00401480            char* i_2 = &var_a8
00401480            
004014a0            for (char* i_1 = i_2; i_1 != &i_2[0x29]; i_1 = &i_1[1])
004014c2                std::operator<<<std::char_traits<char> >(__out: &std::cout, 
004014c2                    __c: *i_1 ^ 0x78)
004014c2            
004014d8            std::ostream::operator<<(this: &std::cout, __pf)
004014d8        
004014e2        exit(status: 0)
004014e2        noreturn

```

Now, there is actually a lot of junk here. A lot of variables are declared, transformed, then not used. The only variables we want to look at are:
rbx register
rax_7
rax_4
rax_6

Now, rbs is the value of the 5th char in the password(as we can look at the "std::string::operator[]"), which tells us that it is "pos 4" of the password.. but remember its 0 indexed.

rax_4 is the value of our password, pos 1, in other words its the second char of our password.

rax_6, hence, is the 6th element in our password, as shown by 0x401462.




rax_7 is our deciding factor. Only when rbx = rax_4 AND rax_6 = '@' (its the ascii value of 0x40) than rax_7 will return 1.

Hence, we can build our solve script.



Refer to solve.py

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
