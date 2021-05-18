from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .energy import EnergyType
from .thermodynamic_temperature import ThermodynamicTemperature

class joule_per_kelvin(Unit):
    profile = {   
        "name":"joule per kelvin",
        "symbol":"J*K-1",
        "express_by_SI_base":"kg*s-3",
        "express_by_SI":""
    }

class HeatCapacityType(QuantityType):
    pri_unit = joule_per_kelvin
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(EnergyType, '/', ThermodynamicTemperature)] = cls
        cls.source[(ThermodynamicTemperature, '*', cls)] = EnergyType
        cls.source[(cls, '*', ThermodynamicTemperature)] = EnergyType
        cls.source[(EnergyType, '/', cls)] = ThermodynamicTemperature
class HeatCapacity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, HeatCapacityType, unit)