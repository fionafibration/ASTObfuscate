from arybo.lib import MBA, boolean_expr_solve
import random

a = random.getrandbits(64)
b = a ^ 0x7fffffffffffffff
d = random.getrandbits(63)
e = random.getrandbits(64)


def f(X):
    T = (X + 1) & (~X)
    return ((T | a) + (~(T) & b)) ^ d

m = MBA(64)
c = m.var('x')

sols = boolean_expr_solve(f(c)[63], c, 1)
zero = sols[0].get_int_be()

def f(X):
    X = X ^ e
    T = (X + 1) & (~X)
    return ((T | a) + (~(T) & b)) ^ d

zero = zero ^ e

print('Zero Value: %s' % hex(zero))
print('Function at Dirac: %s' % hex(f(zero)))
print('Function at Dirac + 1: %s' % hex(f(zero + 1)))
print('Function at Dirac + 2: %s' % hex(f(zero + 2)))

print('Dirac Function:\n((((x ^ %s) + 1) & (~(x ^ %s)) | %s) + (~(((x ^ %s) + 1) & (~(x ^ %s))) & %s)) ^ %s' % (e, e, a, e, e, b, d))