Challenge sourced at:
https://crackmes.one/crackme/5ab77f5333c5d40ad448c102
Information is correct at the time of publishing, 5 September 2026
------------------------------------------------------------------------------------------------------------------------------------
When we try running this program, we see that this is a password checker. Hence, we will have to reverse the algorithm that trys to check our password

For me, I opened it in Binary Ninja. Now, let me give you a high level pseudocode
```python
password = input()
length = len(password)
if pow(length,3)-pow(length,2)*5-length*6 == 56: 			#0x38 is hex for 56, passing it to an algebra calculator yields us a value of 7 for our password length
	score = 0
	total = 0
	for i in range(6):
		score+=(input[i]*3-40)*input[i])
	total = score/10*5						# this DOES NOT equate to total = score/2, as there may be discarded remainders, Hence, we need to ensure that score%10 = 0
									# Refer to the ascii table to check out the ascii values of different chars in which are divisible by 10
	if score-total == 0:						# this is naturally satisfied
		PRINT SUCCESS
	else:
		PRINT FAILURE
	

```

Example:

```text
 wine cm2.exe 
0024:err:environ:init_peb starting L"Z:\\home\\jasper\\CTF\\5ab77f5333c5d40ad448c102\\cm2\\cm2.exe" in experimental wow64 mode
  8            .oPYo. 8
  8            8  .o8 8
  8oPYo. oPYo. 8 .P'8 8  .o  .oPYo. odYo.
  8    8 8  `' 8.d' 8 8oP'   8oooo8 8' `8
  8    8 8     8o'  8 8 `b.  8.     8   8
  `YooP' 8     `YooP' 8  `o. `Yooo' 8   8
  :.....:..:::::.....:..::...:.....:..::..
  ::::::::::::::::::::::::::::::::::::::::
  ::::::::::::::::::::::::::::::::::::::::

  Enter password : PPPPPPP


 You've done it! Now write a solution :)

```



Written using GNU NANO

Code decompiled using Binary Ninja

Note: Not for commercial use.
