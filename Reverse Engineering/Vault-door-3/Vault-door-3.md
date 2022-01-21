# vault-door-3

## Description

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a648ca6dd275b9454c5d0de6d0f6efd3/VaultDoor3.java).

## Solution

Instead of trying to do the scrambling the checkPassword function does just in reverse, we can instead observe how a string we input is scrambled and map the old indexes of characters to the new. Let's change the checkPassword function to make this possible.

```java
// must change return type 
public boolean checkPassword(String password) {
    if (password.length() != 32) {
        return false;
    }
    char[] buffer = new char[32];
    int i;
    for (i=0; i<8; i++) {
        buffer[i] = password.charAt(i);
    }
    for (; i<16; i++) {
        buffer[i] = password.charAt(23-i);
    }
    for (; i<32; i+=2) {
        buffer[i] = password.charAt(46-i);
    }
    for (i=31; i>=17; i-=2) {
        buffer[i] = password.charAt(i);
    }
    String s = new String(buffer);
    System.out.println(s); // so we can see the scrambled version
    return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
}
```

We know that the password is of length 32, so let's construct a string that is composed of 32 unique characters.
```java
String toScramble = "abcdefghijklmnopqrstuvwxyz012345"
```

Let's run our modified version of our script (don't forget to add picoCTF{} to our string).
When doing so, we get this string: `abcdefghponmlkji4r2t0vyxwzu1s3q5`.

Now let's write a script that determines the index mappings of the scrambling and then uses those mappings to descramble the flag.

```python
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
```

## Flag

*picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}*
