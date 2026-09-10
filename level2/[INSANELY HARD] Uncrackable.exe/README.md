Challenge sourced from:
https://crackmes.one/crackme/6942f04b0992a052ab2223e6

Information is correct at the time of publishing.

Now, there are 2 ways to solve this, dynamic and static analysis. I personally think dynamic is somewhat easier, and I shall be going through that first.

First, lets open up our binary both in Binary Ninja and a debugger, and in my case, its x64dbg.

Lets immediately head to the main function and look for any signs of comparing our input to the target. Apparently, we see a memcmp, and lets set a breakpoint there for analysis.

<img src="../../images/Pasted image.png">

Now, we need to set a breakpoint. But where? Under Binary Ninja, memcmp is at 14000229e. 
At a typical executable, the preferred image base is 0x140000000. Hence, at x64dbg, we go to crackmes.one+229e (crackmes.one is the name of the chall file, it may differ)

Now, another problem arises. How long of a password do we even input, before we even reach memcmp? Well, the following lines tell us:

```text
14000229e                    rdx_19 = memcmp(rcx_23, rdx_18, var_68_1) == 0
```

Now, we are comparing rcx_23(our input) to rdx_18, which is the target.
Lets go backwards. 

```
140002263                int32_t* rdx_18 = &var_98
```

Then, whats the length of var_98?

```text
1400021f5                sub_140003280(&var_98, 0x16)
```
well, its 0x16(hex) long. 

Hence, we just input a 22 char password, the we can derive the password.

<img src="../../images/Pasted image (2).png">

I know, this is just one method and I promised 2. Hence, let me elaborate on how to analyse this statically.

Now, the decompiled code is just way to long for me to copy and paste here, so we will just be focusing on the important bits.

```text
140002206                if (i_6 != i_6 + 0x16)
140002206                {
14000225d                    do
14000225d                    {
140002214                        int64_t rcx_21 = var_80.q
140002218                        char r9_6 = *i_2 ^ 0x5a
140002218                        
14000221f                        if (rdi u>= rcx_21)
14000224e                            sub_140003bf0(&var_98, 1, zx.q(var_b8), r9_6)
14000221f                        else
14000221f                        {
140002229                            var_88_2.q = rdi + 1
14000222d                            int32_t* rax_23 = &var_98
14000222d                            
140002231                            if (rcx_21 u> 0xf)
140002231                                rax_23 = var_98.q
140002231                            
140002236                            *(rax_23 + rdi) = r9_6
14000223a                            *(rax_23 + rdi + 1) = 0
14000221f                        }
14000221f                        
140002253                        rdi = var_88_2.q
140002257                        i_2 += 1
14000225d                    } while (i_2 != i_6 + 0x16)
140002206                }
```

As prev. mentioned, var_98 is the target passcode. Hence, we just have to trace this logic in order to decrypt the bytes(found earlier in the decompiled code, not here).

r9_6 holds the value of *i_2^0x5a.

Then what is *i_2? 

Well, i_2 is a counter, and it increments. 

Next I want to talk about this chunk
```text
140001f20        int128_t* i_7 = sub_140006618(0x16)
140001f36        int128_t* i_6 = i_7
140001f39        sub_14001f1c0(i_7, &var_98, 0x16)
140001f41        int32_t var_88_2
140001f41        var_88_2.q = 0
140001f49        var_98.o = zx.o(0)
140001f52        var_98.b = 0
140001f5a        int32_t var_80
140001f5a        var_80.q = 0xf
140001f62        sub_140003280(&var_98, 0x1e)
```

i_6 has the same pointer value as i_7. Then, i7 is passed into sub_14001f1c0(), and copies 0x16 bytes into the memory pointed to by i_7.

And thanks to 
```
1400021fc                int128_t* i_2 = i_6
```
we can be certain taht *i_2 points to the target password.

Hence, we can perform the xor and get the correct password.

Refer to solve.py

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
