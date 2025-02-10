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
    assert "Alphabet" not in default_encoder.info()

@pytest.mark.unit
def test_encoder_info_alphabet(default_encoder):
    assert type(default_encoder.info(alf=True)) is str
    assert "Alphabet" in default_encoder.info(alf=True)

@pytest.mark.unit
def test_run_encryption(default_encoder):
    assert default_encoder.run_encryption()
    assert default_encoder.run_encryption(kwargs={"algo": "scytale", "radius": 4})
    assert default_encoder.run_encryption(kwargs={"algo": "rot13"})
    
@pytest.mark.unit
@pytest.mark.benchmark()
def test_caesar_encode(benchmark):
    en = Encoder(algo="caesar_cipher", message="abcdefghijklmnopqrst", key=4)
    result = benchmark(en.caesar_cipher)
    assert result == 'efghijklmnopqrstuvwx'