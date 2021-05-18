from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .radial_length import RadialLengthType
from .force import ForceType

class newton_meter(Unit):
    profile = {   
        "name":"newton meter",
        "symbol":"N*m",
        "express_by_SI_base":"kg*m+2*s-2",
        "express_by_SI":""
    }

class MomentOfForceType(QuantityType):
    pri_unit = newton_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ForceType, '*', RadialLengthType)] = cls
        cls.source[(RadialLengthType, '*', ForceType)] = cls
        cls.source[(cls, '/', RadialLengthType)] = ForceType
        cls.source[(cls, '/', ForceType)] = RadialLengthType

class MomentOfForce(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, MomentOfForceType, unit)