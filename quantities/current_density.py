from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .electric_current import ElectriCurrentType
from .area import AreaType

class ampere_per_square_meter(Unit):
    profile = {
        "name":"ampere per square meter",
        "symbol":"",
        "express_by_SI_base":"A*m-2",
        "express_by_SI":""
    }
class CurrentDensityType(QuantityType):
    pri_unit = ampere_per_square_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ElectriCurrentType, '/', AreaType)] = cls
        cls.source[(cls, '*', AreaType)] = ElectriCurrentType
        cls.source[(AreaType, '*', cls)] = ElectriCurrentType
        cls.source[(ElectriCurrentType, '/', cls)] = AreaType

class CurrentDensity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, CurrentDensityType, unit)