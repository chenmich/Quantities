'''
All the classes are for power and radiant flux quantity
'''
from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .energy import EnergyType
from .time import TimeType

class watt(Unit):
    profile = {
        "name":"watt",
        "symbol":"W",
        "express_by_SI_base":"kg*m+2*s-3",
        "express_by_SI":"J/s"
    }

class PowerType(QuantityType):
    pri_unit = watt
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(EnergyType, '/', TimeType)] = cls
        cls.source[(cls, '*', TimeType)] = EnergyType
        cls.source[(TimeType, '*', cls)] = EnergyType

class Power(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, PowerType, unit)