import unittest
import pytest

import my_cryptography as mc


class test_Encoder(unittest.TestCase):
    def setUp(self):
        test1 = my_cryptography.Encoder()
        #test2 = my_cryptography.Encoder()
        #test3 = my_cryptography.Encoder()
        
    def test_scytale(self):
        print(test1)
        #assert test1.scytale(message = 'abcdefghijklmnopqrst') == 'ahobipcjqdkrelsfmtgn'
        #assert test1.scytale(algo = 'scytale', message = '01234567891112131415161718192021222324') == '0516273849'


    def tearDown(self):
        del test1