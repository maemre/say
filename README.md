# say

Say (pronounced [/saj/](https://en.wikipedia.org/wiki/Help:IPA/Turkish) is
a tool to generate polyphonic pieces following rules from common practice in Western classical music.

## Why?

I was learning species counterpoint, and a lot of the rules looked like they could be encoded in linear integer arithmetic and solved by Z3.

## How

say treats each voice (i.e. melody line) as an array of symbolic integer variables (represented in Z3), and encodes constraints between melody lines, and constraints inside a melody line using integer arithmetic constraints. Then, Z3 can solve the set of constraints to produce a melody line with given requirements

## System Requirements

You need to have Python 3.7+, JDK 14, Scala 2.13, SBT 1.4 (Scala and SBT are installed automatically if you have a recent enough version of SBT), and a recent enough version of Z3 (we are using 4.8.9).

## Types of compositions/feature list/roadmap

### Species counterpoint

Roughly following Johann Joseph Fux's _Gradus ad Parnassum_, the roadmap for species counterpoint is:

- [ ] Cantus firmus
    - [ ] only whole notes
    - [ ] only steps
    - [ ] steps, skips, and leaps
- [ ] First species (against a given cantus firmus)
    - [ ] only one line besides the cantus firmus
    - [ ] multiple lines
- [ ] First species and cantus firmus
    - combining the parts before
- [ ] Second species
    - [ ] two notes against one
    - [ ] can start on upbeat and have rests
- [ ] Third species
    - [ ] 4 (or 3) notes against one
- [ ] Fourth species
    - [ ] sustained notes, syncopation
    - [ ] supplied rhythmic structure
    - [ ] generated rhytmic structure
- [ ] Fifth species
    - [ ] switching between species
- [ ] Using existing techniques & derivations
    - [ ] double passing tone
    - [ ] double neighbor
    - [ ] melodic inversion
    - [ ] retrograde
    - [ ] retrograde inversion
    - [ ] agumentation
    - [ ] diminution

An important goal for us is to syntesize a cantus firmus *along with* the other melodies, rather than generating melodies over a given cantus firmus. This can later be restricted to "write over" a given counterpoint by fixing the counterpoint in the constraints generated

### Free counterpoint

TODO

### Inventions

TODO

### Writing crab cannons

TODO

### Chord progressions

TODO

### Scales:

- [ ] C major
- [ ] major scale in other keys
- [ ] modes of C major
- [ ] other scales
- [ ] key changes

### Time signatures:

Each time signature would involve incorporating the accent structure within it

- [ ] 4/4 - common time
- [ ] 3/4
- [ ] 2/4
- [ ] compound meters (6/8, 9/8, etc)
- [ ] ability to extend with other odd time signatures
- [ ] switching meters
- [ ] borrowing parts from other meters (tuplets)

### Soft constraints

A lot of the guidelines involve "avoid X" along with "do not do Y". Initially, we interpret it as "do not do X". However, as this project evolves, we are planning to implement a "probably bad idea" budget to allow things that should be avoided to add some spiciness to the composition.
