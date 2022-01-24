# vault-door-5

## Description

In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://jupiter.challenges.picoctf.org/static/0a53bf0deaba6919f98d8550c35aa253/VaultDoor5.java).

## Solution

Looking at the checkPassword function, we can see that the password is first url encoded, and then base 64 encoded. We can just do these in reverse order with decoders online ([decode base64](https://www.base64decode.org/) [url decoder](https://www.urldecoder.org/)).

```java
public boolean checkPassword(String password) {
    String urlEncoded = urlEncode(password.getBytes());
    String base64Encoded = base64Encode(urlEncoded.getBytes());
    String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                    + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                    + "JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2";
    return base64Encoded.equals(expected);
}
```

## Flag

*picoCTF{c0nv3rt1ng_fr0m_ba5e_64_0b957c4f}*
