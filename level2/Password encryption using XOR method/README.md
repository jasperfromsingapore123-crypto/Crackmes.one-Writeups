Challenge sourced from:
https://crackmes.one/crackme/68407be02b84be7ea77435d6

Information is correct at the time of publishing 9 September 2026

Now, we are given a password/serial checker. Lets open it up in our decompiler, and in my case, Binary Ninja. 

Here, we see a main() function. There are a bunch of functions responsible for io, but we will be ignoring them because they dont affect our password. Hence, the function to reverse here, would be sub_1400012a0()

Lets open it up!

```text
1400012a0    int128_t* sub_1400012a0(int128_t* arg1, int64_t* arg2, int64_t* arg3)

1400012b6        int32_t i_1 = 0
1400012b8        int128_t* var_30 = arg1
1400012c3        __builtin_memset(dest: arg1, ch: 0, count: 0x20)
1400012d9        int64_t* r12 = arg2
1400012d9        
1400012dc        if (arg2[3] u> 0xf)
1400012de            r12 = *arg2
1400012de        
1400012e1        int64_t r14 = arg2[2]
1400012e5        int64_t rsi = 0x7fffffffffffffff
1400012e5        
1400012f2        if (r14 u> 0x7fffffffffffffff)
14000140c            sub_1400011b0()
14000140c            noreturn
14000140c        
1400012fc        if (r14 u> 0xf)
14000131a            int64_t rax_2 = r14 | 0xf
140001321            void* const rax_6
140001321            uint64_t rax_3
140001321            
140001321            if (rax_2 u<= 0x7fffffffffffffff)
140001354                rsi = rax_2
140001354                
14000135a                if (rax_2 u< 0x16)
14000135a                    rsi = 0x16
14000135a                
140001365                if (rsi != -1)
140001373                    if (rsi + 1 u>= 0x1000)
140001375                        rax_3 = rsi + 0x28
140001375                        
14000137c                        if (rax_3 u> rsi + 1)
14000137c                            goto label_140001334
14000137c                        
140001412                        sub_140001110()
140001412                        noreturn
140001412                    
14000138b                    rax_6 = sub_140002000(rsi + 1)
140001365                else
140001367                    rax_6 = nullptr
140001321            else
14000132d                rax_3 = -0x7fffffffffffffd9
140001334            label_140001334:
140001334                int64_t rax_4 = sub_140002000(rax_3)
140001334                
14000133f                if (rax_4 == 0)
140001384                    _invalid_parameter_noinfo_noreturn()
140001384                    noreturn
140001384                
140001345                rax_6 = (rax_4 + 0x27) & 0xffffffffffffffe0
140001349                *(rax_6 - 8) = rax_4
140001394            *arg1 = rax_6
14000139a            arg1[1].q = r14
1400013a1            *(arg1 + 0x18) = rsi
1400013a5            memcpy(dest: rax_6, src: r12, count: r14.d + 1)
1400012fc        else
1400012fe            arg1[1].q = r14
140001302            *(arg1 + 0x18) = 0xf
14000130f            *arg1 = *r12
14000130f        
1400013ae        if (arg2[2] u> 0)
1400013b0            int64_t r9_1 = 0
1400013b3            int64_t i = 0
1400013b3            
1400013f0            do
1400013bb                int128_t* rax_7 = arg1
1400013bb                
1400013be                if (*(arg1 + 0x18) u> 0xf)
1400013c0                    rax_7 = *arg1
1400013c0                
1400013c8                char* r8_1 = rax_7 + r9_1
1400013cc                int64_t* rcx_4 = arg3
1400013cc                
1400013cf                if (arg3[3] u> 0xf)
1400013d1                    rcx_4 = *arg3
1400013d1                
1400013d9                char* rdx_2 = modu.dp.q(0:i, arg3[2])
1400013dd                i_1 += 1
1400013df                r9_1 += 1
1400013e2                i = sx.q(i_1)
1400013e9                *r8_1 ^= *(rdx_2 + rcx_4)
1400013f0            while (i u< arg2[2])
1400013f0        
14000140b        return arg1
```

This seems to be a huge chunk. However, all the password transformation logic occurs in the lower parts. Anyways, I will guide you throw in which what it means.

I will start from 1400013ae
Now, we have 2 variables defined as value 0, r9_1 and i. We can take them as counters.
Next, from the end of the while loop, we see this:
while(i u<arg2[2]).

I think this is a major learning point. arg2[2] means the LENGTH OF THE STRING. I know this is counter intinuitive, but there are the following proof:

1.

1400013a5            memcpy(dest: rax_6, src: r12, count: r14.d + 1)

The third argument of this is always the number of bytes to copy. Then, what value is passed into r14?

Well, its arg[2] !

2.

1400012dc        if (arg2[3] u> 0xf)
1400012de            r12 = *arg2

This matches MSVC std::string small-string optimization, where a capacity greater than 15 means the characters are stored on the heap. I mean.. the reason above may be easier for you to understand :(


To move on, I have renamed the variables so it will be easier to follow, i mean the variable names its using is kinda making me insane.

```text
1400013ae        if (target[2] u> 0)
1400013b0            int64_t counter1 = 0
1400013b3            int64_t counter2 = 0
1400013b3            
1400013f0            do  // suspected transformation logic, TO DO: REVERSE
1400013bb                int128_t* output_2 = output
1400013bb                
1400013be                if (*(output + 0x18) u> 0xf)
1400013c0                    output_2 = *output
1400013c0                
1400013c8                char* variable = output_2 + counter1
1400013cc                int64_t* input_1 = input
1400013cc                
1400013cf                if (input[3] u> 0xf)
1400013d1                    input_1 = *input
1400013d1                
1400013d9                char* variable2 = modu.dp.q(0:counter2, input[2])
1400013dd                counter3 += 1
1400013df                counter1 += 1
1400013e2                counter2 = sx.q(counter3)
1400013e9                *variable ^= *(variable2 + input_1)
1400013f0            while (counter2 u< target[2])
```

I simply renamed the variables, no logic was changed.

Now, as we can see, we have the following new vars I dont remember mentioning in this writeup:
```text
output
output_2
variable
variable_2
counter1
counter2
input
input_1
```

Now, I do remember talking about memcpy. HENCE, now I shall talk about the variable called "output"

The function first creates output as a copy of the target. For strings longer than 15 characters, this is done through the memcpy branch. In our case, the target is exactly 15 characters long, so MSVC's small-string storage is used and *arg1 = *r12 performs the copy instead.

Then, output_2 is basically a pointer to the actual character buffer used by output.

variable is initialised with the address of output_2[counter1]
Why? You may ask.

1. The reason why its variable[i] is because it is initialised as a char* not just as a normal char. 
More precisely: variable[i] is exactly the same as:
*(variable + i)

2. The same goes for output_2+counter1. output_2 is the POSITION in which output exists. Hence, when we add counter1 to it, we are told to go to the position specified, which in this case is exactly output_2[counter1] 

I think these are just the confusing things in the program, the rest can be illustrated in the solve script. 

I think this is just about it for this program. BUT, thats not the end! Lets go back to the main function. 

Check this out:

```text
1400014f9        int128_t* buffer1_1 = sub_1400012a0(&var_78, &var_58, &var_38)
1400014fe        int128_t* buffer1 = buffer1_1
1400014fe        
140001506        if (*(buffer1_1 + 0x18) u> 0xf)
140001508            buffer1 = *buffer1_1
140001508        
14000150b        uint64_t count = buffer1_1[1].q
140001513        bool rbx
140001513        
140001513        if (count == 0xf)
140001527            rbx = memcmp(buffer1, buffer2: "CrackmePassword", count) == 0
```

The result of the function is stored into buffer1_1.
Then, the same result is copied into buffer1.

Then, we compare buffer1 and the target: CrackmePassword. If they are the same, 0 is returned. 0 just means success and 1 means failure.


With that out of the way, I think we can write a solve script.

Refer to solve.py


Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
