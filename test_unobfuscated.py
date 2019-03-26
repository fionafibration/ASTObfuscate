import getpass
from os import urandom

name = getpass.win_getpass('What is your name?')


def random_bytes(num_bytes, *, ast_no_obfuscate=None):
    byte_data = urandom(num_bytes)
    return byte_data


def single_random_byte(unused_arg):
    return urandom(1)


def add_2_nested(a, b):
    def x(b):
        return b + 2
    return x(a)


class Data:
    internal = 2

    def add_2_instance(self, a, *, ast_no_obfuscate=None):
        return a + self.internal

    @classmethod
    def add_2_class(cls, a):
        return a + cls.internal

    @staticmethod
    def add_2_static(a):
        return a + 2

if name:
    print('Hello, %s!' % name)
else:
    print('I see how it is!')

x = 57
print(x, Data.add_2_class(x), Data().add_2_instance(x), Data().add_2_static(x), add_2_nested(x, None), x // 2, 0.1 + 0.2, ~2)
print('Expected: 57 59 59 59 59 28 0.30000000000000004 -3\n')

x += 15
print(x)
print('Expected: 72\n')

Data.internal += 1

print(x, Data.add_2_class(x), Data().add_2_instance(x), Data().add_2_static(x), add_2_nested(x, None))
print('Expected: 72 75 75 74 74\n')

print(True, True, True, True, True)
print('Expected: True True True True True\n')

print(False, False, False, False, False)
print('Expected: False False False False False\n')

print('Random byte is: %r' % single_random_byte(None))