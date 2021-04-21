from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .area import AreaType
from .mass import MassType

class kilogram_per_square_meter(Unit):
    profile = {
        "name":"kilogram per square meter",
        "symbol":"",
        "express_by_SI_base":"kg*m-2",
        "express_by_SI":""
    }

class SurfaceDensityType(QuantityType):
    pri_unit = kilogram_per_square_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(MassType, '/', AreaType)] = cls
        cls.source[(AreaType, '*', cls)] = MassType
        cls.source[(cls, '*', AreaType)] = MassType
        cls.source[(MassType, '/', cls)] = AreaType

class SurfaceDensity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, SurfaceDensityType, unit)