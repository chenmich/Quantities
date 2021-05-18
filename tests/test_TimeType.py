import pytest
from quantities import time

def test_time_creation():
    assert time.TimeType.pri_unit == time.s
    assert time.TimeType.SI_conherent_unit == time.s
