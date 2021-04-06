import pytest
from quantities import length

def test_Length_creation():
    assert length.LengthType.pri_unit == length.m
    assert length.LengthType.SI_conherent_unit == length.LengthType.pri_unit