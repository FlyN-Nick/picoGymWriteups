# The Numbers

## Description

The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?

## Solution

At first this may seem like ascii, however the integers in the image are too small. However, all of the integers are smaller than 26, the number of letters in the english alphabet. The integers may correspond to the letters in the alphabet. The below script checks this suspicion and finds it to be true.

```python
numbers = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
flag = ''
for num in numbers:
    flag += alphabet[num-1] # zero indexing
flag = flag[:len('picoCTF')] + '{' + flag[len('picoCTF'):] + '}' # add back the curly braces
print(flag)
```

## Flag

*picoctf{thenumbersmason}*
