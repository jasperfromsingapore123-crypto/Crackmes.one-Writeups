Challenge sourced from 
https://crackmes.one/crackme/60db74bb33c5d410b88430dc

Information is correct at the time of publishing, 14 September 2026.


We are given a password verifier. Lets analyse it in a decompiler, and in my case, its Binary Ninja.

We are given this main function

```text
004013db    int32_t main(int32_t argc, char** argv, char** envp)

004013ee        if (argc == 1)
004013ee        {
004013fa            _9ff8a42e_cbd2_481f_9c73_6880f720771f(*argv)
004013ff            return 1
004013ee        }
004013ee        
00401422        if ((zx.q(strlen(argv[1])) & 1) != 0)
00401422        {
0040142e            _a97962fc_d68f_47c5_9221_d17da57166a4(&_dbf69e5f_8300_41c9_8c80_02a819c56349)
00401433            return 1
00401422        }
00401422        
00401461        if (strcmp(&_867a0be1_691e_4546_9b6c_020df3bcdc93, 
00401461            _99adb5ad_c9d1_44ff_84ce_b52782ac7aeb(argv[1])) == 0)
00401461        {
00401483            _a97962fc_d68f_47c5_9221_d17da57166a4(&_a67bcbe1_4a3e_4c27_a894_ae121b083cac)
00401488            return 0
00401461        }
00401461        
0040146d        _a97962fc_d68f_47c5_9221_d17da57166a4(&_dbf69e5f_8300_41c9_8c80_02a819c56349)
00401472        return 1
```

This looks horrifying. However, we can take some time to analyse each one of then.

```text
004011a9    int64_t _9ff8a42e_cbd2_481f_9c73_6880f720771f(int64_t arg1)

004011dc        char* format = memset(malloc(bytes: 0x12), 0, 0x12)
004011ef        __builtin_strncpy(dest: format, src: "a\x7fmsqF,1\x7f,HrxmsJ", count: 0x10)
004011fd        *(format + 0x10) = 0x16
00401205        void* var_30 = nullptr
00401205        
00401243        while (*(var_30 + format) != 0)
00401243        {
0040120f            void* rax_1 = var_30
00401217            var_30 = rax_1 + 1
00401231            *(rax_1 + format) = *(format + rax_1) - 0xc
00401243        }
00401243        
00401258        printf(format, arg1)
0040126f        return free(mem: format)
```
Basically its printing a decrypted string. Not what we want to analyse.

However, this strcmp looks interesting:
```
00401461        if (strcmp(&_867a0be1_691e_4546_9b6c_020df3bcdc93, 
00401461            _99adb5ad_c9d1_44ff_84ce_b52782ac7aeb(argv[1])) == 0)
```

It seems taht _99adb5ad_c9d1_44ff_84ce_b52782ac7aeb() is the function verifying the input, and comparing it with 
&_867a0be1_691e_4546_9b6c_020df3bcdc93

By the way, for your reference, here is a main renamed function I created.

![Screenshot](images/Pasted%20image%20(3).png)

Anyways, lets go reverse the function we have identified.


```text
00401321    int64_t _99adb5ad_c9d1_44ff_84ce_b52782ac7aeb(char* arg1)

00401335        uint64_t rax_1 = strlen(arg1)
0040133e        void* i = nullptr
0040134e        void* var_30 = rax_1 - 1
00401352        char var_39 = 0xfe
00401379        int64_t result = memset(malloc(bytes: rax_1 + 1), 0, rax_1 + 1)
00401379        
004013cf        for (; i u< rax_1; i += 1)
004013cf        {
004013a2            *(i + result) = *(var_30 + arg1) - 0x20
004013a9            var_30 += sx.q(var_39)
004013a9            
004013b2            if (var_30 == -1)
004013b2            {
004013b4                var_30 += 1
004013bf                var_39 = (neg.d(zx.d(var_39))).b
004013b2            }
004013cf        }
004013cf        
004013da        return result

```

Now, we have a counter called i. Lets go analyse the loop.

rax_1 is the length of our input.


A char is 8 bits/1 byte. It is now given the value of 0xfe, which is 254 in decimal. However, thats not exactly the case due to the size of var_39. 

For an 8 bit signed integer, values 128 to 255 are treated as negative. Hence, the actual value of var_39 used is 254 - 256 which equals to negative 2.

Lets continue.

As we move on further, we see this:

```text
004013a2            *(i + result) = *(var_30 + arg1) - 0x20
```

This basically means, result[1] = input[rax_1-1]-0x20.
Then, var_30 is incremented by var_39.


This is where it gets somewhat interesting.

var_30 is initially defined as the length of the input - 1. On every iteration, 2 is deducted away. This kinda mangles up the input. But, in my solve script, I demonstrate how to reverse this.

Now, once var_30 = -1, var_39 becomes positive, and the value of 1 is added onto var_30. Now, we keep adding. You may think, how does this work? 

Well, it keeps deducting 2 from var_30, till it reaches -1. This is for odd indicies. Then it adds the value 1, and starts dealing with the even indicies.

Now lets write a solve script


Refer to solve.py

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
