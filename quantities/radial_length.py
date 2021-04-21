
from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .length import m

class radial_m(m):
    pass
class RadialLengthType(QuantityType):
    pri_unit = radial_m
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        pass

class RadialLength(Quantity):
    def __init__(self, value:float, unit=None):
        super().__init__(value, RadialLengthType, unit)