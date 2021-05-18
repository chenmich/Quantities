from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .heat_capacity import HeatCapacityType
from .mass import MassType

class joule_per_kilogram_kelvin(Unit):
    profile = {   
        "name":"joule per kilogram kelvin",
        "symbol":"J*K-1*kg-1",
        "express_by_SI_base":"m+2*s-2*K-1",
        "express_by_SI":""
    }

class SpecificHeatCapacityType(QuantityType):
    pri_unit = joule_per_kilogram_kelvin
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(HeatCapacityType, '/', MassType)] = cls
        cls.source[(cls, '*', MassType)] = HeatCapacityType
        cls.source[(MassType, '*', cls)] = HeatCapacityType
        cls.source[(HeatCapacityType, '/', cls)] = MassType
class SpecificHeatCapacity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, SpecificHeatCapacityType, unit)