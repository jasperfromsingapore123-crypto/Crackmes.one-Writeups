Challenge is sourced from:
https://crackmes.one/crackme/5db0ef9f33c5d46f00e2c729

Information is correct at the time of publishing 6 September 2026

We are given a password checker(as usual), and it seems we need to try to get the correct password.
Lets try opening it in a decompiler, and in my case, its Binary Ninja.

We are given this relatively short main(), and lets check it out

```text
004012a1    int32_t main(int32_t argc, char** argv, char** envp)

004012a9        void* fsbase
004012a9        int64_t rax = *(fsbase + 0x28)
004012c4        sub_401348("Gtu.}'uj{fq!p{$", 1)
004012d5        sub_401348("Lszl{{%", 0)
004012ed        void var_58
004012ed        __isoc99_scanf(format: "%64[^\n]", &var_58)
004012ed        
00401307        if (sub_4013e3(&var_58, "fhz4yhx|~g=5") != 0)
00401328            sub_401348("Zwvup(", 1)
00401307        else
00401315            sub_401348("Ftyynjy*", 1)
00401315        
0040133f        if (rax == *(fsbase + 0x28))
00401347            return 0
00401347        
00401341        __stack_chk_fail()
00401341        noreturn
```
var_58 is likely our input, because of "scanf", which is the standard input function in C.
We can then go ahead to rename var_58 as the input.

As we can see, var_58 is being passed as arguments for sub4013e3(). Hence, lets go reverse that.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We are led into sub_4013e3(). However, it just seems to be repeatedly calling sub_401175(), as seen in the while loop. Hence, lets go reverse sub_401175().

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```text
00401175    uint64_t sub_401175(int64_t arg1)

00401182        if (arg1 != 0)
00401188            data_404028 = arg1
0040118f            data_404010 = 0x7b1
0040118f        
004011a5        if (*data_404028 == 0)
004011a7            return 0
004011a7        
004011b9        int32_t rax_7 = data_404010 * 7
004011c2        uint32_t rax_10 = rax_7 s>> 0x1f u>> 0x10
004011ce        data_404010 = zx.d(rax_7.w + rax_10.w) - rax_10
004011d4        char* rax_12 = data_404028
004011df        data_404028 = &rax_12[1]
00401214        return zx.q(sx.d(*rax_12) - data_404010 s% 0xa)

```
arg1, in this case, whatever that has been passed into it, in other words:
The encoded string, "fhz4yhx|~g=5", is passed into sub_4013e3 as arg2, then sub_4013e3() passes it into sub_401175() as the argument.
Hence, lets go decipher what sub_401175() is trying to do.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Basically, what it does is that it defines a "key"(data_404010), and defining data_404028 as the encoded password string. 
Then, the value of rax_7 would be 7 times the value of key.

The following lines:
004011c2        uint32_t rax_10 = rax_7 s>> 0x1f u>> 0x10
004011ce        data_404010 = zx.d(rax_7.w + rax_10.w) - rax_10

Look very scary. However, what they do is as follows:

declare rax_10 and do a series of transformations to rax_7 and store that value in rax_10.
Yet, rax_7 is a int32 integer. When we take rax_7>>0x1f, we are left with 0, in other words rax_10 = 0.
Hence, data_4040101 = the lowest 16 bits of rax_7, in other words rax_7&0xffff

Lets move on to the next lines.

rax_12 points to the current character of data_404028. Then, data_404028 will be the next character.
Finally, we return the value of the rax_12 - data_4040101%10 (note that 0xa is hex for the decimal value 10)
WE ARE DONE IN UNDERSTANDING WHAT THIS FUNCTION IS ABOUT. WELL PLAYED.

However, you may notice the condition if(arg1 !=0).
This ensures that data_404028 is only initialised ONCE, and hence that explains why sub_4013e3() calls sub_401175() with the argument "0"
In other words, the second and above iterations of the function, sub_401175()  is called with the argument "0"
 
Since now we can understand the transformation, lets refer to solve.py


Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.

PS. if you have any questions about this challenge, please lemme know, this aint a simple one to digest especially if you have just started out!
