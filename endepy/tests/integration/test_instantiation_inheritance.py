import pytest
from my_cryptography import Decoder
from my_cryptography import Encoder

@pytest.mark.unit
def test_encoder_default_instantiation():
    en = Encoder()
    assert en.org_msg == "abcdefghijklmnopqrst"
    assert en.enc_msg == "opqrstuvwxyzabcdefgh"
    assert en.algo.__name__ == "rot13"


@pytest.mark.unit
def test_decoder_default_instantiation():
    de = Decoder()
    assert de.enc_msg == "opqrstuvwxyzabcdefgh"
    assert de.dec_msg == "abcdefghijklmnopqrst"
    assert de.algo.__name__ == "rot13"