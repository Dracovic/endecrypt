import pytest
from ....py import my_cryptography as mc


@pytest.mark.benchmark(group="performance")
def test_caesar_encode(benchmark):
    en = mc.Encoder(algo="caesar_cipher", message="abcdefghijklmnopqrst", key=4)
    result = benchmark(en.caesar_cipher)
    assert result == 'efghijklmnopqrstuvwx'