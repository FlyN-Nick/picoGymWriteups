# information

## Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/c28a959c5605d5f67480d5dd3a77f302/cat.jpg).

## Solution

If we check the metadata with `exiftool`, we find that there are two suspicious strings, "7a78f3d9cfb1ce42ab5a3aa30573d617" and "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" that seem to have been encoded with base64.  We can use an [online tool](https://www.base64decode.org/) to get the flag.

## Flag

*picoCTF{the_m3tadata_1s_modified}*
