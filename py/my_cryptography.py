class Encoder:
    """An Encoder is an Object that is created with a specified algorithm as a parameter
       as well as an optional message to encode on creation."""

    def __init__(self, **kwargs):
        self.org_msg = kwargs["message"]
        if hasattr(self, kwargs["algo"]):
            self.algo = getattr(self, kwargs["algo"])
            if callable(self.algo):
                self.enc_msg = self.algo()

    def scytale(self, r: int = 5) -> str:
        #print('Instantiation success!')
        msg_len = len(self.org_msg) - 1
        result = ''
        i = 0
        t = 0
        index = 0
        while(len(result) <= msg_len):
            if index > msg_len:
                t = index - msg_len
                i = 0
                index = r*i+t
            result = result + self.org_msg[index]
            i += 1
            index = r*i+t
        #print(result)
        return result


#scy = Encoder(algo = 'scytale', message = '01234567891011121314151617 vaccination')
#scy2 = Encoder(algo = 'scytale', message = 'active vaccination')
#scy3 = Encoder(algo = 'scytale', message = '0123456789')
#scy4 = Encoder(algo = 'scytale', message = '012345678901234567890123456789')
#print(scy2.enc_msg)
#print(scy3.enc_msg)
#print(scy4.enc_msg)

class Decoder:
    """A Decoder is an Object that is created with a specified algorithm as a parameter
       as well as an optional message to decode on creation."""

    def __init__(self,**kwargs):
        self.enc_msg = kwargs['message']
        if hasattr(self, kwargs['algo']):
            self.algo = getattr(kwargs['algo'])
            if callable(self.algo):
                self.dec_msg = self.algo()

    def scytale(self) -> str:
        result = ''
        return result


long = Encoder(algo = 'scytale', message = '01234567891011121314')
print('\n')
print(long.enc_msg)