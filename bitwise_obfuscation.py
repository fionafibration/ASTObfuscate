from z3 import *
from arybo.lib import MBA, boolean_expr_solve
import random

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

a = random.getrandbits(64)
b = 0x7fffffffffffffff ^ a
c = random.getrandbits(64)
d = 0x7fffffffffffffff ^ b


def f(X):
  T = ((X+1)&(~X))
  C = ((T | a) & c) + ((~T & b) | d)
  return C

m = MBA(64)
c = m.var('x')
print(f(c))

0x7AFAFA697AFAFA69 0x80A061440A061440 0x10401050504 0x1010104

"""
sols = boolean_expr_solve(f(c)[63], c, 1)
zero = sols[0].get_int_be()

print(hex(zero))"""
