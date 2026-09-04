This is a writeup for The Barista's Secret on Crackmes.one, found here:
https://crackmes.one/crackme/69b878e2ddd6176826ae8a22


Information accurate at the time of publishing

September 4 2026


Solve:

Lets first open it up in Binary Ninja and look at the main function

140001d03    int main()

140001d0b        __main()
140001d1c        SetConsoleOutputCP(wCodePageID: 0xfde9)
140001d2a        SetConsoleCP(wCodePageID: 0xfde9)
140001d2c        anti_debug()
140001d4d        char var_11
140001d4d        deobf(src: "P|wvQavd", len: 8, key: 0x13, dst: &var_11)
140001d57        putchar(_Character: 0xa)
140001d66        puts(_Buffer: &data_140005070)
140001d7c        printf(&data_1400050f8, &var_11)
140001d8b        puts(_Buffer: &data_140005128)
140001d9a        puts(_Buffer: &data_140005160)
140001da9        puts(_Buffer: &data_140005198)
140001db8        puts(_Buffer: &data_1400051d0)
140001dd6        printf("  > ", 
140001dd6            puts(_Buffer: "  License Key Format:  BREW-XXXXXXXX-XXXXXXXX-XXXXXXXX\n")) //you can see the flag is in 4 parts, (BREW-)(XXXX-)(XXX-)(XXX)
140001dec        fflush(_Stream: __acrt_iob_func(_Ix: 1))
140001df1        int64_t var_68
140001df1        __builtin_memset(dest: &var_68, ch: 0, count: 0x50)
140001df1        
140001e6e        if (fgets(_Buffer: &var_68, _MaxCount: 0x50, _Stream: __acrt_iob_func(_Ix: 0))
140001e6e                == 0)
140001e70            return 1
140001e70        
140001e8d        *(&var_68 + strcspn(_Str: &var_68, _Control: "\n\r")) = 0
140001e8d        
140001ea5        if (validate(serial: &var_68) == 0)
140001edc            puts(_Buffer: &data_1400052e0)
140001ea5        else
140001eb1            puts(_Buffer: &data_140005298)
140001ecb            printf("  FLAG: CODEBREW{%s}\n\n", &var_68:5)
140001ecb        
140001eeb        puts(_Buffer: "  Press Enter to exit...")
140001ef0        getchar()
140001ef5        getchar()
140001efa        return 0

This is the entry function, and basically, it takes in your serial key, then passes it through validate().
Now lets take a look at it.


140001c54    int validate(char const* serial)

140001c85        uint32_t C
140001c85        uint32_t B
140001c85        uint32_t A
140001c85        
140001c85        if (parse_blocks(serial, &A, &B, &C) == 0)
140001c87            return 0
140001c87        
140001ca2        if (check1(A, B) == 0)
140001ca4            return 0
140001ca4        
140001cbc        if (check2(C) == 0)
140001cbe            return 0
140001cbe        
140001cd9        if (check3(A, B) == 0)
140001cdb            return 0
140001cdb        
140001cef        if (_poison == 0)
140001cf8            return 1
140001cf8        
140001cf1        return 0


Now, we are given 2(actually more than that but counting is bad aint it lol)  new functions here. 
-Parse Blocks
-Check1,2,3

Alright, so let me give you a high level overview of this

parse_blocks:
This function is basically a license-key parser. It checks that the serial has the right format and then converts the three 8-character hexadecimal chunks into integers.

140001905        deobf(src: "QAVD>", len: 5, key: 0x13, dst: &_Str2)

The line above is likely just XORing "QAVD>" with 0x13, which will yield us BREW-

the remaining parts are just parsing your input into the required format


Lets now look at the checks

check1 just returns whether B equals to A^0xc0ffee42

-----------------------------------------------------------------------------------------------------------------------------------------

check2:
there is an obfuscated string "v`cav``|", xoring it with the key, 0x13 returns us "espresso"
We also have another string "rarqzpr", xoring it with 0x13 returns us arabica

We have a very very goofy bunch:
140001a68    uint32_t check2(uint32_t C)

140001a8f        char var_35
140001a8f        deobf(src: "v`cav``|", len: 8, key: 0x13, dst: &var_35)
140001a98        char* var_10 = &var_35
140001b3b        var_34
140001b3b        var_33
140001b3b        var_32
140001b3b        var_31
140001b3b        var_30
140001b3b        var_2f
140001b3b        var_2e
140001b3b        uint32_t var_14_2 = C ^ 
					(zx.d(var_32.b) << 0x18 |  //0x18 = 24
					zx.d(var_34.b) << 8|
140001b3b             			zx.d(var_35) | 
					zx.d(var_33.b) << 0x10) //0x10 = 16
					^ (zx.d(var_2e.b) << 0x18 //0x18 = 24
140001b3b            			| zx.d(var_30.b) << 8 
					| zx.d(var_31.b) 
					| zx.d(var_2f.b) << 0x10 //0x10 = 16

dst: &var_35 just means that we shld start writing from that. However, since there are 8 chars, we will need 8 vars, which perfectly maps to var_2e

//pseudocode only.

first_part = word[0] | word[1]<<8|word[2]<<16|word[3]<<24
second_part = word[4]|word[5]<<8|word[6]<<16|word[7]<<24
var_14_2 = C^first_part^second_part

lets look at the second very goofy part

140001b5a        deobf(src: "rarqzpr", len: 7, key: 0x13, dst: &var_3d)
140001b63        char* var_28 = &var_3d
140001bc5        var_3c
140001bc5        var_3b
140001bc5        var_3a
140001bc5        return (var_14_2 ^ (zx.d(var_3a.b) << 0x18 | zx.d(var_3c.b) << 8 | zx.d(var_3d)
140001bc5            | zx.d(var_3b.b) << 0x10)) == 0xcafebabe


It takes "arab" and puts them into var_3d, var_c3, var_3b and var_3a

once again, lets break this return statement down.

Lets assign a variable to the later more goofy part... maybe lets call it "temp"

temp = var_3d|var_3c<<8|var_3b<<16|var_3a<<24

then, the return statement simply returns whether var_14_2^temp equlas to 0xcafebabe or not

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, lets take a look at check3:

So, there is an array called data initialised, ie data[8]

in simple pseudocode, its basically 2 loops, as such

for(int i = 0;i<=3;i++){
data[i] = (A>>(i*8))&0xff; //btw <<3 is equal to *8

}
for(int i = 0;i<=3;i++){
data[i+4] = (B>>(i*8))&0xff;
}
return brew_hash(&data,8)&0xfffff == 0xdecaf


Hey there seems to be a new function. Now, lets inspect that.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

brew_hash

Alright, for this function, lets take a look at it.

High level pseudocode:
int result = 0xc0ffe42
for(int i = 0;i<8;i++){
	result^=data[i]*0x9e3779b1
	result = rol32(result,13)
	result -= 0x3f001200
}
return result

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, lets create a solve script. Refer to solve.py





Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
