import pytest
from quantities import length

def test_Length_creation():
    length.LengthType.pri_unit = length.m