Challenge sourced from:
https://crackmes.one/crackme/66ccb430b899a3b9dd02b07a

Information is accurate at the point of publishing 6 September 2026

We are given a password checker. Lets pop it into our decompiler, and in my case its Binary Ninja

We will be needing the following strings, as they are the strings that form our password.

The program initialises the following strings.
```text
1400012d2        var_90 = -0x7035c86e54ec9be8
1400012e8        int64_t var_88 = -0x58ebc2c8d1cfc015
1400012f4        text = -0x33749a2d00a2daa5
140001300        int64_t var_58 = -0x58ebc2c8d18a8d60

```

It appears to us that var_88 and var_58 is NOT used in the program. 
Before anything, note that the strings are defined as 8 bytes integers.

Now, later, we see:

```text
140001304        zmm0_2.o = var_90.o
140001309        zmm0_2.o ^= text.o
```
.o means that zmm0_2 is an octoword.
Since var_90 is an 8 byte integer, and just right after it in the computer's memory, uts var_88,hence zmm0_2 is basically var_90 and var_88
Same goes for text.o, because the computer is treating it as an octoword.

Hence, we can build our solve script.
Refer to solve.py


Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
