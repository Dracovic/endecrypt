import sys
import my_cryptography as mc
import cli

def main():
        if (len(sys.argv) <= 1): # runs if python main.py (no args)
                en = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius =4)
                en.info()
                print('\n')
                de = mc.Decoder(message=en.enc_msg, algo="scytale", radius =4)
                de.info()
                # FOR QUICK DEBUG
                #en = mc.Encoder(algo="caesar_cipher", message="abcdefghijklmnopqrst", key=4)
                #en.info(alf=True)
                #de = mc.Decoder(algo="caesar_cipher", message=en.enc_msg, key=4)
                #de.info(alf=True)
                #en = mc.Encoder(message = "TheQuickBrownFoxJumpsOverTheLazyDog", algo = "affine", key = 5)
                #en.info(alf=True)
                #NEXT TO TEST:
                de = mc.Decoder(message = "LNywOSo2lzkYfFk3ZOapEmTyzLNy9eb8vkI", algo = "affine", key = 5)
                de.info(alf=True)
                return None
        else:
                return cli.main() # runs if python main.py (-e/-d) (plus args)

if __name__ == "__main__":
        main() 