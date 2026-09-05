Challenge sourced from 
https://crackmes.one/crackme/5f181ff233c5d42a7c667a95

Information is correct at the time of publishing 5 September 2026

Let us first open our program in our decompiler, and in my case, its Binary Ninja. I have attached the validate_serial() function right here.

```text
004011a9    int64_t validate_serial(char* arg1, int16_t arg2 @ x87control)

00401205        if (*arg1 s<= 0x2f || *arg1 s> 0x7a || arg1[1] s<= 0x2f || arg1[1] s> 0x7a
00401205                || arg1[2] s<= 0x2f || arg1[2] s> 0x7a)
0040120c            invalid_serial()
0040120c            noreturn
0040120c        
00401221        if (strlen(arg1) != 0x10)
00401228            invalid_serial()
00401228            noreturn
00401228        
00401245        float var_10 = fconvert.s(float.t(sx.w(*arg1)) / fconvert.t(122.0))
00401264        float var_14 = fconvert.s(float.t(sx.w(arg1[1])) / fconvert.t(122.0))
00401274        int16_t var_38_2 = sx.w(arg1[2])
00401283        float var_18 = fconvert.s(float.t(var_38_2) / fconvert.t(122.0))
00401299        char var_28[0x10]
00401299        memcpy(&var_28, arg1, 3)
00401299        
00401325        for (int32_t i = 3; i s<= 0xf; i += 1)
004012aa            long double x87_r7_7 = float.t(i) * fconvert.t(var_18)
004012af            int16_t x87status_1
004012af            int16_t temp0_1
004012af            temp0_1, x87status_1 = __fnstcw_memmem16(arg2)
004012b2            int16_t rax_31 = temp0_1
004012b6            rax_31:1.b |= 0xc
004012bd            int16_t x87control
004012bd            int16_t x87status_2
004012bd            x87control, x87status_2 = __fldcw_memmem16(rax_31)
004012c0            var_38_2.d = int.d(x87_r7_7 + x87_r7_7)
004012c3            int16_t x87control_1
004012c3            int16_t x87status_3
004012c3            x87control_1, x87status_3 = __fldcw_memmem16(temp0_1)
004012c6            int32_t rcx_1 = var_38_2.d
004012cc            long double x87_r7_10 = float.t(i) * fconvert.t(var_14)
004012d1            int16_t x87control_2
004012d1            int16_t x87status_4
004012d1            x87control_2, x87status_4 = __fldcw_memmem16(rax_31)
004012d4            var_38_2.d = int.d(x87_r7_10 + x87_r7_10)
004012d7            int16_t x87control_3
004012d7            int16_t x87status_5
004012d7            x87control_3, x87status_5 = __fldcw_memmem16(temp0_1)
004012da            int32_t rdx_1 = var_38_2.d
004012e0            long double x87_r7_13 = float.t(i) * fconvert.t(var_10)
004012e5            int16_t x87control_4
004012e5            int16_t x87status_6
004012e5            x87control_4, x87status_6 = __fldcw_memmem16(rax_31)
004012e8            var_38_2.d = int.d(x87_r7_13 + x87_r7_13)
004012eb            int16_t x87status_7
004012eb            arg2, x87status_7 = __fldcw_memmem16(temp0_1)
00401319            var_28[sx.q(i)] = (*"npUd4pN7nzmUpJwGl6QCRAlS8c04AqUC4trOWcYquvUhzmy82VAQ1TPizhUa7ol8fMG7X9WRijs82ZD7qgqvMf98PAAPJ69q01QkIa3ylGfirWgHHhBvkbG0thB947CaTy5T9UFAx9yMaODNF1vbVvN8sh9BV8XmXjUciqhgJCv6naxePgw2nn3Dh7w5SVQyOfnLopTCzZqi1QAzRslzMhLqZPfgZtqqNIPWwxDJdxMkP97pS4GsDNwp2SjIOeuyk87ps0ewWI9CKjV9aiFlgdyFta9jjMD7avxhswFC6p1EJ4ssdLB3OLuOPOxzoHcuAhkv1zD0auvTNZMJDBGGPMRnACkhczqNA3BkAWmXiZty9yV3GuoHzkEiCr8HiOMR7nLkLUTyiPw96Rfm07h066ybDvPEXo6ot5druBE4t8o9haHeTyA4NlvVpp7bbmGNHc3Y5oxmYqG1pNYF5EpDLqfihB6BXGEeU5fRjA0aOojnLePPpcyuio4mehaHZAUF
00401319                …")[((sx.q(rdx_1) + (sx.q(rcx_1) << 5)) << 5) + sx.q(var_38_2.d)]
00401319        
00401340        return memcmp(&var_28, arg1, 0x10)
```

I think that there are a lot of things to learn here.

There are very weird names, like x87_r7_7.... x87???
However, do not worry. They are just literally just variable names, you can rename them as you wish. You can ignore the lines such as "temp0_1, x87status_1 = __fnstcw_memmem16(arg2)" because they are CPU floating point instructions

When we simplify everything, we can write out the solve script.



I copied the entire decompiled validate_serial() (btw derived from the main function), because there are a lot of things to learn from this.

Refer to solve.py for the solve script

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
