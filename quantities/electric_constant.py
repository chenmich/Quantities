from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .length import LengthType
from .capacitance import CapacitanceType

class farad_per_meter(Unit):
    profile = {   
        "name":"farad per meter",
        "symbol":"",
        "express_by_SI_base":"F*m-1",
        "express_by_SI":""
    }

class ElectricConstantType(QuantityType):
    pri_unit = farad_per_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(CapacitanceType, '/', LengthType)] = cls
        cls.source[(cls, '*', LengthType)] = CapacitanceType
        cls.source[(LengthType, '*', cls)] = CapacitanceType
        cls.source[(CapacitanceType, '/', cls)] = LengthType

class ElectricConstant(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ElectricConstantType, unit)
