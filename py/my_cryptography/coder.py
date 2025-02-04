from argparse import ArgumentError
from pathlib import Path
import string

class Coder:
    """An Coder tool to (en/de)crypt messages using various algorithms.

        An Coder is an Object that is created with a specified alphabet, algorithm,
        message, input file, and output file as parameters.

        This Coder class abstracts and manages attributes for both the Encoder and Decoder classes
        that they will have in common. Also will manage files and command-line inputs.

            Attributes:
                alphabet: dict - the alphabet to be used for (en/de)crypted.
                    Defaults to all ascii letters and digits using the -al --alphabet argument.
                org_msg: str - the original message to be (en/de)crypted.
                algo: str - the algorithm used to (en/de)crypted the message.
                (optional)
                input_file: str - the file to be (en/de)crypted.
                output_file: str - the (en/de)crypted file to be written or written to.
    """

    def __init__(self, **kwargs):

        if kwargs: # everything that is to be done if there are args passed by command-line
            if "alphabet" in kwargs: # user may define their own alphabet
                self.alphabet = self.generate_alphabet(kwargs["alphabet"])
            else:
                self.alphabet = self.generate_alphabet()

            if "message" in kwargs: # user defined message
                self.org_msg = kwargs["message"]
            elif "input" in kwargs: # user defined file for input
                self.input_file = kwargs["input"]
            else:
                self.org_msg = "abcdefghijklmnopqrst"

        else: #No arguments passed programatically, adds default values
            self.org_msg = "abcdefghijklmnopqrst"
            self.alphabet = self.generate_alphabet()

    def info(self):
        """Prints the attributes of the Coder object."""
        #print(f"Alphabet: {self.alphabet}") DEPRECATED
        #TODO: print(f'Input File:{self.input}')
        #TODO: print(f'Output File: {self.output}')

    def generate_alphabet(self, additions: str = "") -> dict:
        self.alphabet = dict([*zip(list(string.ascii_letters + string.digits), range(1,62))])
        user_defined = [*zip([c for c in additions if c not in self.alphabet], range(63, 63+len(additions)))]
        for k, v in user_defined:
            self.alphabet[k] = v
        self.alphabet[" "] = len(self.alphabet)+1
        self.alphabet["-"] = len(self.alphabet)+1
        return self.alphabet

    def validate_input_file(self, input_arg: str) -> bool:
        """This function validates the name of the input file set in the command line using the -o flag
        
            Arguments:
                input_arg: str - name of the file, comes from parser
            
            Returns:
                True: bool - validataion either passes and returns True or fails and raises an Error.
        """
        try:
            if input_arg[:-4] != '.txt':
                raise ArgumentError(f'{input_arg} does not have a valid file termination')
        finally:
            return True
    
    def validate_output_file(self, output_arg: str) -> bool:
        """This function validates the name of the output file set in the command line using the -o flag
        
            Arguments:
                output_arg: str - name of the file, comes from parser
            
            Returns:
                True: bool - validataion either passes and returns True or fails and raises an Error.
        """
        try:
            if output_arg[:-4] != '.txt':
                raise ArgumentError(f'{output_arg} does not have a valid file termination')
        finally:
            return True
    
    def _validate_algo(self, algo: str) -> bool: # should only be called by child classes
        """This function checks the Coder class and makes sure that the algorithm is programmed into the Encoder or Decoder classes
    
            Arguments:
                en_or_de: bool - True if it's encryption, False if it's decryption
                algo_arg: str - name of the Algorithm to validate the existence of
    
            Returns:
                True: bool  - validation either passes and returns True or fails and raises an Error.
        """
        if hasattr(self, algo): # self always refers to the object instantiated, here the Child calling it
            self.algo = getattr(self, algo)
            if callable(self.algo):
                return True
            else:
                raise ArgumentError(f'{algo} is not an existing supported algorithm.')
                return False
        else:
                raise ArgumentError(f'{algo} is not an existing supported algorithm.')
                return False


#co = Coder()
#co = Coder(alphabet="abcd!@#$%^&*()_+=-")
#print(co.alphabet)