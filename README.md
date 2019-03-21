# ASTObfuscate

ASTObfuscate is a little project designed to parse Python syntax, and turn that Python into an obfuscated version for compilation into  `.pyc` file.

ASTObfuscate is not meant for pure obfuscation of the source code, as it is relatively easy to make the source code much more readable by folding in constants

### Use Cases
ASTObfuscate was originally based on [Jurrian Bremer's AST obfuscator he made for a CTF event](http://jbremer.org/python-source-obfuscation-using-asts/).
ASTObfuscate may not hold up to expert eyes, but combining it with compilation into a `.pyc` file will probably make for a reasonably difficult CTF, but manual obfuscation
of the source code is recommended before running it through ASTObfuscate. 

See the crc32 files for an example of simple CTF flag verifier obfuscated with 5 passes of ASTObfuscate

### Examples
```python
print('Hello, World!')
```
becomes
```python
OO11lOO01O00lllOlllOl = (lambda l00110100O00lO11111lO,
    lO10111llOlO1011100ll: l00110100O00lO11111lO % lO10111llOlO1011100ll)
O00011OOO10OlOOl01O11 = (lambda Ol01lOlOO0100OlOlO0O0,
    O0lO101lO0Ol1O1lO0lOl: Ol01lOlOO0100OlOlO0O0 ^ O0lO101lO0Ol1O1lO0lOl)
print(''.join(filter(lambda llO1lOOll111O0100OllO: ord(
    llO1lOOll111O0100OllO) % O00011OOO10OlOOl01O11(2 ^ 4, 0 * 3 + 0) != 0 *
    5 + 0, '*ZZ\x12\x0cx\x00\x0660\x12xZ\x18\x0c')).join(chr(
    O00011OOO10OlOOl01O11(ll0O1O110lOO0OlOl10OO, OO11OOl1lO0O0011OOlll)) for
    OO11OOl1lO0O0011OOlll, ll0O1O110lOO0OlOl10OO in zip(
    b'\\rUc\xc0KgW\xf8\xfc?\x12\x0b', b'}\x169\x11\xaf\x1cG{\x97\x90SwC'))[
    ::-1 * 6 + 5 ^ 0 * 6 + 0])
```

### Usage
```$ astobfuscate.py <input filename> <output filename> <passes>```

Run ASTObfuscate on the source code `passes` times. Note that the code will become exponentially slower and larger as the number of passes go up.

```$ astobfuscate.py <input filename> <output filename>```

Run ASTObfuscate on the source code once. 

In Python source:

```python
def function_to_remain(arg1, arg2, arg3, *remaining, ast_no_obfuscate=None):
    pass
```

Tell ASTObfuscate that a function's name and arguments should remain the same and not be changed. All other functions will be renamed and have their arguments obfuscated

### Possible improvements:
* Add a function to turn the entire program into a single line of code, likely using csvoss's [onelinerizer](https://github.com/csvoss/onelinerizer). This approach will likely fail
if the program needs to have functions or classes exported.

* Add more ways for integers, strings, and booleans to be obfuscated. This would add more variation to the generated code.

* Class attribute and method obfuscation.

* Folding of single return statement functions into lambdas

* Lambda namespaces

### Thanks for reading!