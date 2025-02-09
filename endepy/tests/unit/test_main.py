import pytest
import sys
from endepy import main

@pytest.mark.unit
def test_main(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main"])
    assert main.main() is None