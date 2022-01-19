# Wireshark doo dooo do doo...

## Description

Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/0505a462ac9beb7412596855df280f6b/shark1.pcapng).

## Solution

As this is a packet capture dump, we can use [Wireshark](https://www.wireshark.org/) to analyze it. If we open the file in wireshark and from the menubar select *analyze* --> *follow* --> *TCP Stream*. Clicking through the streams, we find that stream #5 contains the text "Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}". This seems to be our flag, but it has been encoded. Trying out various common ciphers, we find that the flag was encoded with ROT13.

## Flag

picoCTF{p33kab00_1_s33_u_deadbeef}
