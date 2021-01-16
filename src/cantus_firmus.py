from z3 import *

from scales import CMajor, complement
from notes import *
import intervals
from intervals import Octave
from util import *

"""This module implements cantus firmus rules"""

def almost_cantus_firmus(s, cf, line_name):
    '''All cantus firmus rules that apply to other lines as well'''

    # the last note should be approached by step, i.e. leading tone
    # progresses to tonic
    last_ival = Abs(cf[-2] - cf[-1])
    s.assert_and_track(And(last_ival <= 2, last_ival > 0), f'last_note_approached_by_step')
    # bounds
    min_line, max_line = Ints(f'{line_name}_min {line_name}_max')
    for note in cf:
        s.add(min_line <= note)
        s.add(max_line >= note)
    s.add(Or([min_line == note for note in cf]))
    s.add(Or([max_line == note for note in cf]))
    # range no more than a tenth
    s.add(max_line - min_line <= intervals.Maj10th)

    # TODO: a single climax
    # TODO: smooth shape
    # TODO: no repetition of motifs or licks
    # any large leaps are followed by step in opposite direction
    for i, note in enumerate(cf):
        if i == 0 or i == len(cf) - 1:
            continue
        # down & up
        # also make sure the second part is a step
        s.add(Implies(cf[i - 1] - note > intervals.Maj3rd, And(note < cf[i + 1], note >= cf[i + 1] - intervals.Maj2nd)))
        # up & down
        # also make sure the second part is a step
        s.add(Implies(cf[i - 1] - note < - intervals.Maj3rd, And(note > cf[i + 1], note <= cf[i + 1] + intervals.Maj2nd)))
    # all progressions are melodic consonances
    for i in range(1, len(cf)):
        s.assert_and_track(melodic_consonance(cf[i-1],cf[i]), f'melodic_consonance_{line_name}_{i}')
