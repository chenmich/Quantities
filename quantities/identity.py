from . quantity_type import QuantityType
from . units import Unit
from . quantity import Quantity


class IdentityUnit(Unit):
    profile = {
        "name":"IdentityUnit",
        "symbol":"Identity",
        "express_by_SI_base":"", 
        "express_by_SI":""
    }

class IdentityType(QuantityType):
    pri_unit = IdentityUnit
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        pass

class Identity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, IdentityType, unit)