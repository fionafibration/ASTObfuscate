from z3 import *
"""
Proves the equivalence of certain operators to highly obfuscated bitwise alternatives

Uses the Z3 theorem prover:

https://github.com/Z3Prover/z3
"""



BITS = 64

def prove(equality):
    s = Solver()
    s.add(Not(equality))
    return s.check() == unsat


x, y = BitVecs('x y', BITS)

proofs = [
    x + y == 2 * (x | y) - (x ^ y),
    x + y == (x | y) + (x & y),

    x - y == 2 * (x | ~y + 1) - (x ^ ~y + 1),
    x - y == (x | ~y + 1) + (x & ~y + 1),

    x | y == (x ^ y) | (x & y),
    x | y == ~(~(x & x) & ~(y & y)),

    x & y == (x | y) - (x ^ y),
    x & y == ~(~(x & y) & ~(x & y)),

    x ^ y == x - y + 2 * (~x & y),
    x ^ y == ~(x & y) & ~(~x & ~y),
    x ^ y == (~x & y) | (x & ~y),

    ~x == ~(x & x),
    ~x == ~(x & (x ^ ~x)) & ~(~x & 0),
    ~x == x ^ (x ^ ~x),

    -x == ~(x & x) + 1,
    -x == (~(x & (x ^ ~x)) & ~(~x & 0)) + 1,
    -x == (x ^ (x ^ ~x)) + 1,
]

assert(all([prove(proof) for proof in proofs]))

print('Proved all equalities!')
