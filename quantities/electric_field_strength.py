from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .length import LengthType
from .electric_potential_difference import ElectricPotentialDifferenceType

class volt_per_meter(Unit):
    profile = {   
        "name":"volt per  meter",
        "symbol":"V*m-1",
        "express_by_SI_base":"kg*m*s-3*A-1",
        "express_by_SI":""
    }

class ElectricFieldStrengthType(QuantityType):
    pri_unit = volt_per_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ElectricPotentialDifferenceType, '/', LengthType)] = cls
        cls.source[(cls, '*', LengthType)] = ElectricPotentialDifferenceType
        cls.source[(LengthType, '*', cls)] = ElectricPotentialDifferenceType
        cls.source[(ElectricPotentialDifferenceType, '/', cls)] = LengthType

class ElectricFieldStrength(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ElectricFieldStrengthType, unit)