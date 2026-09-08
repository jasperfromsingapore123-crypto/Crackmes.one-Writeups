The challenge is sourced from:

`https://crackmes.one/crackme/5ea7133233c5d47611746483`

Information is correct as of **5 September 2026**.

## Overview

We are given a program that takes a single command-line argument, transforms the input, and prints the resulting string.

I opened the binary in **Binary Ninja**.

At first, the decompiled code looks rather intimidating because it contains a large amount of C++ standard-library code, including expressions such as:

```text
std::allocator<char>
std::string::size_type
std::operator+
```

However, most of this is simply the implementation detail behind `std::string`. Once the important variables and operations are identified, the actual logic is quite simple.

After analyzing the program, I reduced it to the following higher-level pseudocode:

```text
password = input()

array_1 = ""
array_2 = ""
array_3 = ""

for i in range(0, len(password), 3):
    array_1 += password[i]

for i in range(1, len(password), 3):
    array_2 += password[i]

for i in range(2, len(password), 3):
    array_3 += password[i]

correct_password = array_3 + array_1 + array_2

print(correct_password)
```

This is significantly easier to understand than the original decompiled C++.

## Understanding the Transformation

The program separates the input into three groups based on the character's index modulo 3.

In other words:

```text
array_1 = characters at indexes 0, 3, 6, 9, ...
array_2 = characters at indexes 1, 4, 7, 10, ...
array_3 = characters at indexes 2, 5, 8, 11, ...
```

For example, given:

```text
abcdefghij
```

the strings would be approximately:

```text
array_1 = adgj
array_2 = beh
array_3 = cfi
```

The important part is the order in which these strings are combined.

The output is **not**:

```text
array_1 + array_2 + array_3
```

Instead, the program constructs:

```text
array_3 + array_1 + array_2
```

This ordering is what must be reversed in order to recover the original password.

## Looking at the Decompiled Code

Binary Ninja shows code similar to:

```text
004012a4        ref var_68.32 = std::operator+<char>(&var_88, argv)
004012be        class std::string var_48
004012be        ref var_48._M_dataplus.32 = std::operator+<char>(&var_68, &var_a8)
004012e6        std::ostream::operator<<(this: std::operator<<(__os: &std::cout),
```

After renaming the surrounding variables based on how they are built and used, `var_88`, `var_68`, and `var_a8` become much easier to understand.

One confusing part is the appearance of `argv` inside one of the `std::operator+` calls.

It is important not to take every decompiler-generated variable name or type completely literally. Decompilers reconstruct higher-level code from machine instructions, and the recovered representation is not always identical to the original source code.

By tracing how the strings are constructed and then observing the order of the concatenations, we can infer the actual operation represented here.

Conceptually, the final construction is:

```text
temp = array_3 + array_1
correct_password = temp + array_2
```

which simplifies to:

```text
correct_password = array_3 + array_1 + array_2
```

This matches the behavior observed earlier.

## Reversing the Transformation

Once the transformation is understood, reversing it is straightforward.

We know that the program takes characters from the original password based on their positions:

```text
0, 3, 6, ...  -> array_1
1, 4, 7, ...  -> array_2
2, 5, 8, ...  -> array_3
```

and then outputs:

```text
array_3 + array_1 + array_2
```

Therefore, we can split the transformed string back into the three corresponding groups and place each character back into its original position.

The implementation of this reversal can be found in `solve.py`.

---

Written using **GNU Nano**

Code decompiled using **Binary Ninja**

**Note:** Not for commercial use.
