import pytest
from quantities import units
from ast import parse

def test_UnitExpressVisitor_visit():
    visitor = units.UnitExpressVisitor()
    unit_exp = 'm'
    tree = parse(unit_exp)
    visitor.visit(tree)
    assert visitor.latex == 'm'
    assert visitor.html == 'm'

    visitor = units.UnitExpressVisitor()
    unit_exp = 'm/s'
    tree = parse(unit_exp)
    visitor.visit(tree)
    assert visitor.latex == 'm/s'
    assert visitor.html == 'm/s'

    visitor = units.UnitExpressVisitor()
    unit_exp = "kg*m+2*s-3"
    tree = parse(unit_exp)
    visitor.visit(tree)
    assert visitor.latex == "kg\cdot m^{2}\cdot s^{-3}"
    assert visitor.html == "kg·m<sup>2</sup>·s<sup>-3</sup>"