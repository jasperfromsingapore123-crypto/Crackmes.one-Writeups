Challenge sourced from:
https://crackmes.one/crackme/6a59546f055757d3df60fd53

Information is correct at the time of publishing

We are given a password checker. This is kinda quite advanced, especially for a beginner. However, with a bit of time, we can solve this.

Lets open it in our decompiler, and in my case, its Binary Ninja. 

```text
00401199    int32_t main(int32_t argc, char** argv, char** envp)

004011b8        char var_c8[0x20]
004011b8        memset(&var_c8, 0, 0x20)
004011c7        puts(str: &data_402008)
004011d6        puts(str: &data_402070)
004011e5        puts(str: &data_402098)
004011f9        printf(format: "Speak the secret: ")
0040121c        char buf[0x87]
0040121c        
0040121c        if (fgets(&buf, n: 0x80, fp: stdin) == 0)
0040121e            return 1
0040121e        
00401232        uint64_t rax_3 = strlen(&buf)
00401232        
00401254        if (rax_3 != 0 && buf[rax_3 - 1] == 0xa)
0040125e            buf[rax_3 - 1] = 0
0040125e        
0040127e        if (strlen(&buf) != 0x11)
0040127e        {
0040128a            puts(str: "\nAccess denied. The House does not recognize this signature.")
0040128f            return 1
0040127e        }
0040127e        
00401299        int32_t var_c_1 = 0
00401299        
0040139b        while (true)
0040139b        {
0040139b            if (var_c_1 u> 0x10)
0040139b            {
004013ab                puts(str: "\nAccess granted. You may enter.")
004013b0                return 0
0040139b            }
0040139b            
004012aa            char rax_12 = buf[sx.q(var_c_1)]
004012dd            char var_ef[0x6]
004012dd            
004012dd            for (int32_t i = 0; i s<= 5; i += 1)
004012ce                var_ef[sx.q(i)] = i.b + rax_12
004012ce            
004012df            char var_e9_1 = 0
004012fc            char var_e8[0x20]
004012fc            SHA256(&var_ef, 6, &var_e8)
004012fc            
0040133a            for (int32_t i_1 = 0; i_1 s<= 0x1f; i_1 += 1)
0040132b                var_c8[sx.q(i_1)] ^= var_e8[sx.q(i_1)]
0040132b            
0040136c            if (memcmp(&var_c8, (sx.q(var_c_1) << 5) + &data_404060, 0x20) != 0)
0040136c                break
0040136c            
00401391            var_c_1 += 1
0040139b        }
0040139b        
00401385        printf(format: "\nInvalid sequence at node %d. The mechanism rejects you.\n", 
00401385            zx.q(var_c_1 + 1))
0040138a        return 1
```

Now, I have attached the main() function. Let me give you an overview of it.

It expects your input to be 17 chars. Else, it throws an error.

Next, lets analyse the while loop. 

Basically, what it does is that it initialises a buffer. Then, it is thrown into a for loop. 

An array is created, and the value of input[i]+i is given to the value stored at each index. 
For example, at position 5 of the array, the value would be var+5, with var being the value of input[var_c_1]

Then, we sha256 encrypt the array, and store it into another array called var_e8.

Finally, we go into a loop and xor each value of the current array(which in other words is var_c8), with the previous array's value(var_e8).


Now, that we can understand what the code is doing, lets write a solve script

Refer to solve.py

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
