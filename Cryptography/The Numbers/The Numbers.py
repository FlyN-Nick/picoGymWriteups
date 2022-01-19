numbers = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
flag = ''
for num in numbers:
    flag += alphabet[num-1] # zero indexing
flag = flag[:len('picoCTF')] + '{' + flag[len('picoCTF'):] + '}'
print(flag)
