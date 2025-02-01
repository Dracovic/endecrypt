import string

class Coder:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    """ A Coder class to abstract manage and not repeat attributes both the Encoder and Decoder classes
        will have in common. Also will manage files and command-line inputs.
    """

    def __init__(self, **kwargs):
        self.std_alphabet = dict([*zip(list(string.ascii_letters + string.digits), range(62))])
        if kwargs:
            if kwargs["message"]:
                self.msg = kwargs["message"]
            elif kwargs["input"][:-4] == ".txt":
                self.input = kwargs["input"]
            if hasattr(self, kwargs["algo"]):
                self.algo = getattr(self, kwargs["algo"])
                if callable(self.algo):
                    if kwargs["algo"] == "scytale":
                        self.enc_msg = self.algo(kwargs["radius"])
                    else:
                        self.enc_msg = self.algo()
        else: #No arguments passed programatically
            self.msg = "abcdefghijklmnopqrst"
            self.algo = "scytale"
=======
=======
    """ A Coder class to abstract manage and not repeat attributes both the Encoder and Decoder classes
        will have in common. Also will manage files and command-line inputs.
    """
>>>>>>> 28f9d6e (began major restructuring)

    def __init__(self, **kwargs):
        self.std_alphabet = dict([*zip(list(string.ascii_letters + string.digits), range(62))])
<<<<<<< HEAD
>>>>>>> 852295f (Created Coder Parent Class to abstract the argument passing from cmdline into both obj instancing without repeating code. Also generating the alphabet to be used for either class)
=======
=======
    """ A Coder class to abstract manage and not repeat attributes both the Encoder and Decoder classes
        will have in common. Also will manage files and command-line inputs.
    """
>>>>>>> 28f9d6e (began major restructuring)

    def __init__(self, **kwargs):
        self.std_alphabet = dict([*zip(list(string.ascii_letters + string.digits), range(62))])
<<<<<<< HEAD
>>>>>>> 852295f (Created Coder Parent Class to abstract the argument passing from cmdline into both obj instancing without repeating code. Also generating the alphabet to be used for either class)
=======
=======
>>>>>>> 28f9d6e (began major restructuring)
        if kwargs:
            if kwargs["message"]:
                self.msg = kwargs["message"]
            elif kwargs["input"][:-4] == ".txt":
                self.input = kwargs["input"]
            if hasattr(self, kwargs["algo"]):
                self.algo = getattr(self, kwargs["algo"])
                if callable(self.algo):
                    if kwargs["algo"] == "scytale":
                        self.enc_msg = self.algo(kwargs["radius"])
                    else:
                        self.enc_msg = self.algo()
        else: #No arguments passed programatically
            self.msg = "abcdefghijklmnopqrst"
            self.algo = "scytale"
<<<<<<< HEAD
>>>>>>> 28f9d6e (began major restructuring)
=======
>>>>>>> 28f9d6e (began major restructuring)

co = Coder()
print(co.std_alphabet)