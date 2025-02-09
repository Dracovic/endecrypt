import pytest
from my_cryptography import Encoder

@pytest.fixture
@pytest.mark.unit
def default_encoder():
    en = Encoder()
    return en

@pytest.mark.unit
def test_encoder_info(default_encoder):
    assert type(default_encoder.info()) is str

@pytest.mark.unit
def test_encoder_info_alphabet(default_encoder):
    assert type(default_encoder.info(alf=True)) is str
    
@pytest.mark.unit
@pytest.mark.benchmark()
def test_caesar_encode(benchmark):
    en = Encoder(algo="caesar_cipher", message="abcdefghijklmnopqrst", key=4)
    result = benchmark(en.caesar_cipher)
    assert result == 'efghijklmnopqrstuvwx'