# hideme

## Description

Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/259/flag.png).

## Solution

Running `exiftool flag.png` does not reveal anything suspicious in the image's metadata. However, running `strings flag.png` (displaying all the printable characters) reveals some human readable text, including `secret/flag.png`. Perhaps there is a file embedded in the image! We can use `binwalk flag.png` to confirm that there is an embedded file. We run `binwalk -e flag.png` to extract, revealing an embedded folder with another image inside of it. This image is the flag written as black text on a white background.

## Flag

*picoCTF{Hidding_An_imag3_within_@n_ima9e_cda72af0}*
