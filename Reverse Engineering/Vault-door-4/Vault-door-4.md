# vault-door-4

## Description

This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java).

## Solution

Looking at just the description, we know that the password has simply just been converted to ASCII. Looking at the source code, the encoded password has been stored with as a byte array. We can just use java's String constructor to recreate the password.

```java
System.out.println("picoCTF{" + vaultDoor.decodePassword() + "}"); // we of course need to run the decoder, this is added to main

public String decodePassword() {

    byte[] myBytes = {
        106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
        0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
        0142, 0131, 0164, 063 , 0163, 0137, 0143, 061 ,
        '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
    };
    return new String(myBytes);
}
```

## Flag

*picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e}*
