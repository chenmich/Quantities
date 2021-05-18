'''
All the classes Quantity, QuantityType and joule is 
for energy, work and amount of heat
'''

from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .force import ForceType, N
from .length import LengthType, m

class joule(Unit):
    profile = {
        "name":"joule",
        "symbol":"J",
        "express_by_SI_base":"kg*m+2*s-2",
        "express_by_SI":"N*m"
    }
class electronvolt(Unit):
    profile = {
        "name":"electronvolt",
        "symbol":"eV",
        "express_by_SI_base":"",
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return value * 1.602176634e-19
    @classmethod
    def from_pri_unit(cls, value):
        return value / 1.602176634e-19

class EnergyType(QuantityType):
    pri_unit = joule
    SI_conherent_unit = pri_unit
    electronvolt = electronvolt
    @classmethod
    def register_type(cls):
        cls.source[(ForceType, '*', LengthType)] = cls
        cls.source[(LengthType, '*', ForceType)] = cls
        cls.source[(cls, '/', ForceType)] = LengthType
        cls.source[(cls, '/', LengthType)] = ForceType

class Energy(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, EnergyType, unit)