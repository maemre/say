from z3 import *

from scales import CMajor, complement
from notes import *
import intervals
from intervals import Octave
from util import *
import cantus_firmus

def in_key(solver, pitch_var, scale):
    # generate pitch ∈ scale if the scale is small. otherwise,
    # generate pitch ∉ complement(scale)
    if len(scale) <= 6:
        solver.assert_and_track(Or([pitch_var % 12 == note.num for note in scale]), f'{pitch_var}_in_key')
    else:
        solver.assert_and_track(And([pitch_var % 12 != note.num for note in complement(scale)]), f'{pitch_var}_in_key')

# This cantus firmus has repetitions so it is breaking some rules
# deliberately
CantusFirmus = list([note.num() for note in [C4, B3, C4, B3,
                                             A3, G3, A3, G3,
                                             B3, C4, D4, F4,
                                             D4, D4, B4, C4]])

assert(len(CantusFirmus) == 16)

# For now, the counterpoint will be above cantus firmus
counterpoint = Ints(' '.join(f'cp_{i}' for i in range(16)))

s = Solver()
s.set(unsat_core=True)
set_core_minimize(s)

## Inter-voice constraints

for i, note in enumerate(counterpoint):
    # make sure we are in key
    in_key(s, note, CMajor)
    # make sure we never cross cantus firmus
    s.assert_and_track(note > CantusFirmus[i], f'no_crossing_{i}')
    # make sure we never overlap cantus firmus
    if i != 0:
        s.assert_and_track(note >= CantusFirmus[i-1], f'no_overlap_{i}')
    # make sure we are never too far from cantus firmus
    s.assert_and_track(note <= CantusFirmus[i] + intervals.P12th, f'not_too_far_{i}')
    # make sure we are in range
    # s.add(And(note >= C3.num(), note <= C6.num()))
    # TODO: exceed a tenth only in emergencies

    # no unisons for now
    if 0 < i < len(counterpoint) - 1:
        s.assert_and_track((note - CantusFirmus[i]) % 12 != 0, f'no_unisons_{i}')

    if i > 0:
        # no perfect consonances in a row
        s.assert_and_track(Implies(perfect_consonance(counterpoint[i - 1], CantusFirmus[i - 1]),
                                   Not(perfect_consonance(note, CantusFirmus[i]))), f'no_perfect_consonance_{i}')
        # no tritones in a row
        s.assert_and_track(Implies(tritone_above(counterpoint[i - 1], CantusFirmus[i - 1]),
                                   Not(tritone_above(note, CantusFirmus[i]))), f'no_tritones_in_a_row_{i}')
        s.assert_and_track(Implies(m2_above(counterpoint[i - 1], CantusFirmus[i - 1]),
                                   Not(m2_above(note, CantusFirmus[i]))), f'no_m2_in_a_row_{i}')

    # TODO: avoid unisons but allow them rarely
    # TODO: prefer imperfect consonances over perfect consonance except for the ends


print("checking inter-voice constraints")
print(s.check())

if s.check() != sat:
    print(s.unsat_core())
    sys.exit(1)

# Should start with perfect consonance
s.assert_and_track(perfect_consonance(counterpoint[0], CantusFirmus[0]), 'start_with_perfect_consonance')

print("checking that we start with perfect consonance")
print(s.check())

# Should end in the 1st scale degree
s.assert_and_track(counterpoint[-1] % 12 == CMajor[0].num, 'end_in_key_center')

print("checking that we end on key center")
print(s.check())

# TODO: climaxes should not coincide

cantus_firmus.almost_cantus_firmus(s, counterpoint, 'cp')
print("checking that counterpoint is almost cantus firmus")
print(s.check())

if s.check() != sat:
    print(s.unsat_core())
    sys.exit(1)

## Intra-voice constraints
for i in range(1, len(counterpoint)):
    prev = counterpoint[i - 1]
    note = counterpoint[i]
    cf_prev = CantusFirmus[i - 1]
    cf_note = CantusFirmus[i]
    # never move more than an octave
    s.assert_and_track(And(prev - note <= Octave, note - prev <= Octave), f'no_leap_larger_than_octave_{i}')
    # TODO: no 3 same imperfect consonance type in a row, we are
    # adding another restriction here for simplicity: no same interval
    # 3 times in a row
    if i > 1:
        s.assert_and_track(Not(And(counterpoint[i - 2] - CantusFirmus[i - 2] == prev - cf_prev, prev - cf_prev == note - cf_note)), f'no_3_same_type_in_a_row_{i}')
    # don't stay on the same note for too long
    if i > 1:
        s.assert_and_track(Not(And(counterpoint[i - 2] == prev, prev == note)), f'dont_stay_for_longer_than_2_{i}')


# TODO: vary the types of motion (this could be done in CLP or max-SAT)
# TODO: never move into perfect consonance by similar motion
# TODO: avoid combining similar motion with leaps

print("checking other intra-voice constraints")
print(s.check())

if s.check() != sat:
    print(s.unsat_core())

print(s.statistics())

with open('z3-constraints.smt2', 'w') as f:
    f.write(s.sexpr())

m=s.model()
for note in counterpoint:
    numeric_val = m[note].as_long()
    note_value = Pitch.from_num(m[note].as_long())
    print(f'{note}\t{note_value}\t{note_value.num()}\t{numeric_val}')
