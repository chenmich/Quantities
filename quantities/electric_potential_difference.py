'''
The electric potential is defined as capactity of charged body to do work.
This is the essence of the phsical quantity electric potential.
Here, we use this definition to design its QuantityType
'''
from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .energy import EnergyType
from .electric_charge import ElectriChargeType

class volt(Unit):
    profile = {
        "name":"volt",
        "symbol":"V",
        "express_by_SI_base":"kg*m+2*s-3*A-1",
        "express_by_SI":"W/A"
    }
class ElectricPotentialDifferenceType(QuantityType):
    pri_unit = volt
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(EnergyType, '/', ElectriChargeType)] = cls
        cls.source[(cls, '*', ElectriChargeType)] = EnergyType
        cls.source[(ElectriChargeType, '*', cls)] = EnergyType
        cls.source[(EnergyType, '/', cls)] = ElectriChargeType
class ElectricPotentialDifference(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ElectricPotentialDifferenceType, unit)