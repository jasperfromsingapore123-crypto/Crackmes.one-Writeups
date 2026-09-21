Challenge sourced from:
https://crackmes.one/crackme/65446e720f4238b24302b41c

Information is correct at the time of publishing

We are given a password checker crackme. Lets reverse it by opening it in our decompiler.

```text
140005fc0    int64_t main()

140005fd5        void var_6c
140005fd5        int512_t entry_zmm1
140005fd5        int512_t zmm1 = b(&var_6c, __main(), entry_zmm1)
140005fdd        int32_t rax
140005fdd        int64_t rdx_1
140005fdd        rax, rdx_1 = a(&var_6c)
140005fe9        char const* const rcx_4
140005fe9        
140005fe9        if (rax s<= 7 || (rax.b & 1) != 0)
14000600a            rcx_4 = "Wrong"
140005fe9        else if (c(&var_6c) == 0)
14000600a            rcx_4 = "Wrong"
140005ff5        else
140005ff5        {
140005ffa            int32_t rax_2
140005ffa            rax_2, rdx_1 = e(&var_6c)
140005fff            rcx_4 = "Correct"
140005fff            
140006008            if (rax_2 == 0)
14000600a                rcx_4 = "Wrong"
140005ff5        }
140005ff5        
140006011        printf(rcx_4, rdx_1, zmm1)
140006020        return 0
```
Now, we are given a main() function, and lets analyse each of the associated functions in it.

We see function a(). 

```text
140001447    uint64_t a(char* arg1)

140001454        return strlen(_Str: arg1)

```
function a() just returns the length of your input, then it is compared. If the length is less than or equal to 7, immediately it gets rejected. rax&1 just looks at whether its odd or even, and in this case, it expects its length to be even


Apparently, c() is the function changing rcx_4, which is the output message. 

```text
140001476    int64_t c(char* arg1)

140001487        int32_t rax
140001487        
140001487        do
140001487        {
140001476            rax.b = *arg1
140001476            
14000147a            if (rax.b == 0)
14000148d                return 1
14000148d            
14000147f            arg1 = &arg1[1]
140001482            rax = (rax & 0xffffffdf) - 0x41
140001487        } while (rax.b u<= 0x19)
140001489        return 0
```

c() just ensures that you are inputting printable ascii values. 

Now, lets continue analysing the functions.

We are now at function e(). Lets analyse that

```text
1400014b7    int64_t e(char* arg1)

1400014bd        int32_t rsi = 0
1400014c7        void var_4a
1400014c7        int32_t rax = d(arg1, &var_4a)
1400014cc        char* rdx_1 = arg1
1400014cc        
1400014cf        while (true)
1400014cf        {
1400014cf            rax.b = *rdx_1
1400014d1            rdx_1 = &rdx_1[2]
1400014d1            
1400014d7            if (rax.b == 0)
1400014d7                break
1400014d7            
1400014d9            rax &= 0xf
1400014dc            rsi += rax
1400014cf        }
1400014cf        
1400014e0        char* rdx_2 = &var_4a
1400014e3        int32_t rbx = 0
1400014e3        
1400014e5        while (true)
1400014e5        {
1400014e5            rax.b = *rdx_2
1400014e5            
1400014e9            if (rax.b == 0)
1400014e9                break
1400014e9            
1400014f3            char rax_1
1400014f3            
1400014f3            if (rax.b - 0x61 u> 5)
1400014f3            {
140001502                if (rax.b - 0x41 u> 5)
140001539                    return 0
140001539                
140001504                rax_1 = rax.b - 0x37
1400014f3            }
1400014f3            else
1400014f5                rax_1 = rax.b - 0x57
1400014f5            
140001507            rax = sx.d(rax_1)
14000150a            rdx_2 = &rdx_2[1]
14000150d            rbx += rax
1400014e5        }
1400014e5        
140001511        int32_t rax_2 = a(arg1)
140001518        int32_t r8_3 = rsi + rax_2
14000151c        int32_t rcx_1 = rax_2 + rbx
140001520        int32_t rdx_4
140001520        
140001520        if (rsi s>= rbx)
14000152e            rdx_4 = mods.dp.d(sx.q(r8_3), rcx_1)
140001520        else
140001525            rdx_4 = mods.dp.d(sx.q(rcx_1), r8_3)
140001525        
140001530        int64_t result = 0
140001534        result.b = rdx_4 == 0
140001541        return result
```

We have another function, d(). 
Lets go analyse that first, before we come straight back into e()

```text

140001493    int64_t d(char* arg1, char* arg2)

140001493        int64_t result = 0
140001493        
140001495        while (true)
140001495        {
140001495            char r8_1 = arg1[result]
140001495            
1400014a0            if (r8_1 == 0)
1400014a0                break
1400014a0            
1400014a6            if (((result + 1).b & 1) == 0)
1400014a6            {
1400014a8                *arg2 = r8_1
1400014ab                arg2 = &arg2[1]
1400014a6            }
1400014a6            
1400014ae            result += 1
140001495        }
140001495        
1400014b3        *arg2 = 0
1400014b6        return result

```

Basically, what this does is to extract every ODD indexed character, then store it in another array. There is another variable called result, which is returned. However, result basically just takes the value of the length of the input

Now lets go back to function e().

Now, let me explain the first while(True) loop. Basically, it goes through every second char in our input array, then adding its ascii value into a variable.

The second while(True) loop will take quite a bit of explanation. 

It checks every single one of your input. 

If that character's ascii value minus the ascii value of 'a' is greater than 5, it passes the first round of check and we continue. Else, it will lead to the following case, which I have **boldened the text**

However, if the char - 'A' (once again ascii values) is greater or equal to 5, it leads to rejection.

Yet, if it passess that, we will store the value of that character - 0x37, which can be represented as character - 'a' + 10, because 'a' = 0x37 + 0x10. By the way, we are still referring to ascii values.

** As mentioned, here is what happens if it fails the check mentioned above. We will basically take the value of the character - 'a' - 10**



Finally, that value will be added onto another variable, before it goes into a final check. 

Finally, we compare all the variables we have created. If it passes the check, then we solve the crackme.

I have attached a Pseudocode file for reference.

Refer to solve.py

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
