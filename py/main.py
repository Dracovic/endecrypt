import sys
import argparse
import my_cryptography as mc
import cli

def main(**kwargs):
        if (len(sys.argv) <= 1): # runs if python main.py (no args)
                en = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst")
                en.info()
                #en = mc.Encoder(algo="caesar_cipher", message="abcdefghijklmnopqrst", key=4)
                #en.info(alf=True)
                print('\n')
                de = mc.Decoder(algo="caesar_cipher", message=en.enc_msg, key=4)
                de.info()
                #de = mc.Decoder(message=en.enc_msg, algo="scytale")
                #de.info(alf=True)
        else:
                cli.main() # runs if python main.py (-e/-d) (plus args)

if __name__ == "__main__":
        main() 