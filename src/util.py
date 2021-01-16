from z3 import *

from notes import *
import intervals
from intervals import Octave

def Abs(x):
    return If(x<0,-x,x)

def melodic_consonance(p1, p2):
    ival = Abs(p2 - p1) % 12
    return And(ival < intervals.Min7th, # this implies it is not a 7th
               ival != intervals.Tritone)

def tritone_above(p1, p2):
    ival = p2 - p1 % 12
    return ival == intervals.Tritone

def m2_above(p1, p2):
    ival = p2 - p1 % 12
    return ival == intervals.Min2nd

def perfect_consonance(p1, p2):
    return Or((p1 - p2) % 12 == intervals.Unison, (p1 - p2) % 12 == intervals.P5th)

def set_core_minimize(s):
    s.set("core.minimize", True)
