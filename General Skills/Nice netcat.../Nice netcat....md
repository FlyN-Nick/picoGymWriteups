# Nice netcat...

## Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22342`, but it doesn't speak English...

## Solution

When running `$ nc mercury.picoctf.net 22342` in the terminal, we find that it prints out a list of integers, most ranging from ~50-120, which is a subset of the range of printable ascii characters. We can use an [online decoder](https://www.dcode.fr/ascii-code) to get the flag.

## Flag

* picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d} *
