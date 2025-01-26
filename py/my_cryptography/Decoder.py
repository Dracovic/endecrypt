class Decoder:
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
        self.enc_msg = kwargs['message']
        if hasattr(self, kwargs['algo']):
            self.algo = getattr(self, kwargs['algo'])
            if callable(self.algo):
                if kwargs["algo"] == "scytale":
                    self.dec_msg = self.algo(kwargs["radius"])
                else:
                    self.dec_msg = self.algo()

    def scytale(self, r: int = 5) -> str:
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

