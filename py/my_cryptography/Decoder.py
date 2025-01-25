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
                self.dec_msg = self.algo(kwargs['radius'])

    def scytale(self, r: int = 5) -> str:
        r += 1
        enc_msg_len = len(self.enc_msg) - 1
        result = ""
        i = 0
        index = 0
        t = 0
        while(len(result) <= enc_msg_len):
            if index > enc_msg_len:
                t = index - enc_msg_len
                i = 0
                index = r*i+t
            result = result + self.enc_msg[index]
            i += 1
            index = r*i + t
        return result

