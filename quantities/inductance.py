from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit

class henry(Unit):
    profile = {
        "name":"henry",
        "symbol":"H",
        "express_by_SI_base":"kg*m+2*s-2*A-2",
        "express_by_SI":"Wb/A"
    }
class InductanceType(QuantityType):
    pri_unit = henry
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        pass

class Inductance(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, InductanceType, unit)