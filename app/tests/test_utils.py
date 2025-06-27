import pytest
from src.utils import is_even

def test_is_even():
    assert is_even(2)
    assert not is_even(3)
    assert is_even(0)
