# vault-door-1

## Description

This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/29b91e638ccbd76aaa8c0462d1c64d8d/VaultDoor1.java).

## Solution

Looking at the source code, we ca see that it checks if the passward is equal to a plaintext string. However, this is not the entire flag, because the "picoCTF{}" is removed from the input before passing it into the `checkPassword` function. We can paste all of the `password.charAt(x) == 'y'` lines into a text file and read from it line by line with a python script. We can get from each of these lines the character and its respective index, and use this to reconstruct the password.

```java
// code we put into a text file
password.charAt(0)  == 'd' &&
password.charAt(29) == '3' &&
password.charAt(4)  == 'r' &&
password.charAt(2)  == '5' &&
password.charAt(23) == 'r' &&
password.charAt(3)  == 'c' &&
password.charAt(17) == '4' &&
password.charAt(1)  == '3' &&
password.charAt(7)  == 'b' &&
password.charAt(10) == '_' &&
password.charAt(5)  == '4' &&
password.charAt(9)  == '3' &&
password.charAt(11) == 't' &&
password.charAt(15) == 'c' &&
password.charAt(8)  == 'l' &&
password.charAt(12) == 'H' &&
password.charAt(20) == 'c' &&
password.charAt(14) == '_' &&
password.charAt(6)  == 'm' &&
password.charAt(24) == '5' &&
password.charAt(18) == 'r' &&
password.charAt(13) == '3' &&
password.charAt(19) == '4' &&
password.charAt(21) == 'T' &&
password.charAt(16) == 'H' &&
password.charAt(27) == 'f' &&
password.charAt(30) == 'b' &&
password.charAt(25) == '_' &&
password.charAt(22) == '3' &&
password.charAt(28) == '6' &&
password.charAt(26) == 'f' &&
password.charAt(31) == '0';
```

```python
# script to get password
char_index_pairs = []

with open('characters.txt', 'r') as f:
    for line in f:
        char = line[line.index("'")+1] # because it is 'char'
        left_paran_index = line.index('(')
        right_paran_index = line.index(')')
        char_index = line[left_paran_index+1:right_paran_index] # because it is (index)
        char_index_pairs.append([char_index, char])
# above generates a 2d list of [char_index, char]

# reconstruct flag
flag = [None] * len(char_index_pairs)
for pair in char_index_pairs:
    flag[int(pair[0])] = pair[1]

# convert list of chars to string
flag = ''.join(flag)

# we need to add back picoCTF{}
flag = f'picoCTF{{{flag}}}' # 3 brackets because we need to escape one of them
```

## Flag

*picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}*
