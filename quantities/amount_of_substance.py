from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit

class mole(Unit):
    profile = {
        "name":"mole",
        "symbol":"mole",
        "express_by_SI_base":"mole", 
        "express_by_SI":"mole"
    }

class AmountOfSubstanceType(QuantityType):
    pri_unit = mole
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        pass

class AmountOfSubstance(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, AmountOfSubstanceType, unit)