Challenge sourced at:
https://crackmes.one/crackme/6a77c5d1df981859694944b8

Lets first open up the file in Binary Ninja.
At 00401380 there is a special command called reap, in which 0040144d has told us it is reap. 
So how to find the key? Lets look at 0040138a
sub_401560 is the one that is deciding whether or not we pass So lets reverse engineer that The encryption logic starts at 004015ca.
It xors the input, add rdx_1, which starts at 7, and increments by 3 every time. 
We can find these bytes here: 0x34378e828a78797f 
As x86 architecture stores bytes in little endian, in the memory, the bytes are: 
```text
7f 79 78 8a 82 8e 37 34. 
```
The encryption logic's result is then compared to the target bytes, and if they are the same, you complete the chall.

So, all we need to do is to write a solve script to get the correct key

#solve.py 
```python
target_bytes = [0x7f, 0x79, 0x78, 0x8a,0x82, 0x8e, 0x37, 0x34] x = 7; output = "" for i in range(8): correct = (target_bytes[i]-x)^0x2a output+=chr(correct) x=x+3
print(output)
```

Then, when you run the elf again, just use reap REAPER42

hope it helps!


Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
