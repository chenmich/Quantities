from . import quantity_type
from . import units
from . import length
from . import time
from . import quantity

class m_per_s(units.Unit):
    pass

class VelocityType(quantity_type.QuantityType):
    pri_unit = m_per_s
    SI_conherent_unit = pri_unit
    @classmethod
    def regist_type(cls):
        cls.source[(length.LengthType, '/', time.TimeType)] = cls
        cls.source[(cls, '*', time.TimeType)] = length.LengthType
        cls.source[(time.TimeType, '*', cls)] = length.LengthType
        cls.source[(length.LengthType, '/', cls )] = time.TimeType
class Velocity(quantity.Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, VelocityType, unit)
        