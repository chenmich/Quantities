__prefix_value__ = {
    "da":1e+1, "h":1e+2,  "k":1e+3,  "M":1e+6,  "G" :1e+9, 
    "T":1e+12, "P":1e+15, "E":1e+18, "Z":1e+21, "Y":1e+24,
    "d":1e-1,  "c":1e-2,  "m":1e-3,  "mu":1e-6, "n":1e-9,
    "p":1e-12, "f":1e-15, "a":1e-18, "z":1e-21, "y":1e-24,
    "base":1e+0
}

class Unit():
    prefix = {'name':'', 'symbol':'base'}
    @classmethod
    def from_pri_unit(cls):
        raise NotImplementedError
    def to_pri_unit(cls):
        raise NotImplementedError

class dUnit(Unit):
    pass