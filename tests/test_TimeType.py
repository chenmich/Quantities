import pytest
from quantities import time

def test_time_creation():
    time.TimeType.pri_unit = time.s
    time.TimeType.SI_conherent_unit = time.s
