import unittest
import pytest

import my_cryptography as mc


class test_Encoder(unittest.TestCase):
    def setUp(self):
        print("Setting up Encoder test...")
        self.test1 = mc.Encoder()
        
    def test_scytale_encoder(self):
        #self.assertIsInstance(self.test1, mc.Encoder) #Sanity Check
        
        ################# No params Test #################
        self.assertEquals(self.test1.algo, getattr(self.test1, "scytale"))
        self.assertEquals(self.test1.org_msg, "abcdefghijklmnopqrst")
        self.assertEquals(self.test1.enc_msg, "afkpbglqchmrdinsejot")
        ################# r = 1 edge case Test #################
        self.test1.enc_msg = self.test1.algo(r = 1)
        self.assertEquals(self.test1.enc_msg, "abcdefghijklmnopqrst")
        ################# r = 2 Test #################
        self.test1.enc_msg = self.test1.algo(r = 2)
        self.assertEquals(self.test1.enc_msg, "akblcmdneofpgqhrisjt")
        ################# r = 3 Test #################
        self.test1.enc_msg = self.test1.algo(r = 3)
        self.assertEquals(self.test1.enc_msg, "ahobipcjqdkrelsfmtgn")

        ################# 1 - 100 Test #################
        for i in range(1, 20):
            self.test1.enc_msg = self.test1.algo(r = i)
            assert isinstance(self.test1.enc_msg, str)

    def tearDown(self):
        print('Tearing down Encoder test...')
        del self.test1


class test_Decoder(unittest.TestCase):
    def setUp(self):
        print("Setting up Decoder test...")
        self.encoder = mc.Encoder()
        self.test1 = mc.Decoder()
        
    def test_scytale_decoder(self):
        #self.assertIsInstance(self.test1, mc.Decoder) #Sanity Check
        
        ################# No params Test #################
        self.encoder.enc_msg = self.encoder.algo() # Default r = 4
        self.test1.dec_msg = self.test1.algo() # Default r = 4
        self.assertEqual(self.encoder.org_msg, self.test1.dec_msg)
        ################# r = 1 edge case Test #################
        self.encoder.enc_msg = self.encoder.algo(r = 1)
        self.test1.enc_msg = self.encoder.enc_msg
        self.test1.dec_msg = self.test1.algo(r = 1)
        self.assertEqual(self.encoder.org_msg, self.test1.dec_msg)
        ################# r = 2 Test #################
        self.encoder.enc_msg = self.encoder.algo(r = 2)
        self.test1.enc_msg = self.encoder.enc_msg
        self.test1.dec_msg = self.test1.algo(r = 2)
        self.assertEqual(self.encoder.org_msg, self.test1.dec_msg)
        ################# r = 3 Test #################
        self.encoder.enc_msg = self.encoder.algo(r = 3)
        self.test1.enc_msg = self.encoder.enc_msg
        self.test1.dec_msg = self.test1.algo(r = 3)
        self.assertEqual(self.encoder.org_msg, self.test1.dec_msg)

        ################# 1 - 100 Test #################
        for i in range(1, 20):
            self.encoder.enc_msg = self.encoder.algo(r = i)      # set encoder encrypted message with each changin radius
            self.test1.enc_msg = self.encoder.enc_msg            # set decoder encrypted message to the one generated above
            self.test1.dec_msg = self.test1.algo(r = i)          # decode the encrypted message using the same 'key' (radius)
            assert self.test1.dec_msg == self.encoder.org_msg    # assert the decoded message is the same as the original message from the encoder

    def tearDown(self):
        print('Tearing down Decoder test...')
        del self.test1

