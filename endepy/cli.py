import argparse
from pathlib import Path
import my_cryptography as mc

def parse_cmd_args() -> dict:
    """This function parses the inputs for when the tool is used directly from the command line. It first checks if any
        were provided at all becuse it can also be called from hard coding in main().

        It has the following options:
        -h, --help            show this help message and exit

        (REQUIRED one or the other)
        -e, -en, --encrypt    Encryption of the message or file will take place     
        -d, -de, --decrypt    Decryption of the message or file will take place     

        (REQUIRED)
        -a ALGO, --algo ALGO, --algorithm ALGO: !Defaults to Scytale as of 2025-01-24
                        Selected encryption/decryption algorithm

        -r RADIUS, --radius RADIUS: !Defaults to 5 as of 2025-01-24
                        Size of the radius for the Scytale Cypher

        -i INPUT, --input INPUT: !Default to "Endycrypt - encryption and decryption tool"
                        The input to be encrypted/dectypted. Can be string,   
                        '.txt' file name or file path

        -o OUTPUT, --output OUTPUT
                        Prints out by default but can be a '.txt' file name   
                        or file path"""

    parser = argparse.ArgumentParser(description="Encrypt and decrypt messages and files", epilog="")
    en_or_de = parser.add_mutually_exclusive_group(required=True)
    en_or_de.add_argument("-e", "-en", "--encrypt", action="store_true", help="Encryption of the message or file will take place", default=False)
    en_or_de.add_argument("-d", "-de", "--decrypt", action="store_true", help="Decryption of the message or file will take place", default=False)

    parser.add_argument("-a", "--algo", "--algorithm", help= "Selected encryption/decryption algorithm")
    parser.add_argument("-r", "--radius", type=int, help= "Size of the radius for the Scytale Cypher")

    parser.add_argument("-m", "--message", help= "The message to be (en/de)crypted", default="Endecrypt - encryption and decryption tool")
    parser.add_argument("-i", "--input", help= "The input to be (en/de)ctypted. Can be string, '.txt' file name or file path", default='Endecrypt - encryption and decryption tool')
    parser.add_argument("-o", "--output", help= "Prints out by default but can be a '.txt' file name or file path", default=None)
    
    args = parser.parse_args()
    args_dict = vars(args)

    return args_dict
#def manage_case_args(algo: str, args: dict) -> dict: a dictionary that hold the correct dict for kwargs to use in the Encoder and Decoder classes

    #for i in range(1,20): # default scytale default behaviour devtest, proper testing in tests/
        #en.enc_msg = en.algo(r=i)                # more of a visualization really..
        #de.enc_msg = en.enc_msg
        #de.dec_msg = de.algo(r=i)
        #print('\n')
        #print(f'Original Message r={i}: {en.org_msg}')
        #print(f'Encoded Message  r={i}: {en.enc_msg}')
        #print(f'Encoded Message  r={i}: {de.enc_msg}')
        #print(f'Decoded Message  r={i}: {de.dec_msg}')
    # scytale tests manual 1 - 9
        #en1 = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius=1)
        #de1 = mc.Decoder(algo="scytale", message=en1.enc_msg, radius=1)

        #print('\n')
        #print(f'Original Message r=1: {en1.org_msg}')
        #print(f'Encoded Message r=1:  {en1.enc_msg}')
        #print(f'Encoded Message r=1:  {de1.enc_msg}')
        #print(f'Decoded Message r=1:  {de1.dec_msg}')

        #en2 = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius=2)
        #de2 = mc.Decoder(algo="scytale", message=en2.enc_msg, radius=2)
    
        #print('\n')
        #print(f'Original Message r=2: {en2.org_msg}')
        #print(f'Encoded Message r=2:  {en2.enc_msg}')
        #print(f'Encoded Message r=2:  {de2.enc_msg}')
        #print(f'Decoded Message r=2:  {de2.dec_msg}')

        #en3 = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius=3)
        #de3 = mc.Decoder(algo="scytale", message=en3.enc_msg, radius=3)

        #print('\n')
        #print(f'Original Message r=3: {en3.org_msg}')
        #print(f'Encoded Message r=3:  {en3.enc_msg}')
        #print(f'Encoded Message r=3:  {de3.enc_msg}')
        #print(f'Decoded Message r=3:  {de3.dec_msg}')

        #en4 = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius=4)
        #de4 = mc.Decoder(algo="scytale", message=en4.enc_msg, radius=4)

        #print('\n')
        #print(f'Original Message r=4: {en4.org_msg}')
        #print(f'Encoded Message r=4:  {en4.enc_msg}')
        #print(f'Encoded Message r=4:  {de4.enc_msg}')
        #print(f'Decoded Message r=4:  {de4.dec_msg}')

        #en5 = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius=5)
        #de5 = mc.Decoder(algo="scytale", message=en5.enc_msg, radius=5)

        #print('\n')
        #print(f'Original Message r=5: {en5.org_msg}')
        #print(f'Encoded Message r=5:  {en5.enc_msg}')
        #print(f'Encoded Message r=5:  {de5.enc_msg}')
        #print(f'Decoded Message r=5:  {de5.dec_msg}')

        #en6 = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius=6)
        #de6 = mc.Decoder(algo="scytale", message=en6.enc_msg, radius=6)

        #print('\n')
        #print(f'Original Message r=6: {en6.org_msg}')
        #print(f'Encoded Message r=6:  {en6.enc_msg}')
        #print(f'Encoded Message r=6:  {de6.enc_msg}')
        #print(f'Decoded Message r=6:  {de6.dec_msg}')
    
        #en7 = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius=7)
        #de7 = mc.Decoder(algo="scytale", message=en7.enc_msg, radius=7)

        #print('\n')
        #print(f'Original Message r=7: {en7.org_msg}')
        #print(f'Encoded Message r=7:  {en7.enc_msg}')
        #print(f'Encoded Message r=7:  {de7.enc_msg}')
        #print(f'Decoded Message r=7:  {de7.dec_msg}')

        #en8 = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius=8)
        #de8 = mc.Decoder(algo="scytale", message=en8.enc_msg, radius=8)

        #print('\n')
        #print(f'Original Message r=8: {en8.org_msg}')
        #print(f'Encoded Message r=8:  {en8.enc_msg}')
        #print(f'Encoded Message r=8:  {de8.enc_msg}')
        #print(f'Decoded Message r=8:  {de8.dec_msg}')

        #en9 = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius=9)
        #de9 = mc.Decoder(algo="scytale", message=en9.enc_msg, radius=9)

        #print('\n')
        #print(f'Original Message r=9: {en9.org_msg}')
        #print(f'Encoded Message r=9:  {en9.enc_msg}')
        #print(f'Encoded Message r=9:  {de9.enc_msg}')
        #print(f'Decoded Message r=9:  {de9.dec_msg}')

def main():
    try:
        args = parse_cmd_args() # dict if there are args, False if there are none
    except Exception as e:
        print(f'An unexpected error occured: {e}')

    print("No command line arguments were provided. Running the program with default values.")
    print(f'Encoder initiated...')
    en = mc.Encoder(algo="atbash", message=args["message"])
    en.info()
    if args["decrypt"] == True:
        print(f'Decoder initiated...')
        de = mc.Decoder (algo="atbash", message=en.enc_msg)
        de.info()
    return None

if __name__ == "__main__":
    # used for cmdline interaction with program
        # used for hard coded examples and debugging
        main()