# vault-door-6

## Description

This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](https://jupiter.challenges.picoctf.org/static/cdb33ffba609e2521797aac66320ec65/VaultDoor6.java).

## Solution

Looking at the source code, for each byte in the user submitted password, it checks if x ^ 0x55 = y, where x is the password byte and y is the encrypted byte. The description states that an XOR encryption scheme is being used, and using google we can confirm that ^ is the operator for XOR. If we google what the inverse function of XOR is, we find that it is itself, where if x ^ y = z, then y ^ z = x. We can use this fact to reverse the XOR encrypted password.

```java
vaultDoor.decryptPassword(); // we of course need to run the decoder, this is added to main

public void decryptPassword() {
    byte[] myBytes = {
        0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
        0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
        0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
        0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36,
    };
    byte[] unencryptedBytes = new byte[32];
    for (int i=0; i<32; i++) {
        byte unencrptedByte = (byte) (myBytes[i] ^ 0x55);
        unencryptedBytes[i] = (unencrptedByte);
    }
    System.out.println("picoCTF{" + new String(unencryptedBytes) + "}");
}
```

## Flag

*picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc}*
