# Scale data

import notes as n

CMajor = [n.C, n.D, n.E, n.F, n.G, n.A, n.B]
CSharpPentatonic = [n.CSharp, n.DSharp, n.FSharp, n.GSharp, n.ASharp]
ChromaticScale = n.ChromaticScale

def complement(scale):
    if scale == CMajor:
        return CSharpPentatonic
    if scale == CSharpPentatonic:
        return CMajor
    raise Exception("complement for other scales is not implemented yet")
