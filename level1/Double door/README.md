Lets open up this file in a decompiler, for me its Binary Ninja

Challenge sourced at:
https://crackmes.one/crackme/6a9281f948cda5a2aaa3dbf3

Information is accurate as per 4 September 2026

We see a variable named "var_58"
It is passed into check_password(), which suggests its the user input. We can thus rename var_58 as such. Anyways, lets go reverse engineer check_password()

We see this:

140001690    int64_t check_password(char* arg1)

1400016b9        void var_4c
1400016b9        char _Str2[0x38]
1400016b9        base64_decode("Y3JhY2ttZTIwMjQ=", &_Str2, &var_4c)
1400016b9        
1400016d0        if (strcmp(_Str1: arg1, &_Str2) == 0)
1400016d2            return 1
1400016d2        
1400016ef        if (strstr(_Str: arg1, _SubStr: "hack") == 0)
1400016f8            return 0
1400016f8        
1400016f1        return 1

We see this "Y3JhY2ttZTIwMjQ="
When base64 decoded, it forms "crackme2024". This is a password.

The second conditional checks if the word "hack" exists, If so, it passes the check.

We can conclude that the password is either:
crackme2024

OR

any string that contains hack

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
