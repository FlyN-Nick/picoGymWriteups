# substitution0

## Description

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?
Download the message [here](https://artifacts.picoctf.net/c/383/message.txt).

## Solution

Given the challenge description, we know that this is a substitution cipher, and it has some sort of "key". Looking at the text, we find this suspicious string at the beginning, *PAQZTNDSRYWFEXGJKCVLBUHOMI*. As this is 26 characters long, and has every letter of the alphabet, it must be the substitution alphabet for a mono-alphabetic substitution. We can use an [online decoder](https://www.dcode.fr/monoalphabetic-substitution) to decrypt.

## Flag

*PICOCTF{5UB5717U710N_3V0LU710N_AA1CC2B7}*
