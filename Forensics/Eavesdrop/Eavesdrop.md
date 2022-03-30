# Eavesdrop

## Description

Download this packet capture and find the flag.

- [Download packet capture](https://artifacts.picoctf.net/c/362/capture.flag.pcap)

## Solution

As this is a packet capture dump, we can use [Wireshark](https://www.wireshark.org/) to analyze it. A good start is to follow the TCP streams. To do this, in the menubar select *analyze* --> *follow* --> *TCP Stream*. In the very first stream, we find a chat conversation between two people, discussing a "secret" file transfer. According to the chat, it will be sent to the port 9002, and to decrypt the file we must run `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`. Now let's find the file.

If we google how to filter for port number, we find that we can use the filter `tcp.port == 9002`. We find that one of the packets sent has 48 bytes of data attached to it. Additionally, it begins with the text "Salted", indicating that it has been salted by openssl, aka what we're looking for.

Now we have to figure out how to convert this hex into an actual file. With some online research ("how to convert hex to binary"), we find that we can use this command: `xxd -r -p input.txt file.des3`. Let's copy the hex (right click --> Copy --> ...as a Hex Stream), and paste it into a text file and run this command.

Now let's run the decryption command `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`. Hmm, we get an error saying "bad decrypt". Perhaps we're using the wrong version of openssl. Let's repeat the above steps in the picoCTF web shell, which should have the right version. Doing so gets us the flag.

## Flag

*picoCTF{nc_73115_411_77b05957}*
