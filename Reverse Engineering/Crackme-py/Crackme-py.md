# crackme-py

## Description

[crackme.py](https://mercury.picoctf.net/static/2ff6c888060f14af5db1232e319547c9/crackme.py)

## Solution

If we open the script, we can see that there is a variable named "bezos_cc_secret" which has been encoded with some sort of encyrption method. Conveniently, the encoding function is in the python script, and it is bidirectional (encrypts and decrypts). We can edit the script so that it runs this decrypting function with the encrypted secret to get the flag.

```python
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE067d3eh2bN" # the secret

# decode function
def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)

choose_greatest() # replace this with decode_secret(bezos_cc_secret) to get the flag
```

## Flag

*picoCTF{1|\/|_4_p34|\|ut_ef5b69a3}*
