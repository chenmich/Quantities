from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit

class m(Unit):
    profile = {
        "name":"meter",
        "symbol":"m", 
        "express_by_SI_base":"m", 
        "express_by_SI":"m"
    }

class yard(Unit):
    profile = {
        "name":"yard",
        "symbol":"yd", 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return 0.9144 * value
    @classmethod
    def from_pri_unit(cls, value):
        return 1.0936 * value

class inch(Unit):
    profile = {
        "name":"inch",
        "symbol":"inch", 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return 0.0254 * value
    @classmethod
    def from_pri_unit(cls, value):
        return  value / 0.0254

class foot(Unit):
    profile = {
        "name":"foot",
        "symbol":"ft", 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return 0.3048 * value
    @classmethod
    def from_pri_unit(cls, value):
        return value * 100 / 2.54 / 12

class mile(Unit):
    profile = {
        "name":"mile",
        "symbol":"mile", 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return 1609.34 * value
    @classmethod
    def from_pri_unit(cls, value):
        return value / 1609.34
class astronomical_unit(Unit):
    profile = {
        "name":"astronomical unit",
        "symbol":"au", 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return  value *149597870700
    @classmethod
    def from_pri_unit(cls, value):
        return value / 149597870700
class LengthType(QuantityType):
    pri_unit = m
    SI_conherent_unit = pri_unit
    foot = foot
    inch = inch
    yard = yard
    mile = mile
    astronomical_unit = astronomical_unit
    @classmethod
    def register_type(cls):
        pass

class Length(Quantity):
    def __init__(self, value:float, unit=None):
        super().__init__(value, LengthType, unit)