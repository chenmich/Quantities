from .quantity_type import QuantityType

class Quantity():
    def __init__(self, value:float, q_type:QuantityType):
        self.__value = value
        self.__type = q_type

