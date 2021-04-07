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
        return __prefix_value__[cls.prefix['symbol']]
    @classmethod
    def to_pri_unit(cls):
        return 1 /__prefix_value__[cls.prefix["symbol"]]

class yUnit(Unit):
    prefix = {'name':'yocto','symbol':'y'}
    
class zUnit(Unit):
    prefix = {'name':'zepto','symbol':'z'}
    
class aUnit(Unit):
    prefix = {'name':'atto','symbol':'a'}
    
class fUnit(Unit):
    prefix = {'name':'femto','symbol':'f'}
class pUnit(Unit):
    prefix = {'name':'pico','symbol':'p'}
class nUnit(Unit):
    prefix = {'name':'nano','symbol':'n'}
class muUnit(Unit):
    prefix = {'name':'micro','symbol':'mu'}
class mUnit(Unit):
    prefix = {'name':'milli','symbol':'m'}
class cUnit(Unit):
    prefix = {'name':'centi','symbol':'c'}
class dUnit(Unit):
    prefix = {'name':'deci','symbol':'d'}
class YUnit(Unit):
    prefix = {'name':'yotta','symbol':'Y'}
class ZUnit(Unit):
    prefix = {'name':'zetta','symbol':'Z'}
class EUnit(Unit):
    prefix = {'exa':'giga','symbol':'E'}
class PUnit(Unit):
    prefix = {'name':'peta','symbol':'P'}
class TUnit(Unit):
    prefix = {'name':'tera','symbol':'T'}
class GUnit(Unit):
    prefix = {'name':'giga','symbol':'G'}    
class MUnit(Unit):
    prefix = {'name':'mega','symbol':'M'}
class kUnit(Unit):
    prefix = {'name':'kilo','symbol':'k'}
class hUnit(Unit):
    prefix = {'name':'hecto','symbol':'h'}
class daUnit(Unit):
    prefix = {'name':'deka','symbol':'da'}