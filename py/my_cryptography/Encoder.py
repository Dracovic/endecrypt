import string
import numpy as np
import cProfile
import pstats
from io import StringIO
import time
import timeit

class Encoder:
    """An Encoder is an Object that is created with a specified algorithm as a parameter
       as well as an optional message to encode on creation."""

    def __init__(self, **kwargs):
        """ The Encoder class is initialized with a message and an algorithm to encode the message.

            Attributes:
                org_msg: str - the original message to be encoded.
                algo: str - the algorithm to encode the message.
                enc_msg: str - the encoded message.

            Examples:
                scy_enc = Encoder(algo = 'scytale', message = '0123456789abcdefghij', radius = 4)
                print(scy_enc.enc_msg)
                >> 05af16bg27ch38di49ej
        """
        if kwargs:
            self.org_msg = kwargs["message"]
            if hasattr(self, kwargs["algo"]):
                self.algo = getattr(self, kwargs["algo"])
                if callable(self.algo):
                    if kwargs["algo"] == "scytale":
                        self.enc_msg = self.algo(kwargs["radius"])
                    else:
                        self.enc_msg = self.algo()
        else: #No arguments passed programatically
            self.org_msg = "abcdefghijklmnopqrst"
            self.algo = getattr(self, "scytale")
            self.enc_msg = self.algo()

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
        lower = [*zip(string.ascii_lowercase, reversed(string.ascii_lowercase))] # pair list of the lower case alphabet with it's pair in reverse order
        upper = [*zip(string.ascii_uppercase, reversed(string.ascii_uppercase))] # pair list of the upper case alphabet with it's pair in reverse order
        nums = [*zip(string.digits, reversed(string.digits))] # pair list of the digits with it's pair in reverse order

        alphabet = dict(lower + upper + nums) # hashmap of all letters and digits with corresponding opposites for quick lookup

        result = ''.join([alphabet[self.org_msg[self.org_msg.index(c)]] for c in self.org_msg])
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
    #performance testing, cProfile, time, and pstats
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

    def rot13(self) -> str: # Only supports lowercase letters
        return self.caesar_cipher(key = 14)
   
    def affine() -> str:
        ...

en = Encoder(message="abcdefghijlkmnopqrst", algo="rot13")
print(en.enc_msg)