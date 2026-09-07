The challenge is sourced from 
https://crackmes.one/crackme/65ed01ee7b0f7ceced2c5afb

Information is correct at the time of publishing.

We are given a password checker. However, this is slightly different. When we just run the file normally, it throws us an error:

```text
jasper@jasper:~/CTF/65ed01ee7b0f7ceced2c5afb$ ./ctf_1 
Error opening file: No such file or directory
```
However, do not worry, as this error is purely attributed to the challenge. An actual error will look more of like this:

```text
jasper@jasper:~/CTF/65ed01ee7b0f7ceced2c5afb$ ./ctf_2
bash: ./ctf_2: No such file or directory
```

Hence, what file does it want? Let us open it up in our Binary Ninja. 

```text
00401420    int32_t main(int32_t argc, char** argv, char** envp)

00401428        int32_t var_10 = 0
0040143a        char filename
0040143a        strcpy(&filename, "secret_flag")
0040144a        FILE* fp = fopen(&filename, mode: "r")
0040144a        
```
Hence, as you can see, it expects a file called secret_flag, and then opens it. Thus, lets see what happens when we create such a file.

```text

jasper@jasper:~/CTF/65ed01ee7b0f7ceced2c5afb$ cat secret_flag 
hello world
jasper@jasper:~/CTF/65ed01ee7b0f7ceced2c5afb$ ./ctf_1 
jasper@jasper:~/CTF/65ed01ee7b0f7ceced2c5afb$ 

```
Nothing appears, though no error is thrown. So, lets now reverse the CONTENTS in which we put into "secret_flag"

```text
00401569            strcpy(&var_41, buf)
00401569            
00401579            for (int32_t i = 0; i s< 8; i += 1)
00401585                var_1c_1 += 1
004015ad                *(&fkey + sx.q(i)) ^= var_41[sx.q(i)]
004015d3                var_41[sx.q(i)] ^= *(&key + sx.q(i + 1))
004015d3                
004015f1                if (sx.d(var_41[sx.q(i)]) != sx.d(*(&skey + sx.q(i))))
004015f3                    var_2c_1 = 0
004015fa                    break
004015fa            
00401612            if (var_2c_1 == 1)
0040162c                giveFlag(var_1c_1, var_50_1.q, var_48_1)
```

As you can wee, we have this checker, before the giveFlag() function is called.
Hence, likely, the for loop above somehow transforms the input. Yet before I go to my solve.py, I want to highlight something.

Notice that fkey is being xored using var_41. HOWEVER, it is NOT used afterwards. That was how I got fooled in my attempt to solve it. Yet, just note that fkey's the one being transformed, not var_41.

Now lets refer to solve.py



Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
