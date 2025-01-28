# endecrypt
(Inspired and with thanks to CrypTool-Online! https://www.cryptool.org/en/)

Encryption-Decryption tool with many methods including old historical ciphers. Includes command-line support as well as Encoder and Decoder classes written in Python.

endecrypt (-d/-e) input --algorithm -o

Options:
-e --en --encrypt	The program with run the selected algorithm to encrypt the input
-d --de --decrypt	The program with run the selected algorithm to decrypt the input
-a --algorithm      The method of encryption or decryption desired to run
-m --message        The string or file to be (en/de)crypted
-i --input          The string or file to be (en/de)crypted
-o --output         The file or path to the file where the output shall be saved.
                    Defaults to terminal output

Optional: (depending on the selected algorithm)
-r --radius The 'key'or radius for the Scytale transposition cipher

This program takes an input which can be a file.txt or an inline text and returns the same once the desired encryption or decryption algorithm has been run.

List of algorithms (for present(*) and future(~) support)

SCYTALE
Polybius Square
ATBASH
CEASAR CIPHER
ROT13 CIPHER
AFFINE CIPHER
RAIL FENCE CIPHER
KEYWORD CIPHER
