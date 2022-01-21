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
print(flag)
