from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .area import AreaType
from .force import ForceType

class newton_per_meter(Unit):
    profile = {
        "name":"newton per meter",
        "symbol":"N*m-1",
        "express_by_SI_base":"kg*m-1*s-1",
        "express_by_SI":""
    }

class SurfaceTensionType(QuantityType):
    pri_unit = newton_per_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ForceType, '/', AreaType)] = cls
        cls.source[(AreaType, '*', cls)] = ForceType
        cls.source[(cls, '*', AreaType)] = ForceType

class SurfaceTension(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, SurfaceTensionType, unit)