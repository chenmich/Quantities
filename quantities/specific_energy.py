from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .energy import EnergyType
from .mass import MassType

class joule_per_kilogram(Unit):
    profile = {   
        "name":"joule per kilogram",
        "symbol":"J*kg-1",
        "express_by_SI_base":"m+2*s-2",
        "express_by_SI":""
    }

class SpecificEnergyType(QuantityType):
    pri_unit = joule_per_kilogram
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(EnergyType, '/', MassType)] = cls
        cls.source[(cls, '*', MassType)] = EnergyType
        cls.source[(MassType, '*', cls)] = EnergyType
        cls.source[(EnergyType, '/', cls)] = MassType

class SpecificEnergy(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, SpecificEnergyType, unit)