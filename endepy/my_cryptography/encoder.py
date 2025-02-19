from my_cryptography.coder import Coder
import string
import numpy as np

class Encoder(Coder): # Encoder inherits cmdline arg mngment and alphabet definition
    """An Encoder tool to encrypt messages using various algorithms.

        An Encoder is an Object that is created with a specified alphabet, algorithm,
        message, input file, and output file as parameters.

            Attributes:
                alphabet: dict - the alphabet to be used for encryption.
                    Defaults to all ascii letters and digits using the -al --alphabet argument.
                org_msg: str - the original message to be encrypted.
                algo: str - the algorithm used to encrypt the message.
                enc_msg: str - the encrypted message.
    """

    def __init__(self, **kwargs):
        """ The Encoder class is initialized with a message and an algorithm to encrypt the message.

            Attributes:
                org_msg: str - the original message to be encoded.
                algo: str - the algorithm to encode the message.
                enc_msg: str - the encoded message.

            Examples:
                scy_enc = Encoder(algo = 'scytale', message = '0123456789abcdefghij', radius = 4)
                print(scy_enc.enc_msg)
                >> 05af16bg27ch38di49ej
        """
        super().__init__(**kwargs)
        if "algo" in kwargs: # user defined algorithm
            algo = kwargs["algo"]
            super()._validate_algo(algo)
        else:
            self.algo = getattr(self, "rot13")
        self.enc_msg = self.run_encryption(kwargs)

    def info(self, alf: bool = False) -> str: # also prints said str
        """Prints the attributes of the Encoder object."""
        #print(f'Type: {self.__class__.__name__}')
        #print(f'Algorithm: {self.algo.__name__}')
        #print(f'Original message: {self.org_msg}')
        #print(f'Encrypted message: {self.enc_msg}')
        #if alf: # alphabet_flag
            #print(f'Alphabet: {self.alphabet}')
        #super().info()
        info = f"""
        Type: {self.__class__.__name__}
        Algorithm: {self.algo.__name__}
        Original message: {self.org_msg	}
        Encrypted message: {self.enc_msg}
        """
        if alf:
            info = info + f'Alphabet: {self.alphabet}\n'
        #info = info + super().info()
        print(info)
        return info

    def run_encryption(self, kwargs) -> str:
        """Runs the algorithm specified in the Encoder object.
        """
        if "algo" in kwargs:
            if kwargs["algo"] == "scytale":
                if 'radius' in kwargs:
                    return self.scytale(kwargs["radius"])
                else:
                    raise ValueError("Scytale requires a radius to be specified")
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
        msg_len = len(self.org_msg) - 1
        result = [' ' for _ in range(msg_len+1)] # Initialize the result string (empty)
        i = 0       # Counter for the loop
        j = 0
        index = 0   # The actual variable used to index the orginal message and extract the character in turn
        t = 0       # This variable is used to control the overflow of the index when it wraps back around
        while(j <= msg_len):    # Loop until the result string is the same length as the original message
            if index > msg_len:           # If the index is greater than the length of the original message it would overflow, so this resets it
                t += 1
                i = 0                     # Reset the counter
                index = r*i+t             # Restart the extraction from the new beginning
            result[index] = self.org_msg[j] # Extracts the character from the original message and adds it to the result string
            i += 1                                # Increment the counter
            j += 1                                # Increment the counter
            index = r*i+t                         # Calculate the next index to extract the character from the original message
        return ''.join(result)

    def atbash(self) -> str: # Only works with alphanumeric strings
        atbash_phabet = {k: v for k, v in zip(self.alphabet.keys(), reversed(self.alphabet.keys()))}
        #print(atbash_phabet)
        result = ''.join([atbash_phabet[c] for c in self.org_msg])
        #print(result)
        return result
        
    def polybius_square(self) -> str: # Only returns lowercase alphabet letters
        n = 5 # The size of the polybius square
        alphabet = list(string.ascii_lowercase)
        alphabet.remove('j') 
        square = np.array(alphabet).reshape(5, 5)

        alphabet_dict = {}
        for row in square:
            for letter in row:
                row, col = np.where(square == letter)
                alphabet_dict[letter] = str(row[0]+1) + str(col[0]+1)
                #print(f'{letter}: {row[0]+1} {col[0]+1}')
        #print(alphabet_dict)
        result = ''
        for letter in self.org_msg:
            if letter == 'j':
                result = result + alphabet_dict['i']
            else:
                result = result + alphabet_dict[letter]
            
        return result
    
    def caesar_cipher(self, key = 4) -> str:                  # Only rotates to the right | supports spaces
        lower_dict = dict([*zip(string.ascii_lowercase, [f for f in range(1,26)])])   # iterate linearly 3 times, then a quick lookup for each char in org_msg
        upper_dict = dict([*zip(string.ascii_uppercase, [f for f in range(1,26)])])   # should be inherited by both Encode and Decode in the future
        digits_dict = dict([*zip(string.digits, [f for f in range(1,26)])])

        caesar_lookup = []
        for letter in self.org_msg:
            if letter == ' ':
                caesar_lookup.append(' ')
            elif letter in string.ascii_lowercase:
                caesar_lookup.append(str(lower_dict[letter]))
            elif letter in string.ascii_uppercase:
                caesar_lookup.append(str(upper_dict[letter]))
            else:
                letter in string.digits
                caesar_lookup.append(str(digits_dict[letter]))

        rotation = list([i for i in range(26-key+1, 27)] + [i for i in range(1, 27-key+1)]) # applies the rotation for the keys to map in the dict
        rotated_lower = dict([*zip(rotation, string.ascii_lowercase)])       # creates the paired list for the dict
        rotated_upper = dict([*zip(rotation, string.ascii_uppercase)])        # creates the paired list for the dict
        rotated_digits = dict([*zip(list([i for i in range(10-key+1, 10)] + [i for i in range(10-key+1)]), string.digits)])                # creates the paired list for the dict
        #print(rotated_lower)
        #print(rotated_digits)
        #print(caesar_lookup)


        result = []
        for num in caesar_lookup:
            if num == ' ':
                result.append(' ')
            elif int(num) in rotated_lower.keys():
                result.append(rotated_lower[int(num)])
            elif int(num) in rotated_upper.keys():
                result.append(rotated_upper[int(num)])
            else:
                result.append(rotated_digits[int(num)])

        return ''.join(result) 

    def cytool_caesar(self, text, key, alphabet, b_encrypt, b_keep_chars, b_block_of_five) -> str:
        ciphertext = ""

        # iterate through text
        for old_character in text:
            new_character = ""
    
            # if character is in alphabet append to ciphertext
            if(old_character in alphabet):
                index = alphabet.index(old_character)
    
                if(b_encrypt):  # if text is to be encrypted
                    new_index = (index + key) % len(alphabet)
    
                else:  # if text is to be decrypted
                    new_index = (index - key) % len(alphabet)
    
                new_character = alphabet[new_index]
    
            else:
    
                # if the symbol is not in alphabet then regard block_of_five and b_encrypt
                if(not b_keep_chars):
                    continue
                else:
                    if(b_block_of_five and b_encrypt):
                        if(old_character != " "):
                            new_character = old_character
                        else:
                            continue
                    else:
                        new_character = old_character
    
            ciphertext = ciphertext + new_character
    
            # if blocks_of_five is true, append a space after every 5 characters
            if(b_block_of_five and b_encrypt):
                if(len(ciphertext.replace(" ", "")) % 5 == 0):
                    ciphertext = ciphertext + " "

        # Output
        return ciphertext

    def rot13(self) -> str: # Only supports lowercase letters
        return self.caesar_cipher(key = 14)
   
    def affine(self, key) -> str:
        inverted_alph = {v: k for k, v in self.alphabet.items()} #switch keys for values
        print(inverted_alph)
        result = ""
        for c in self.org_msg:
            index = self.alphabet[c]*key
            if index > (len(inverted_alph)):
                index = index%len(inverted_alph)

            result += inverted_alph[index]
            print(result)

    def rail_line(self) -> str:
        ...

#only for local quick debugging purposes
def main(): #gets ImportError for relative import...
    #en = Encoder(message = "TheQuickBrownFoxJumpsOverTheLazyDog", algo = "affine", key = 5)
    ...

if __name__ == "__main__":
    main()

    #performance testing, cProfile, time, and pstats
        #import cProfile
        #import pstats
        #from io import StringIO
        #import time

        #en = Encoder()
        #print(en.caesar_cipher())
        #print(en.cytool_caesar(text='abcdefghijklmnopqrst', key=4, alphabet='abcdefghijklmnopqrstuvwxyz', b_encrypt=True, b_keep_chars=False, b_block_of_five=False))
    
        #profiler = cProfile.Profile()
        #start_time = time.perf_counter_ns()
        #profiler.enable()
        #en.caesar_cipher()
        #profiler.disable()
        #end_time = time.perf_counter_ns()
    
        #s = StringIO()
        #stats = pstats.Stats(profiler, stream=s)
        #stats.strip_dirs().sort_stats("cumulative").print_stats(10)
        #print(s.getvalue())
    
        #print(f'{"":<25}My Caesar execution time: {end_time - start_time}: nanoseconds')
        #print("-"*50)
    
        #profiler = cProfile.Profile()
        #start_time = time.perf_counter_ns()
        #profiler.enable()
        #en.cytool_caesar(text='abcdefghijklmnopqrst', key=4, alphabet='abcdefghijklmnopqrstuvwxyz', b_encrypt=True, b_keep_chars=False, b_block_of_five=False)
        #profiler.disable()
        #end_time = time.perf_counter_ns()
    
        #print(f'{"":<25}Cryptool Caesar execution time: {end_time - start_time}: nanoseconds')
    
        #s = StringIO()
        #stats = pstats.Stats(profiler, stream=s)
        #stats.strip_dirs().sort_stats("cumulative").print_stats(10)
        #print(s.getvalue())
