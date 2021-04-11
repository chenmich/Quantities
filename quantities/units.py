#from ast import parse, Subscript, Name, Constant, dump
import ast


__prefix_value__ = {
    "da":1e+1, "h":1e+2,  "k":1e+3,  "M":1e+6,  "G" :1e+9, 
    "T":1e+12, "P":1e+15, "E":1e+18, "Z":1e+21, "Y":1e+24,
    "d":1e-1,  "c":1e-2,  "m":1e-3,  "mu":1e-6, "n":1e-9,
    "p":1e-12, "f":1e-15, "a":1e-18, "z":1e-21, "y":1e-24,
    "base":1e+0
}

class UnitExpressVisitor(ast.NodeTransformer):
    '''
        This class will generate the latex express and html express for unit' epxpress.
        The raw express of units will be arithmetic expression. It is storage in the class variable
        profile of the class Unit and subclass. 
        This class will walk the ast by parsing from the arithmetic expression.

    '''
    def __init__(self):
        super().__init__()
        self.latex = ''
        self.html = ''
    
    def visit_Num(self, node):
        self.latex = self.latex + str(node.value) +"}"
        self.html = self.html + str(node.value) + "</sup>"
    def visit_Name(self, node):
        self.latex = self.latex +  node.id
        self.html =  self.html + node.id  
        
    def visit_BinOp(self, node):
        self.visit(node.left)
        if isinstance(node.op, ast.Div):
            self.latex = self.latex + '/'
            self.html = self.html + '/'
        if isinstance(node.op, ast.Sub):
            self.latex =  self.latex + '^{-'
            self.html = self.html + '<sup>-'
        if isinstance(node.op, ast.Add):
            self.latex = self.latex + "^{"
            self.html = self.html + "<sup>"
        if isinstance(node.op, ast.Mult):
            self.latex = self.latex + "\cdot "
            self.html = self.html + "·"
        self.visit(node.right) 

class Unit():
    ''' 
        This class is the base class for all units
        the variable  profile will 
        The arithmetic expression of units will follow the rules:
        1.the symbol of each will be an item
        2.the symbol will be seperated from each other by "*" and "/", "+" and "-"
        3.The exponent of the power of the symbol is directly expressed 
          by addition and subtraction operator
        for example:
            kg*m/s-2
            kg*m+2*s-3
            kg-1*m-2*s+3*A+2
            m/s
            m
        This arithmetic expression will be convert the latex and html express
    '''
    prefix = {'name':'', 'symbol':'base'}
    q_type = None
    
    profile = {
        "name":'',
        'symbol':'', 
        'express_by_SI_base':'', 
        'express_by_SI':'' 
    }
    @classmethod
    def from_pri_unit(cls):
        return 1 /__prefix_value__[cls.prefix['symbol']]
    @classmethod
    def to_pri_unit(cls):
        return __prefix_value__[cls.prefix["symbol"]]
    @classmethod
    def symbol(cls):
        return cls.profile["symbol"]
    @classmethod
    def express_by_SI_base(cls):
        tree = ast.parse(cls.profile['express_by_SI_base'])
        visitor = UnitExpressVisitor()
        visitor.visit(tree)
        return visitor.latex, visitor.html
    @classmethod 
    def express_by_SI(cls):
        tree = ast.parse(cls.profile['express_by_SI'])
        visitor = UnitExpressVisitor()
        visitor.visit(tree)
        return visitor.latex, visitor.html

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


