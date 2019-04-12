from arybo.lib import MBA, boolean_expr_solve
import random
"""
Implements a generator for a dirac delta function, which is a function which is one value across it's entire domain
except for one input

Can be used to have an obfuscated equality check or the like

Uses the Arybo Mixed Boolean Arithmetic symbolics library 
"""



# Initialize our values:
# Bitlength
# The "zero" of the dirac function, or rather where it is different
# The desired output at the zero

bitlength = input('What is the desired bitlength? Press enter to default to 64.\n>>>')

bitlength = int(bitlength) if bitlength else 64

desired_zero = input('What is the desired solution of the Dirac function?\n'
                     'E.G. 0xdeadbeef, 12345, etc.\n'
                     'Press enter to default to random value\n>>>')

desired_zero = eval(desired_zero) if desired_zero else random.getrandbits(bitlength)

desired_output = input('What is the desired output at the dirac value?\n'
                       'E.G. 0xdeadbeef, 12345, etc.\n'
                       'Press enter to default to random value\n>>>')

desired_output = eval(desired_output) if desired_output else random.getrandbits(bitlength)



# They have to fit within our bitlength
assert type(desired_zero) == int and desired_zero.bit_length() <= bitlength
assert type(desired_output) == int and desired_output.bit_length() <= bitlength

# The zero before XORing with e is always 0x7ffff...
basic_zero = ((1 << bitlength - 1) - 1)

# Basic bit of obfuscation, this doesn't change anything
a = random.getrandbits(bitlength - 1)
b = a ^ basic_zero

# This gets XORed to produce the desired output
d = desired_output ^ ((1 << bitlength) - 1)

# This gets XORed to produce the desired input
e = desired_zero ^ basic_zero


# Our function
def f(X):
    T = (X + 1) & (~X)
    return ((T | a) + (~(T) & b)) ^ d

# Solve the function with Arybo to ensure it's a Dirac delta
m = MBA(bitlength)
c = m.var('x')

# Solve where the output highest bit is equal to the highest bit in the desired output
# Everything else will always be equal
sols = boolean_expr_solve(f(c)[bitlength - 1], c, (desired_output & ~(basic_zero)) >> bitlength)
zero = sols[0].get_int_be()

# We should only have one solution, and it should be our 0x7ffff...
assert len(sols) == 1
assert zero == basic_zero


# Build the same function but with the XORing with e to change the actual zero
def f(X):
    X = X ^ e
    T = (X + 1) & (~X)
    return ((T | a) + (~(T) & b)) ^ d

zero = zero ^ e

# Evaluate our function to show to the user it's working
print('Dirac Value: %s' % hex(zero))
print('Function at Dirac: %s' % hex(f(zero)))
print('Function at Dirac + 1: %s' % hex(f((zero + 1) % (2 ** bitlength - 1))))
print('Function at Dirac + 2: %s' % hex(f((zero + 2) % (2 ** bitlength - 1))))


# Print out our dirac function with everything inlined
print('Dirac Function:\n((((x ^ %s) + 1) & (~(x ^ %s)) | %s) + (~(((x ^ %s) + 1) & (~(x ^ %s))) & %s)) ^ %s' % (e, e, a, e, e, b, d))