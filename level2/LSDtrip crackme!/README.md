Decompiled using Binary Ninja.

Challenge can be found at:
https://crackmes.one/crackme/673df8399b533b4c22bd2f1b
Information is accurate as per 4 September 2026

Alright.. lets open up our file in a decompiler. For me, the main() function is sub_401000()

We are given:

00401000    void sub_401000() __noreturn

00401010        printf(_Format: "\n     "LSDtrip"" crackme by Alon Alush, alonalush5@gmail.com       "
00401010        "\n PASSWORD >>> ")
0040101e        char* eax = malloc(_Size: 0x14)
0040103a        fgets(_Buffer: eax, _MaxCount: 0x14, _Stream: _iob)
00401047        int32_t var_c = 0
0040104f        int32_t var_10 = 0
0040104f        
00401060        while (sx.d(eax[var_10]) != 0)
0040108f            var_c += sx.d(eax[var_10]) * (var_10 + 1)
00401071            var_10 += 1
00401071        
004010b2        if (strlen(_Str: eax) != 5 || var_c != 0x3b1)
004010d1            printf(_Format: "\nWrong! I think you're on LSD?", var_10, var_c, eax)
004010b2        else
004010be            printf(_Format: "\n [+] Good job! You sober! \n", var_10, var_c, eax)
004010be        
004010d9        _getch()
004010e4        exit(_Except: 0)
004010e4        noreturn

Ok. So the way we understand this is:

We are given 2 integers, var_c and var_10.

var_10 is a counter, because it increments every time in the while loop, and the while loop ends when you reach the end of the input(ie. reaches a null byte)
var_c like a "summer", because it just adds up the numbers every time through the loop.

Exactly how it works:

#python pseudocode

ord(password[i])*counter 

Note: in this case its var_10.

------------------------------------------------------------

The length of the input must be 5, but we need to realise there is a null byte when we press enter. Hence, the actual password is just 4 chars.

The total sum of the input, ie we ord() each char, must be 945. But once again, we must take into acc the null byte.



Now, lets create a solve script. Refer to solve.py

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
