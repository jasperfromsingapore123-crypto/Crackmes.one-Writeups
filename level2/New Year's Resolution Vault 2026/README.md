Challenge is sourced from:
https://crackmes.one/crackme/695549ef6199fe19c0574632

Information is correct at the time of publishing, 9 September 2026.

We are given a username(the resolution) and password validator. We get to decide the username but the password is decided through some transformation algorithm.
Hence, lets now open up our program in a decompiler, and in my case, its Binary Ninja.

I want to focus on this bit

```text
140001847    uint64_t main()

140001852        __main()
140001868        SetConsoleTitleA(lpConsoleTitle: "New Year's Crackme 2026")
14000186a        print_banner()
14000187a        bool rax_1 = IsDebuggerPresent() != 0
140001894        std::operator<<<std::char_traits<char> >(&_.data$_ZSt4cout, 
140001894            "Enter your New Year's Resolution: ")
1400018a0        std::string var_48
1400018a0        std::string::string(this: &var_48)
1400018b6        std::getline<char>(&_.data$_ZSt3cin, &var_48)
1400018c9        int32_t rbx
1400018c9        
1400018c9        if (std::string::empty(this: &var_48) == 0)
140001902            std::operator<<<std::char_traits<char> >(&_.data$_ZSt4cout, 
140001902                "Enter the Unlock Code for this resolution: ")
140001918            uint64_t var_50
140001918            std::istream& rax_3 = std::istream::operator>>(this: &_.data$_ZSt3cin, &var_50)
140001918            
140001934            if (std::ios::operator!(this: rax_3 + *(*rax_3 - 0x18)) == 0)
140001965                int64_t var_20_1 = calculate_checksum(&var_48)
140001965                
14000196d                if (rax_1 != 0)
140001974                    var_20_1 ^= 0xdeadbeef
140001974                
140001980                if (var_20_1 != var_50)
1400019ca                    std::operator<<<std::char_traits<char> >(&_.data$_ZSt4cout, 
1400019ca                        "\n[FAILED] The vault remains locked. Try again next year.\n")
140001980                else
140001996                    std::operator<<<std::char_traits<char> >(&_.data$_ZSt4cout, 
140001996                        "\n[SUCCESS] Resolution Accepted! Validation complete.\n")
1400019af                    std::operator<<<std::char_traits<char> >(&_.data$_ZSt4cout, 
1400019af                        "Happy New Year 2026!\n")
1400019af                
```

Now, first, a check is performed. Is Debugger pressent? Then, it goes on to print out text, before inputting your resolution(which is kinda like a username), before putting it through calculate_checksum()

Before we dive into calculate_checksum(), we will see this var_20_1^deadbeef. But do note its only triggered when we run it under a debugger.

Hence, now lets look at the calculate_checksum() function.

```text
14000176a    int64_t calculate_checksum(std::string const& arg1)

140001776        int64_t var_20 = 0
14000177e        int64_t result = 0x7e9
14000177e        
1400017d8        for (uint64_t i = 0; i u< std::string::length(this: arg1); i += 1)
1400017bf            result =
1400017bf                rol.q(result + zx.q(*std::string::operator[](this: arg1, i)) * (i + 1), 3)
1400017bf                ^ 0x20262026
1400017bf        
1400017ec        return result
```

Basically, what it does is to initialise a variable called result and give it the value of 0x7e9. Then, add it to the ascii value of the i th char in the resolution. Afterwards, we multiply it with (i*1). Before the final touch, we rotate left the 64 bit result by a number defined, which in this case is "3".
Finally, we xor it with 0x20262026.

With this crucial knowledge, we can write a solve.py.

Refer to solve.py

Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
