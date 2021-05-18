'''
The electrical resistance of a circuit is the ratio 
between the voltage applied to the current flowing through it.
'''

from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .electric_potential_difference import ElectricPotentialDifferenceType
from .electric_current import ElectriCurrentType

class ohm(Unit):
    profile = {
        "name":"ohm",
        "symbol":"Ω",
        "express_by_SI_base":"kg*m+2*s-3*A-2",
        "express_by_SI":"V/A"
    }

class ElectricResistanceType(QuantityType):
    pri_unit = ohm
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ElectricPotentialDifferenceType, '/', ElectriCurrentType)] = cls
        cls.source[(cls, '*', ElectriCurrentType)] = ElectricPotentialDifferenceType
        cls.source[(ElectriCurrentType, '*', cls)] = ElectricPotentialDifferenceType
class ElectricResistance(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ElectricResistanceType, unit)

