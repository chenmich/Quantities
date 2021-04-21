from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .power import PowerType
from .area import AreaType

class watt_per_square_metre(Unit):
    profile = {   
        "name":"watt per square metre",
        "symbol":"W*m-2",
        "express_by_SI_base":"kg*s-3",
        "express_by_SI":""
    }

class HeatFluxDensityType(QuantityType):
    pri_unit = watt_per_square_metre
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(PowerType, '/', AreaType)] = cls
        cls.source[(cls, '*', AreaType)] = PowerType
        cls.source[(AreaType, '*', cls)] = PowerType
        cls.source[(PowerType, '/', cls)] = AreaType

class HeatFluxDensity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, HeatFluxDensityType, unit)