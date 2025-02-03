from .coder import Coder
import string

class Decoder(Coder): # Decoder inherits cmdline arg mngment and alphabet definition
    """A Decoder is an Object that is created with a specified algorithm as a parameter
       as well as an optional message to decode on creation."""

    def __init__(self,**kwargs):
        """ The Decoder class is initialized with a message and an algorithm to encode the message.

            Attributes:
                enc_msg: str - the original message to be encoded.
                algo: str - the algorithm to encode the message.
                dec_msg: str - the encoded message.

            Examples:
                scy_dec = Decoder(algo = 'scytale', message = '05af16bg27ch38di49ej', radius = 4)
                print(scy_dec.dec_msg)
                >> 0123456789abcdefghij
        """
        if "algo" in kwargs: # user defined algorithm
            self._validate_algo(kwargs["algo"])
        else:
            self.algo = getattr(self, "rot13")
        super().__init__(**kwargs)
        self.enc_msg = self.org_msg
        self.dec_msg = self.run_decryption(**kwargs)

    def info(self, alf: bool = False):
        """Prints the attributes of the Encoder object."""
        print(f'Type: {self.__class__.__name__}')
        print(f'Algorithm: {self.algo.__name__}')
        print(f'Encrypted message: {self.enc_msg}')
        print(f'Decrypted message: {self.dec_msg}')
        if alf: # alphaber_flag
            print(f'Alphabet: {self.alphabet}')
        super().info()

    def run_decryption(self, **kwargs):
        if kwargs["algo"] == "scytale":
            return self.scytale(kwargs["radius"])	
        elif 'key' in kwargs:
            return self.algo(kwargs["key"])
        else:
            return self.algo()
      
    def scytale(self, r: int = 4) -> str:
        """ Scytale is a simple transposition cipher used in ancient Greece. I imagine it as a regular prism
            of a certain number of faces. The number of faces is the key to the cipher. The message is written
            on the prism and then read off in a spiral fashion.
            
            Attributes:
                r: int - the number of faces on the prism.
                
            Returns:
                result: str - the encoded message.
        """
        enc_msg_len = len(self.enc_msg) - 1
        result = [" " for _ in range(enc_msg_len+1)]
        i = 0
        j = 0
        index = 0
        t = 0
        while(j <= enc_msg_len):
            if index > enc_msg_len:
                t += 1
                i = 0
                index = r*i+t
            result[j] = self.enc_msg[index]
            i += 1
            index = r*i+t
            j += 1
        return ''.join(result)

    def atbash(self) -> str: # Only works with alphanumeric strings
        atbash_phabet = {k:v for k, v in zip(self.alphabet.keys(), reversed(self.alphabet.keys()))}
        result = ''.join([atbash_phabet[c] for c in self.enc_msg])
        return result

    def polybius_square(self) -> str: # Only works with lower case alphabet
        alphabet = list(string.ascii_lowercase)
        alphabet.remove('j')
        transform = [str(i+1)+str(j+1) for i in range(5) for j in range(5)]
        #for i in range(5):
            #for j in range(5):
                #transform.append(str(i+1)+str(j+1))

        #print(alphabet)
        #print(transform)
        #print([*zip(alphabet, transform)])

        alphabet_dict = {t: k for k, t in [*zip(alphabet, transform)]}
        #print(alphabet_dict)

        result = ''
        for i, j in zip(self.enc_msg[::2], self.enc_msg[1::2]):
            result = result + alphabet_dict[i+j]

        return result

    def caesar_cipher(self, key = 4) -> str: # Only works with lower case alphabet and spaces
        alphabet = list(string.ascii_lowercase)

        #print(self.enc_msg)
        #print(alphabet)

        result = ""
        for char in self.enc_msg:
            if char != " ":
                index = alphabet.index(char) - key
                result = result + alphabet[index]
            else:
                result = result + " "
        return result

    def rot13(self) -> str:
        return self.caesar_cipher(key = 14)
        ...

#de = Decoder(message="zyxwvutsrqponmlkjihg", algo="atbash")
#print(de.atbash())
#de = Decoder(message="111213141521222324253132333435", algo="polybius_square")
#print(de.dec_msg)
#de = Decoder(message="efghijklmnopqrstuvwx", algo="caesar_cipher")
#de = Decoder(message="opqrstuvwxyzabcdefgh", algo="rot13")
#print(de.dec_msg)