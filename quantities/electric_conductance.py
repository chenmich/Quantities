from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .electric_potential_difference import ElectricPotentialDifferenceType
from .electric_current import ElectriCurrentType
from .electric_resistance import ElectricResistanceType
from .identity import IdentityType

class siemens(Unit):
    profile = {
        "name":"ohm",
        "symbol":"S",
        "express_by_SI_base":"kg-1*m-2*s+3*A+2",
        "express_by_SI":"A/V"
    }

class ElectricConductanceType(QuantityType):
    pri_unit = siemens
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ElectriCurrentType, '/', ElectricPotentialDifferenceType)] = cls
        cls.source[(cls, '*', ElectricPotentialDifferenceType)] = ElectriCurrentType
        cls.source[(ElectricPotentialDifferenceType, '*', cls)] = ElectriCurrentType
        cls.source[(ElectriCurrentType, '/', cls)] = ElectricPotentialDifferenceType
        cls.source[(IdentityType, '/', cls)] = ElectricResistanceType
        cls.source[(IdentityType, '/', ElectricResistanceType)] = cls


class ElectricConductance(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ElectricConductanceType, unit)
