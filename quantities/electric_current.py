from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit

class A(Unit):
    profile = {
        "name":"ampere",
        "symbol":"A", 
        "express_by_SI_base":"A", 
        "express_by_SI":"A"
    }
class ElectriCurrentType(QuantityType):
    pri_unit = A
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        pass

class ElectriCurrent(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ElectriCurrentType, unit)