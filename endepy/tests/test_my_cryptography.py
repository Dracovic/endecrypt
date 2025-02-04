import unittest
import pytest
import time
import my_cryptography as mc

class test_Encoder(unittest.TestCase):
    def setUp(self):
        print("Setting up Encoder test...")
        self.scytale = mc.Encoder(algo="scytale", message="abcdefghijklmnopqrst", radius =4)
        
    def test_scytale_encoder(self):
        #self.assertIsInstance(self.test1, mc.Encoder) #Sanity Check
        
        ################# No params Test #################
        self.assertEqual(self.scytale.algo, getattr(self.scytale, "scytale"))
        #self.assertEqual(self.test1.org_msg, "abcdefghijklmnopqrst")
        #self.assertEqual(self.test1.enc_msg, "afkpbglqchmrdinsejot")
        ################# r = 1 edge case Test #################
        #self.test1.enc_msg = self.test1.algo(r = 1)
        #self.assertEqual(self.test1.enc_msg, "abcdefghijklmnopqrst")
        ################# r = 2 Test #################
        #self.test1.enc_msg = self.test1.algo(r = 2)
        #self.assertEqual(self.test1.enc_msg, "akblcmdneofpgqhrisjt")
        ################# r = 3 Test #################
        #self.test1.enc_msg = self.test1.algo(r = 3)
        #self.assertEqual(self.test1.enc_msg, "ahobipcjqdkrelsfmtgn")

        ################# 1 - 100 Test #################
        #for i in range(1, 20):
            #self.test1.enc_msg = self.test1.algo(r = i)
            #assert isinstance(self.test1.enc_msg, str)

    def test_atbash_encoder(self):
        self.test1.algo = getattr(self.test1, "atbash")
        self.assertEqual(self.test1.algo, getattr(self.test1, "atbash"))
        ################# lowercase Test #################
        self.assertEqual(self.test1.org_msg, "abcdefghijklmnopqrst")
        self.test1.enc_msg = self.test1.algo()
        self.assertEqual(self.test1.enc_msg, "zyxwvutsrqponmlkjihg")
        ################# uppercase Test #################
        self.test1.org_msg = "ABCDEFGHIJKLMNOPQRST"
        self.test1.enc_msg = self.test1.algo()
        self.assertEqual(self.test1.enc_msg, "ZYXWVUTSRQPONMLKJIHG")
        ################# full alphabet Test #################
        self.test1.org_msg = "AbCdEfGhIjKlMnOpQrSt"
        self.test1.enc_msg = self.test1.algo()
        self.assertEqual(self.test1.enc_msg, "ZyXwVuTsRqPoNmLkJiHg")
        ################# numeric Test #################
        self.test1.org_msg = "0123456789"
        self.test1.enc_msg = self.test1.algo()
        self.assertEqual(self.test1.enc_msg, "9876543210")
        ################# alphabet and numerics Test #################
        self.test1.org_msg = "Ab0Cd1Ef2Gh3Ij4Kl5Mn6Op7Qr8St9"
        self.test1.enc_msg = self.test1.algo()
        self.assertEqual(self.test1.enc_msg, "Zy9Xw8Vu7Ts6Rq5Po4Nm3Lk2Ji1Hg0")
 
    def test_polybius_square(self):
        self.test1.algo = getattr(self.test1, "polybius_square")
        self.test1.enc_msg = self.test1.algo()
        self.assertEqual(self.test1.enc_msg, "1112131415212223242425313233343541424344") # 24 twice bc i and j map to the same
    
    def test_rot13(self):
        self.assertEqual(self.test1.rot13(), self.test1.caesar_cipher(key=14))
   
    def tearDown(self):
        print('Tearing down Encoder test...')
        del self.scytale

@pytest.mark.benchmark(group="performance")
def test_caesar_encode(benchmark):
    en = mc.Encoder()
    result = benchmark(en.caesar_cipher)
    assert result == 'efghijklmnopqrstuvwx'

@pytest.mark.benchmark(group="performance")
def test_cytool_caesar(benchmark):
    en = mc.Encoder()
    result = benchmark(en.caesar_cipher)
    assert result == 'efghijklmnopqrstuvwx'
 

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

    def test_atbash_decoder(self):
        self.encoder.algo = getattr(self.encoder, "atbash")
        self.test1.algo = getattr(self.test1, "atbash")
        self.assertEqual(self.test1.algo, getattr(self.test1, "atbash"))
        ################# lowercase Test #################
        self.encoder.org_msg = "abcdefghijklmnopqrst"
        self.test1.enc_msg = self.encoder.algo()
        self.test1.dec_msg = self.test1.algo()
        self.assertEqual(self.test1.dec_msg, "abcdefghijklmnopqrst")
        ################# uppercase Test #################
        self.encoder.org_msg = "ABCDEFGHIJKLMNOPQRST"
        self.test1.enc_msg = self.encoder.algo()
        self.test1.dec_msg = self.test1.algo()
        self.assertEqual(self.test1.dec_msg, "ABCDEFGHIJKLMNOPQRST")
        ################# full alphabet Test #################
        self.encoder.org_msg = "AbCdEfGhIjKlMnOpQrSt"
        self.test1.enc_msg = self.encoder.algo()
        self.test1.dec_msg = self.test1.algo()
        self.assertEqual(self.test1.dec_msg, "AbCdEfGhIjKlMnOpQrSt")
        ################# numeric Test #################
        self.encoder.org_msg = "0123456789"
        self.test1.enc_msg = self.encoder.algo()
        self.test1.dec_msg = self.test1.algo()
        self.assertEqual(self.test1.dec_msg, "0123456789")
        ################# alphabet and numerics Test #################
        self.encoder.org_msg = "Ab0Cd1Ef2Gh3Ij4Kl5Mn6Op7Qr8St9"
        self.test1.enc_msg = self.encoder.algo()
        self.test1.dec_msg = self.test1.algo()
        self.assertEqual(self.test1.dec_msg, "Ab0Cd1Ef2Gh3Ij4Kl5Mn6Op7Qr8St9")

    def test_polybius_square(self):
        self.encoder.org_msg = 'abcdefghiiklmnopqrst'                # must be square so only 25 letters, j is i now
        self.encoder.algo = getattr(self.encoder, "polybius_square") # set encoder algo to polybius_square
        self.test1.algo = getattr(self.test1, "polybius_square")     # set decoder algo to polybius_square
        self.test1.enc_msg = self.encoder.algo()                     # set decoder encrypted msg to encoder's polybius_square encoding
        self.test1.dec_msg = self.test1.algo()                       # decode encoder's encrypted msg
        self.assertEqual(self.test1.dec_msg, self.encoder.org_msg)   # decoder's decrypted msg should match encoder's original mesg (24 twice bc i and j map to the same)
        
    def test_rot13(self):
        self.encoder.org_msg = 'abcdefghiiklmnopqrst'                # must be square so only 25 letters, j is i now
        self.encoder.algo = getattr(self.encoder, "rot13")           # set encoder algo to rot13 
        self.test1.algo = getattr(self.test1, "rot13")               # set decoder algo to rot13
        self.test1.enc_msg = self.encoder.algo()                     # set decoder encrypted msg to encoder's polybius_square encoding
        self.test1.dec_msg = self.test1.algo()                       # decode encoder's encrypted msg
        self.assertEqual(self.test1.dec_msg, self.encoder.org_msg)   # decoder's decrypted msg should match encoder's original mesg (24 twice bc i and j map to the same)
        
        
        
    def tearDown(self):
        print('Tearing down Decoder test...')
        del self.test1

@pytest.mark.benchmark(group="performance", timer=time.perf_counter_ns)
def test_caesar_decode(benchmark):
    en = mc.Encoder(message="abcdefghijklmnopqrst",algo="caesar_cipher")
    de = mc.Decoder(message=en.enc_msg, algo="caesar_cipher")
    result = benchmark(de.caesar_cipher)
    assert result == en.org_msg
