from . import quantity_type
from . import units
from . import length
from . import time

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