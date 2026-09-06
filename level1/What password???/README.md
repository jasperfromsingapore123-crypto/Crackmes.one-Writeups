Challenge sourced at:
https://crackmes.one/crackme/6a83e2f205a9e80a90724421

Information is correct at the time of publishing.

We are given a password checker. Lets open our program in a decompiler, and in my case, its binary ninja.

```text
00401150    int32_t main(int32_t argc, char** argv, char** envp)

0040116d        syscall(sys_read {0}, fd: 0, buf: &input, count: 0x400)
0040116f        int64_t r14 = 0
00401175        int64_t r15 = 2
00401175        
00401193        while (true)
00401193            char r12_3 = ((&pw)[r14] ^ 0x27) + r15.b
00401193            
00401199            if (r12_3 != (&input)[r14])
004011c9                syscall(sys_write {1}, fd: 1, buf: &wrong_msg, count: 0x14)
004011d3                syscall(sys_exit {0x3c}, status: 0)
004011d3                noreturn
004011d3            
0040119f            if (r12_3 == 0xa)
0040119f                break
0040119f            
004011a7            r14 += 1
004011aa            r15 += 2
004011aa        
004011ee        syscall(sys_write {1}, fd: 1, buf: &right_msg, count: 0x12)
004011f8        syscall(sys_exit {0x3c}, status: 0)
004011f8        noreturn

```
What it basically does is taht it initialises r14 and r15 with values.
Then, when r12_3 is not equal to 10(its the decimal representation of 0xa), it will:
xor pw[r14] with 0x27, then add the value of r15, before &0xff the value(the .b in the decompiled code just means that)

Then we increment r14 and r15 with 1 and 2 respectively.

To get the value of pw, just click on it, and you will see the values.

```text
00404028  uint8_t pw = 0x4e

00404029                             49 1d 42 7c 41 7c 33 75 6a 6b 3c 7e 7f cb                                      I.B|A|3ujk<~..
```

Hence, we can write a solve script. Refer to solve.py



Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
