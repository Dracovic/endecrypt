import string

class Coder:

    def __init__(self):
        self.std_alphabet = dict([*zip(list(string.ascii_letters + string.digits), range(62))])

co = Coder()
print(co.std_alphabet)