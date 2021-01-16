
PitchClasses = dict([])

class PitchClass:
    """The natural of this pitch class, removing all accidentals"""
    def natural(self):
        return PitchClasses[str(self)[0]]

class C(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 1
    def __str__(self):
        return "C"

class CSharp(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 2
    def __str__(self):
        return "C#"

class D(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 3
    def __str__(self):
        return "D"

class DSharp(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 4
    def __str__(self):
        return "D#"

class E(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 5
    def __str__(self):
        return "E"

class F(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 6
    def __str__(self):
        return "F"

class FSharp(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 7
    def __str__(self):
        return "F#"

class G(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 8
    def __str__(self):
        return "G"

class GSharp(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 9
    def __str__(self):
        return "G#"

class A(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 10
    def __str__(self):
        return "A"

class ASharp(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 11
    def __str__(self):
        return "A#"

class B(PitchClass):
    """Numeric value in terms of half-steps from C (1-indexed)"""
    num = 12
    def __str__(self):
        return "B"

ChromaticScale = [C, CSharp, D, DSharp, E, F, FSharp, G, GSharp, A, ASharp, B]

for p_class in ChromaticScale:
    PitchClasses[str(p_class)] = p_class



class Pitch:
    """Offset from C0"""
    def num(self):
        return self.p_class.num + self.octave * 12

    """Difference between two pitches, in semitones"""
    def __sub__(self, other):
        return self.num() - other.num()
    
    def __init__(self, klass, octave):
        self.p_class = klass
        self.octave = octave

    def __str__(self):
        return f'{self.p_class.__name__}{self.octave}'

    @staticmethod
    def from_num(n):
        return Pitch(ChromaticScale[(n - 1) % 12], (n - 1) // 12)

MiddleC = Pitch(C, 4)

C3 = Pitch(C, 3)
D3 = Pitch(D, 3)
E3 = Pitch(E, 3)
F3 = Pitch(F, 3)
G3 = Pitch(G, 3)
A3 = Pitch(A, 3)
B3 = Pitch(B, 3)
C4 = Pitch(C, 4)
D4 = Pitch(D, 4)
E4 = Pitch(E, 4)
F4 = Pitch(F, 4)
G4 = Pitch(G, 4)
A4 = Pitch(A, 4)
B4 = Pitch(B, 4)
C5 = Pitch(C, 5)
D5 = Pitch(D, 5)
E5 = Pitch(E, 5)
F5 = Pitch(F, 5)
G5 = Pitch(G, 5)
A5 = Pitch(A, 5)
B5 = Pitch(B, 5)
C6 = Pitch(C, 6)
D6 = Pitch(D, 6)
E6 = Pitch(E, 6)
F6 = Pitch(F, 6)
G6 = Pitch(G, 6)
A6 = Pitch(A, 6)
B6 = Pitch(B, 6)
