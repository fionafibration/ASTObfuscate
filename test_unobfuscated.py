import getpass
from os import urandom
name = getpass.win_getpass('What is your name?')

if name:
    print('Hello, %s!' % name)
else:
    print('I see how it is!')

x = 57
print(x, x + 2, x // 2)
print('Expected: 57 59 28')
print('Random byte is: %r' % urandom(1))