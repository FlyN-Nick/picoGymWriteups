# vault-door-training

## Description

Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/1afdf83322ee9c0040f8e3a3c047e18b/VaultDoorTraining.java).

## Solution

Looking at the source code, we ca see that it checks if the passward is equal to a plaintext string. However, this is not the entire flag, because the "picoCTF{}" is removed from the input before passing it into the `checkPassword` function.

```java
String input = userInput.substring("picoCTF{".length(), userInput.length()-1); // picoCTF{} is removed with this line
public boolean checkPassword(String password) {
    return password.equals("w4rm1ng_Up_w1tH_jAv4_eec0716b713"); // plaintext password
}

```

## Flag

picoCTF{w4rm1ng_Up_w1tH_jAv4_eec0716b713}
