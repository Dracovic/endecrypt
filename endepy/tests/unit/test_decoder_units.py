import pytest
from my_cryptography import Decoder

@pytest.mark.unit
def test_decoder_default_instantiation():
    de = Decoder()
    assert de.enc_msg == "opqrstuvwxyzabcdefgh"
    assert de.dec_msg == "abcdefghijklmnopqrst"
    assert de.algo.__name__ == "rot13"