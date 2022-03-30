# St3g0

## Description

Download this image and find the flag.

- [Download image](https://artifacts.picoctf.net/c/425/pico.flag.png)

## Solution

The challenge name suggests that the flag has been hidden in the image via steganography. Furthermore, St3g0 is almost exactly $t3g0, which is a commonly used delimetter for lsb encoding. We can make the educated guess that it is LSB encoded, and use a [python script](https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2) we find online to decode.

## Flag

*picoCTF{7h3r3_15_n0_5p00n_87ef5b0b}*
