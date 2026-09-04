Challenge source can be found at https://crackmes.one/crackme/68eb89c32d267f28f69b7544.
Accurate at the time this was written. 4 September 2026

When we try to run the file just as ./chall, we realise that it returns a Segmentation Fault. Lets try running it under gdb(in my case I also have gef) :)

Lets first run it... then check it out with info proc mappings
```text
gef➤  info proc mappings
process 55979
Mapped address spaces:

Start Addr         End Addr           Size               Offset             Perms File 
0x0000000000010000 0x0000000000011000 0x1000             0x1000             r-xp  /home/jasper/CTF/68eb89c32d267f28f69b7544/chall/todo/chall 
0x00007ffff7ff7000 0x00007ffff7ffb000 0x4000             0x0                r--p  [vvar] 
0x00007ffff7ffb000 0x00007ffff7ffd000 0x2000             0x0                r--p  [vvar_vclock] 
0x00007ffff7ffd000 0x00007ffff7fff000 0x2000             0x0                r-xp  [vdso] 
0x00007ffffffdd000 0x00007ffffffff000 0x22000            0x0                rw-p  [stack] 
0xffffffffff600000 0xffffffffff601000 0x1000             0x0                --xp  [vsyscall] 
gef➤ 
```
So as we can see, the program's space is between 0x10000 and 0x11000

lets analyse nearby instructions to see whats causing the seg fault

First, lets run starti, to actually see the first instruction, then run x/24i $pc to see the nearby instructions. We get this:
```text
gef➤  x/24i $pc
=> 0x1007a:	push   rbp
   0x1007b:	mov    rbp,rsp
   0x1007e:	sub    rsp,0x30
   0x10082:	movabs rax,0x6d202c7972746e45
   0x1008c:	mov    edx,0xa6e6961
   0x10091:	mov    QWORD PTR [rbp-0x30],rax
   0x10095:	mov    QWORD PTR [rbp-0x28],rdx
   0x10099:	mov    QWORD PTR [rbp-0x20],0x0
   0x100a1:	mov    QWORD PTR [rbp-0x18],0x0
   0x100a9:	mov    DWORD PTR [rbp-0x4],0xc
   0x100b0:	mov    edx,DWORD PTR [rbp-0x4]
   0x100b3:	lea    rax,[rbp-0x30]
   0x100b7:	mov    esi,edx
   0x100b9:	mov    rdi,rax
   0x100bc:	call   0x10000
   0x100c1:	mov    eax,0x0
   0x100c6:	leave
   0x100c7:	ret
   0x100c8:	data16 ins BYTE PTR [rdi],dx
   0x100ca:	(bad)
   0x100cb:	addr32 cs je 0x10147
   0x100cf:	je     0x100d1
   0x100d1:	add    BYTE PTR [rax],al
   0x100d3:	add    BYTE PTR [rax],al

```
We can see that the function ends with:

0x100c6: leave
0x100c7: ret

Before ret executes, inspect the top of the stack:

gef➤ info reg rsp rbp
rsp  0x7fffffffdae0
rbp  0x0

gef➤ x/g $rsp
0x7fffffffdae0: 0x0000000000000001

So:

[rsp] = 0x1

ret takes the value at [rsp] and uses it as the next instruction address. Therefore, when ret executes, it will try to jump to 0x1, which is invalid and causes the segmentation fault.

To observe this directly, set a breakpoint at the leave instruction:

b *0x100c6
c

Then step through leave and ret using:

ni

This lets us watch how the stack changes just before the crash.

Alright.. Now lets try running it with a few arguments. 
gef➤ run "1" "2" "3"
Lets run it again.
Eventually, we reach this stage:

[#0] Id 1, Name: "chall", stopped 0x4 in ?? (), reason: SIGSEGV

Huh. This time we passed 3 args, 1,2,3. Ths, it ended up at 0x4. Then, where do we actually going to need flag.txt file?

Lets analyse it.

gef➤  find 0x10000,+0x1000, "flag.txt"
0x100c8
1 pattern found.
gef➤  find 0x10000,+0x1000,0x100c8
0x10030
0x10280
2 patterns found.

As we can see, 0x10030 and 0x10280 dereferences the position of flag.txt.
Lets analyse them as well

And hence, we have this:
```text
gef➤  x/32i 0x10030-0xc
   0x10024:	push   rbp
   0x10025:	mov    rbp,rsp
   0x10028:	sub    rsp,0x50
   0x1002c:	mov    QWORD PTR [rbp-0x8],0x100c8
   0x10034:	mov    rdi,QWORD PTR [rbp-0x8]
   0x10038:	mov    rax,0x2
   0x1003f:	mov    rsi,0x2
   0x10046:	mov    rdx,0x1ff
   0x1004d:	syscall
   0x1004f:	mov    rdi,rax
   0x10052:	lea    rsi,[rbp-0x50]
   0x10056:	mov    rax,0x0
   0x1005d:	mov    rdx,0xb
   0x10064:	syscall
   0x10066:	lea    rax,[rbp-0x50]
   0x1006a:	mov    esi,0xb
   0x1006f:	mov    rdi,rax
   0x10072:	call   0x10000
   0x10077:	nop
   0x10078:	leave
   0x10079:	ret
   0x1007a:	push   rbp
   0x1007b:	mov    rbp,rsp
   0x1007e:	sub    rsp,0x30
   0x10082:	movabs rax,0x6d202c7972746e45
   0x1008c:	mov    edx,0xa6e6961
   0x10091:	mov    QWORD PTR [rbp-0x30],rax
   0x10095:	mov    QWORD PTR [rbp-0x28],rdx
   0x10099:	mov    QWORD PTR [rbp-0x20],0x0
   0x100a1:	mov    QWORD PTR [rbp-0x18],0x0
   0x100a9:	mov    DWORD PTR [rbp-0x4],0xc
   0x100b0:	mov    edx,DWORD PTR [rbp-0x4]
gef➤  

We see these instructions:

   0x10024:     push   rbp
   0x10025:     mov    rbp,rsp
   0x10028:     sub    rsp,0x50
These are function proluges, and hence, we can comfirm this is the function we want to reach. 
```
btw:
push rbp
→ save the caller's old frame pointer

mov rbp, rsp
→ create a new stack frame

sub rsp, 0x50
→ reserve 0x50 bytes for local variables

0x10024 = 65572 in decimal.

Hence, we need to pass 65572-1=65571 chall, as the program's argument counter includes ./chall as an argument. 


The following command helps us complete the chall

./chall{1..65572}


Note: It may be confusing cos we just said we want 65571 args. But, you need to realise we are starting at "1", and hence, it is actually 65571 arguments

```text
jasper@jasper:~/CTF/68eb89c32d267f28f69b7544/chall/todo$ ./chall {1..65572}
Entry, main
flag{done}
Segmentation fault         (core dumped) ./chall {1..65572}
jasper@jasper:~/CTF/68eb89c32d267f28f69b7544/chall/todo$ 
```


Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
