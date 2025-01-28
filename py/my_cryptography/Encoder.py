import string
import numpy as np

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
    
en = Encoder()
print(en.polybius_square())