'''
The capacitance C is the ratio of the amount of charge q 
on either conductor to the potential difference V between the conductors.
'''
from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .electric_charge import ElectriChargeType
from .electric_potential_difference import ElectricPotentialDifferenceType

class farad(Unit):
    profile = {
        "name":"farad",
        "symbol":"F",
        "express_by_SI_base":"kg-1*m-2*s+4*A",
        "express_by_SI":"C/V"
    }
class CapacitanceType(QuantityType):
    pri_unit = farad
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ElectriChargeType, '/', ElectricPotentialDifferenceType)] = cls
        cls.source[(cls, '*', ElectricPotentialDifferenceType)] = ElectriChargeType
        cls.source[(ElectricPotentialDifferenceType, '*', cls)] = ElectriChargeType
        cls.source[(ElectriChargeType, '/', cls)] = ElectricPotentialDifferenceType

class Capacitance(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, CapacitanceType, unit)