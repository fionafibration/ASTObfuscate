import ast
from ast import *
from collections import namedtuple
import astor.code_gen
import pyminifier.minification
import pyminifier.token_utils
import random
import os
import sys
import time


def random_string(minlength, maxlength):
    return random.choice('lO') + ''.join(random.choice('lO10') for _ in range(random.randint(minlength, maxlength)))


def import_node(name, newname, froms=None):
    if froms:
        froms = [Str(from_name) for from_name in froms]
    else:
        froms = []
    """Import module obfuscation"""
    # import sys -> sys = __import__('sys', globals(), locals(), [], -1)
    return Assign(
        targets=[Name(id=newname, ctx=Store())],
        value=Call(func=Name(id='__import__', ctx=Load()),
                   args=[Str(s=name),
                         Call(func=Name(id='globals', ctx=Load()), args=[],
                              keywords=[], starargs=None, kwargs=None),
                         Call(func=Name(id='locals', ctx=Load()), args=[],
                              keywords=[], starargs=None, kwargs=None),
                         List(elts=froms, ctx=Load()), Num(n=0)],
                   keywords=[], starargs=None, kwargs=None))


def obfuscate_string(s):
    """Various String Obfuscation routines."""
    var1 = random_string(20, 20)
    var2 = random_string(20, 20)

    random_bytes = os.urandom(len(s))

    pair1 = random_bytes
    pair2 = bytes([
        x ^ y for x, y in zip(random_bytes, s.encode('utf-8'))
    ])

    random_divisor = random.randint(2, 6)

    chars = list(filter(lambda x: ord(x) % random_divisor == 0, [chr(x) for x in range(0, 126)]))

    list_of_chars = ''.join([random.choice(chars) for _ in range(15)])



    table0 = [
        # '' -> ''
        lambda: Str(s=''),

        lambda: Call(func=Attribute(value=Str(s=''), attr='join', ctx=Load()), args=[Call(func=Name(id='filter', ctx=Load()), args=[Lambda(args=arguments(args=[arg(arg=var1, annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=Compare(left=BinOp(left=Call(func=Name(id='ord', ctx=Load()), args=[Name(id=var1, ctx=Load())], keywords=[]), op=Mod(), right=Num(n=random_divisor)), ops=[NotEq()], comparators=[Num(n=0)])), Bytes(s=list_of_chars)], keywords=[])], keywords=[])
    ]

    table1 = [
        # 'a' -> 'a'
        lambda x: Str(s=chr(x)),
        # 'a' -> chr(0x61)
        lambda x: Call(func=Name(id='chr', ctx=Load()), args=[Num(n=x)],
                       keywords=[], starargs=None, kwargs=None),
    ]

    table = [
        # 'abc' -> 'a' + 'bc'
        lambda x: BinOp(left=Str(s=x[:len(x)//2]),
                        op=Add(),
                        right=Str(s=x[len(x)//2:])),
        # 'abc' -> 'cba'[::-1]
        lambda x: Subscript(value=Str(s=x[::-1]),
                            slice=Slice(lower=None, upper=None,
                                        step=Num(n=-1)),
                            ctx=Load()),

        lambda x: Call(func=Attribute(value=Str(s=''), attr='join', ctx=Load()), args=[GeneratorExp(elt=Call(func=Name(id='chr', ctx=Load()), args=[BinOp(left=Name(id=var1, ctx=Load()), op=BitXor(), right=Name(id=var2, ctx=Load()))], keywords=[]), generators=[comprehension(target=Tuple(elts=[Name(id=var2, ctx=Store()), Name(id=var1, ctx=Store())], ctx=Store()), iter=Call(func=Name(id='zip', ctx=Load()), args=[Bytes(s=pair1), Bytes(s=pair2)], keywords=[]), ifs=[], is_async=0)])], keywords=[])
    ]

    if not len(s):
        return random.choice(table0)()

    if len(s) == 1:
        return random.choice(table1)(ord(s))

    return random.choice(table)(s)


class Obfuscator(ast.NodeTransformer):
    def __init__(self, layers=1):
        ast.NodeTransformer.__init__(self)

        # imported modules
        self.imports = {}

        # Import values from modules
        self.from_imports = {}

        # The names of the imported values
        self.import_aliases = {}

        # global values (can be renamed)
        self.globs = {}

        # local values
        self.locs = {}

        # inside a function
        self.indef = False

        self.layers = layers

        self.renamed = False

    def obfuscate_global(self, name):
        newname = random_string(20, 20)
        self.globs[name] = newname
        return newname

    def obfuscate_local(self, name):
        newname = random_string(20, 20)
        self.locs[name] = newname
        return newname

    def visit_Import(self, node):
        newname = self.obfuscate_global(node.names[0].name)
        self.imports[node.names[0].name] = newname

    def visit_ImportFrom(self, node):
        module_name = self.obfuscate_global(node.module)
        self.from_imports[module_name] = {}
        self.import_aliases[node.module] = module_name
        for alias in node.names:
            self.from_imports[module_name][alias.name] = self.obfuscate_global(alias.name)

    def visit_Str(self, node):
        return obfuscate_string(node.s)

    def visit_Num(self, node):
        type = random.randint(1, 3)
        if type == 1:
            d = random.randint(2, 6)
            return BinOp(left=BinOp(left=Num(node.n // d), op=Mult(),
                                    right=Num(n=d)),
                         op=Add(), right=Num(node.n % d))
        elif type == 2 and node.n:
            random_num = random.getrandbits(node.n.bit_length())
            return BinOp(left=Num(node.n ^ random_num), op=BitXor(), right=Num(random_num))

        else:
            return node

    def visit_Attribute(self, node):
        if isinstance(node.value, Name) and isinstance(node.value.ctx, Load):
            node.value = self.visit(node.value)
            return Call(func=Name(id='getattr', ctx=Load()), args=[
                Name(id=node.value.id, ctx=Load()), Str(s=node.attr)],
                keywords=[], starargs=None, kwargs=None)
        node.value = self.visit(node.value)
        return node

    def visit_BinOp(self, node):

        opnames = {
            Add: 'add',
            Sub: 'sub',
            Mult: 'mul',
            Div: 'truediv',
            FloorDiv: 'floordiv',
            Mod: 'mod',
            Pow: 'pow',
            BitOr: 'or',
            BitXor: 'xor',
            BitAnd: 'and',
            LShift: 'lshift',
            RShift: 'rshift',
        }

        if type(node.left) == Num and type(node.right) == Num:
            obfuscate_numbers = True
        else:
            obfuscate_numbers = False

        node.left = self.visit(node.left)
        node.right = self.visit(node.right)

        if obfuscate_numbers:
            try:
                return Call(func=Attribute(value=Name(self.globs.get('operator', 'operator'), ctx=Load()), attr=opnames[type(node.op)]), args=[node.left, node.right], keywords=[])
            except:
                return node
        else:
            return node

    def visit_FunctionDef(self, node):
        self.indef = True
        self.locs = {}
        node.name = self.obfuscate_global(node.name)
        node.body = [self.visit(x) for x in node.body]
        self.indef = False
        return node

    def visit_Name(self, node):
        # obfuscate known globals
        if not self.indef and not self.renamed and isinstance(node.ctx, Store) and node.id not in self.globs:
            node.id = self.obfuscate_global(node.id)
        #elif self.indef:
        #    if isinstance(node.ctx, Store):
        #        node.id = self.obfuscate_local(node.id)
        #    node.id = self.locs.get(node.id, node.id)
        node.id = self.globs.get(node.id, node.id)
        return node

    def visit_Module(self, node):
        # Import the operator module
        # This is used for obfuscating binary operations
        newname = self.obfuscate_global('operator')
        self.imports['operator'] = newname

        for i in range(self.layers):
            node.body = [y for y in (self.visit(x) for x in node.body) if y]
            self.renamed = True

        for name, newname in self.imports.items():
            node.body.insert(0, import_node(name, newname))

        for name, newname in self.import_aliases.items():
            for alias in self.from_imports[newname].keys():
                node.body.insert(0, Assign(targets=[Name(id=self.from_imports[newname][alias], ctx=Store())],
                                           value=Attribute(
                                               value=Name(id=newname, ctx=Load()),
                                               attr=alias
                                           )))
            node.body.insert(0, import_node(name, newname, self.from_imports[newname].keys()))


        node.body = [y for y in (self.visit(x) for x in node.body) if y]
        return node


class GlobalsEnforcer(ast.NodeTransformer):
    def __init__(self, globs):
        ast.NodeTransformer.__init__(self)
        self.globs = {}

    def visit_Name(self, node):
        node.id = self.globs.get(node.id, node.id)
        return node


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)

    if len(sys.argv) == 3:
        layers = int(sys.argv[2])
    else:
        layers = 1

    if sys.argv[1] == '-':
        root = ast.parse(sys.stdin.read())
    else:
        root = ast.parse(open(sys.argv[1], 'rb').read())

    # obfuscate the AST
    obf = Obfuscator(layers=layers)
    root = obf.visit(root)

    # resolve all global names
    root = GlobalsEnforcer(obf.globs).visit(root)

    print(astor.code_gen.to_source(root, indent_with=' '))
