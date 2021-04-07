from .quantity_type import QuantityType
from .units import Unit

class Quantity():
    def __init__(self, value:float, q_type:QuantityType, unit=None):
        self.__value = value
        self.__type = q_type
        if unit != None:
            self.__unit = unit
        else:
            self.__unit = q_type.SI_conherent_unit
    def add(self, other):
        raise NotImplementedError
    def substract(self, other):
        raise NotImplementedError
    def multiply(self, other):
        raise NotImplementedError
    def divide(self, other):
        raise NotImplementedError
    def to_unit(self, unit:Unit):
        if unit not in self.q_type.__dict__.values() or unit == None:
            raise TypeError('The unit is not for this physical qunatity!')
        
        else:
            to_pri_coffic = self.current_unit.to_pri_unit()
            from_pri_coffic = unit.from_pri_unit()
            value = self.value * to_pri_coffic * from_pri_coffic
            return Quantity(value, self.q_type, unit)

    @property
    def value(self):
        return self.__value
    @property
    def current_unit(self):
        return self.__unit
    @property
    def q_type(self):
        return self.__type
    
        

