from .quantity_type import QuantityType
from .quantity import Quantity

from .units import Unit

class s(Unit):
    profile = {
        "name":"second", 
        "symbol":"s", 
        "express_by_SI_base":"s",
        "express_by_SI":"s"
    }
class minute(Unit):
    profile = {
        "name":"minute", 
        "symbol":"min", 
        "express_by_SI_base":"",
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return 60 * value
    @classmethod
    def from_pri_unit(cls, value):
        return value / 60
class hour(Unit):
    profile = {
        "name":"hour", 
        "symbol":"h", 
        "express_by_SI_base":"",
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return 3600 * value
    @classmethod
    def from_pri_unit(cls, value):
        return value / 3600
class day(Unit):
    profile = {
        "name":"day", 
        "symbol":"d", 
        "express_by_SI_base":"",
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return 24 * 3600 * value
    @classmethod
    def from_pri_unit(cls, value):
        return value / (24 * 3600)


class TimeType(QuantityType):
    pri_unit = s
    SI_conherent_unit = pri_unit
    minute = minute
    hour = hour
    day = day
    @classmethod
    def register_type(cls):
        pass

class Time(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, TimeType, unit)
