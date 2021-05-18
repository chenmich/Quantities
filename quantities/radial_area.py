from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .area import square_meter
from .radial_length import RadialLengthType

class radial_square_meter(square_meter):
    pass
class RadialAreaType(QuantityType):
    pri_unit = square_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(RadialLengthType, '*', RadialLengthType)] = cls
        cls.source[(cls, '/', RadialLengthType)] = RadialLengthType
class RadialArea(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, RadialAreaType, unit)
