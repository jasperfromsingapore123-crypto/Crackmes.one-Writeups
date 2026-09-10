  GNU nano 8.7.1                                                                                                 README.md *                                                                                                         
Challenge sourced from:
https://crackmes.one/crackme/60a5301b33c5d4544d40d754

Information is correct at the time of publishing.

We are given a password checker. Lets open it up in a decompiler to take a look at it, and it my case, its Binary Ninja.

Wow: Its actually stripped. But its ok, we can find the entry point through _start.
There, it directs us to sub_401401.
Lets check that out.

In this function, its all startup code, before leading to the main() function. Hence, lets go check that out.

(btw another good way to reach the main() function would be to see the strings in the program)
```text
004010a0    int32_t sub_4010a0()

004010a9        __security_cookie
004010e3        int64_t var_5c
004010e3        __builtin_strncpy(dest: &var_5c, src: "\nInput key: ", count: 0xd)
004010fc        int128_t var_40
004010fc        __builtin_strncpy(dest: &var_40, src: "Wrong! Try again.\n", count: 0x13)
00401118        int32_t var_64
00401118        __builtin_strcpy(dest: &var_64, src: "Tl0dP0G")
00401128        int64_t var_4c
00401128        __builtin_strncpy(dest: &var_4c, src: "Nice job!\n", count: 0xb)
0040113c        srand(_Seed: _time64(_Time: nullptr).d)
00401150        int32_t eax_4
00401150        int32_t edx
00401150        edx:eax_4 = sx.q(rand())
004011a2        int32_t var_60
004011a2        char eax_6
004011a2        
004011a2        for (int32_t i = 0; i s< 0x64; i += 5)
004011a2        {
00401156            eax_6 = *(&var_64 + i)
00401156            
0040115c            if (eax_6 == 0)
0040115c                break
0040115c            
00401160            *(&var_64 + i) = eax_6 + 6
00401164            eax_6 = *(&var_64:1 + i)
00401164            
0040116a            if (eax_6 == 0)
0040116a                break
0040116a            
0040116e            *(&var_64:1 + i) = eax_6 + 6
00401172            eax_6 = *(&var_64:2 + i)
00401172            
00401178            if (eax_6 == 0)
00401178                break
00401178            
0040117c            *(&var_64:2 + i) = eax_6 + 6
00401180            eax_6 = *(&var_64:3 + i)
00401180            
00401186            if (eax_6 == 0)
00401186                break
00401186            
0040118a            *(&var_64:3 + i) = eax_6 + 6
0040118e            eax_6 = *(&var_60 + i)
0040118e            
00401194            if (eax_6 == 0)
00401194                break
00401194            
00401198            *(&var_60 + i) = eax_6 + 6
004011a2        }
004011a2        
004011f2        for (int32_t i_1 = 0; i_1 s< 0x64; i_1 += 5)
004011f2        {
004011a6            eax_6 = *(&var_64 + i_1)
004011a6            
004011ac            if (eax_6 == 0)
004011ac                break
004011ac            
004011b0            *(&var_64 + i_1) = eax_6 + 0xa
004011b4            eax_6 = *(&var_64:1 + i_1)
004011b4            
004011ba            if (eax_6 == 0)
004011ba                break
004011ba            
004011be            *(&var_64:1 + i_1) = eax_6 + 0xa
004011c2            eax_6 = *(&var_64:2 + i_1)
004011c2            
004011c8            if (eax_6 == 0)
004011c8                break
004011c8            
004011cc            *(&var_64:2 + i_1) = eax_6 + 0xa
004011d0            eax_6 = *(&var_64:3 + i_1)
004011d0            
004011d6            if (eax_6 == 0)
004011d6                break
004011d6            
004011da            *(&var_64:3 + i_1) = eax_6 + 0xa
004011de            eax_6 = *(&var_60 + i_1)
004011de            
004011e4            if (eax_6 == 0)
004011e4                break
004011e4            
004011e8            *(&var_60 + i_1) = eax_6 + 0xa
004011f2        }
004011f2        
004011f7        uint32_t var_68
004011f7        uint32_t edi_2
004011f7        
004011f7        if (mods.dp.d(edx:eax_4, 3) == 0)
004011f7        {
00401266            int16_t ecx_7 = var_64.w
00401275            int32_t edi_7 = (sx.d(ecx_7:1.b) * sx.d(var_60:2.b)) & 0x80000001
00401275            
0040127b            if (edi_7 s< 0)
00401281                edi_7 = ((edi_7 - 1) | 0xfffffffe) + 1
00401281            
0040129c            edi_2 = (edi_7 + sx.d(ecx_7.b)) * sx.d(var_60.b)
0040129c                + sx.d(var_64:3.b) * sx.d(var_64:2.b)
004011f7        }
004011f7        else if (mods.dp.d(edx:eax_4, 3) == 1)
004011fc        {
00401237            int16_t ecx_5 = var_60.w
00401247            int32_t esi_1 = sx.d(ecx_5:1.b)
0040125e            edi_2 = divs.dp.d(
0040125e                sx.q(sx.d(ecx_5.b) + sx.d(var_60:2.b) - sx.d(var_64.b) + esi_1), 
0040125e                sx.d(var_64:3.b)) * esi_1 + 0xbb
004011fc        }
004011fc        else if (mods.dp.d(edx:eax_4, 3) != 2)
00401231            edi_2 = var_68
00401201        else
00401201        {
00401203            int16_t edx_6 = var_60.w
00401229            edi_2 = divs.dp.d(sx.q((sx.d(var_64:2.b) + sx.d(edx_6:1.b)) * 0x26f6), 
00401229                sx.d(edx_6.b)) - sx.d(var_64:3.b) * 5 + 0x369
00401201        }
00401201        
004012a2        int64_t* var_74_2 = &var_5c
004012a8        sub_401020("%s")
004012b1        int32_t* var_7c = &var_68
004012b7        sub_401060("%d")
004012b7        
004012c3        while (var_68 != edi_2)
004012c3        {
004012c9            int128_t* var_74_3 = &var_40
004012cf            sub_401020("%s")
004012d8            int64_t* var_7c_1 = &var_5c
004012de            sub_401020("%s")
004012e7            int32_t* var_84_1 = &var_68
004012ed            sub_401060("%d")
004012c3        }
004012c3        
004012ff        int64_t* var_74_4 = &var_4c
00401305        sub_401020("%s")
0040130f        system(_Command: "pause")
00401322        CookieCheckFunction(var_68)
0040132a        return 0
```
Now, we have a number of strings, however all I wish to focus on ill be var_64, because it is the target string, or in other words what our key is based on.

Also, you realise that there is a rand() function. The number generated will decide WHICH of a pool of passwords will be correct.

Hence, let me give you a high level overivie of what the code is doing before we move on to the solve script.

First, there are 2 for loops. They keep looping, until a null byte is detected. 
The first loop increments each character's ascii value by 6, whereas the second loop increments each character's ascii value by 10.

Finally, a variable is calculated( specifically, edi_7). 

Finally, using our created variable, as well as SPECIFIED chars in the target string, we derive at THREE different passwords.



Refer to **solve.cpp** for the solve script

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
