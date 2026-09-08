Challenge is sourced from:
https://crackmes.one/crackme/6403ac2a33c5d447bc76179f

Information is correct at the time of publishing 8 September 2026

We are given a seriel checker. Lets open it up in Binary Ninja, or any decompiler of your choice. I think there is something new to learn in this crackme, especially for beginners.

Lets check out our main function first. Apparently, we have this sub_401255(), which is our password checker. Hence, lets go reverse that.

Now, once we are in sub_401255(), we see 2 functions.
```text
00401255    int64_t sub_401255(char* arg1)

00401283        if (strlen(arg1) != 0xd || arg1[3] != 0x2d)
00401285            return 0
00401285        
004012a0        int32_t rax_6 = sub_4011ee(arg1, 0, 3)
004012a0        
004012ac        if (rax_6 == 0xffffffff)
004012ae            return 0
004012ae        
004012de        int32_t var_c_1 = 4
004012de        
00401381        while (true)
00401381            if (var_c_1 s> 0xc)
00401387                return 1
00401387            
004012fb            int32_t rax_17 = sub_4011ee(arg1, var_c_1, 3)
004012fb            
00401307            if (rax_17 == 0xffffffff)
00401309                return 0
00401309            
00401370            if ((sub_4011c9(arg1[sx.q((var_c_1 - 4) s/ 3)]) ^ (rax_6 s% 3)) != rax_17 s% 9)
00401370                break
00401370            
00401379            var_c_1 += 3
00401379        
00401372        return 0
```

Lets go check out each of those new functions.

```text
004011ee    uint64_t sub_4011ee(void* arg1, int32_t arg2, int32_t arg3)

00401200        int32_t var_c = 0
0040120a        int32_t var_10 = arg2
0040120a        
0040124e        while (true)
0040124e            if (var_10 s>= arg3 + arg2)
00401250                return zx.q(var_c)
00401250            
00401224            int32_t rax_6 = sub_4011c9(*(arg1 + sx.q(var_10)))
00401224            
00401230            if (rax_6 == 0xffffffff)
00401230                break
00401230            
0040123c            var_c += rax_6
0040123f            var_10 += 1
0040123f        
00401232        return 0xffffffff
```

Now, lets first understand what this program is doing before going to sub_4011c9()

Basically, it initialises 2 new variables, var_c and var_10. var_c is defined with the value of 0, whereas var_10 will take the value of the arguments of the function.

Basically, what it does is that it will loop through the sequence, till the value of var_10 is equal to or greater than the values of arg2 and arg3 combined.
Then, the value of var_c is returned.

So, how do we derive at the final value of var_c?

Well, we derive another value through another function. Then that value is added onto var_c, before incrementing var_10 by one.
Hence, to put it in simple terms, var_c is just the sum of all the chars' ascii values from the index specified by arg2 to that specified by arg3.

Now, lets reverse sub_4011c9()

```text
004011c9    uint64_t sub_4011c9(char arg1) __pure

004011dc        if (arg1 s> 0x2f && arg1 s<= 0x39)
004011e9            return zx.q(sx.d(arg1) - 0x30)
004011e9        
004011de        return 0xffffffff
```

Now, this is actually where I said we could learn lots of new stuff. You see, this is actually a bit of "pattern recognition", when you see arg1 - 0x30, chances are actually (in this kind of scenario), we are getting the ascii value of a character.

The above conditional just checks whether the character is within a range.

Now, since we understand these 2 functions, lets go check out the other function we have yet to analyse.

Alright, this is our last function, sub_401255(). I have attached the code above ^^. Do check it out for reference. 

Here, there is first a conditional that checks the length of the input(must be 13 chars) and the 4th char( must be a dash ie. '-')

Next, we see the variable rax_6. Basically, it takes the total sum of the ascii values of the input, from index 0 to index 3. If the value of rax_6 = 0xffffffff it immediately means it FAILED.

Then we see a variable called var_c_1 being initialised with the value of 4.

Then, we move on to a while loop. 

We see rax_17 being initialised, with sub_4011ee() being called again, with the arguments: "arg1","var_c_1" and 3.

arg1 is our input

var_c_1 is the variable we mentioned above

and 3 is just 3

if rax_17 yields the value of 0xffffffff, once again, its an immediate FAIL.

Finally, we see this big chunk

```text
00401370            if ((sub_4011c9(arg1[sx.q((var_c_1 - 4) s/ 3)]) ^ (rax_6 s% 3)) != rax_17 s% 9)
00401370                break
```

We are given this large chunk, but let me help unpack it. 

As prev. mentioned, sub_4011c9 turns ascii chars into their respective values. Then, we take the char at [(var_c_1-4-4)//3], then xor it with rax_6%3. If that result is not equal to rax_17, aka the sum of all the variables mentioned in sub_4011ee(), it means we FAILED. NOOOOOO

Anyways, for easier reference, here is a pseudocode I wrote, I think this is actually a really challenging challenge. Time is really needed to digest this.

```text
def func1(input,ARG2,ARG3):     #ARG2 = 0 and ARG3 = 3
    var = 0
    arg2 = ARG2
    while arg2 <= ARG2+ARG3
        result = func2(input[arg2])
        if result == 0xffffffff:
            return 0xffffffff
        
        var+=result
        arg2+=1

    return var

def func2(arg1):
    if(arg1>0x2f and arg1<=0x39):
            return arg1-0x30
    return 0xffffffff

def final(input):
    if len(input)!=13 or input[3]!= '-':
        return 0
    var = func1(input,0,3)
    
    if var == 0xffffffff:
        return 0
    
    variable = 4
    
    while True:
            if(variable>12):
                return 1
            
            rax_16 = func1(input,variable,3)

            if(rax_16 == 0xffffffff):
                return 0
            
            if (func2(input[(variable-4)//3])^(var%3)) != rax_16 % 9:
                return 0
            variable+=3
    return 0

```
Now, since we have an idea what its doing, we can brute force the serial using python. It generates the first 5 serials, though you can easily change that (tho i admit the format of the output can be improved :(

Refer to solve.py



Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
