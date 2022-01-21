orig = "abcdefghijklmnopqrstuvwxyz012345"
scrambled = "abcdefghponmlkji4r2t0vyxwzu1s3q5"

mappings = {}
for i in range(len(orig)):
    mappings[scrambled.index(orig[i])] = i


scrambled_flag = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
flag = [None] * len(scrambled_flag)

for i in range(len(scrambled_flag)):
    flag[mappings[i]] = scrambled_flag[i]

flag = "".join(flag)
flag = f"picoCTF{{{flag}}}"
print(flag)
