import pytest
from my_cryptography import Encoder

pytest.mark.unit
def test_encoder_default_instantiation():
    en = Encoder()
    assert en.org_msg == "abcdefghijklmnopqrst"
    assert en.enc_msg == "opqrstuvwxyzabcdefgh"
    assert en.algo.__name__ == "rot13"

@pytest.mark.unit
def test_caesar_encode(benchmark):
    en = mc.Encoder(algo="caesar_cipher", message="abcdefghijklmnopqrst", key=4)
    result = benchmark(en.caesar_cipher)
    assert result == 'efghijklmnopqrstuvwx'