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
        self.org_msg = kwargs["message"]
        if hasattr(self, kwargs["algo"]):
            self.algo = getattr(self, kwargs["algo"])
            if callable(self.algo):
                self.enc_msg = self.algo(kwargs["radius"])

    def scytale(self, r: int = 5) -> str:
        """ Scytale is a simple transposition cipher used in ancient Greece. I imagine it as a regular prism
            of a certain number of faces. The number of faces is the key to the cipher. The message is written
            on the prism and then read off in a spiral fashion.
            
            Attributes:
                r: int - the number of faces on the prism.
                
            Returns:
                result: str - the encoded message.
        """
        msg_len = len(self.org_msg) - 1
        result = '' # Initialize the result string (empty)
        r += 1      # The number of faces on the prism + 1 to have the correct next character in the string        msg_len = len(self.org_msg) - 1
        i = 0       # Counter for the loop
        t = 0       # This variable is used to control the overflow of the index when it wraps back around
        index = 0   # The actual variable used to index the orginal message and extract the character in turn
        while(len(result) <= msg_len):    # Loop until the result string is the same length as the original message
            if index > msg_len:           # If the index is greater than the length of the original message it would overflow, so this resets it
                t = index - msg_len       # This calculates where it should start on the next pass
                i = 0                     # Reset the counter
                index = r*i+t             # Restart the extraction from the new beginning
            result = result + self.org_msg[index] # Extracts the character from the original message and adds it to the result string
            i += 1                                # Increment the counter
            index = r*i+t                         # Calculate the next index to extract the character from the original message
        return result

