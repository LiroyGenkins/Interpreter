from lex import lex
from pars import SyntaxCheck
from StackMachine import StackMachine
import sys

cod = input('>>> ')
while cod != 'exit':
    try:
        tokens = lex(cod)
        print(tokens)
        parser = SyntaxCheck(tokens)
        lang = parser.lang()
        print(lang)
        for char in lang.rpn:
            print(char[0],end = '\t')
        print()
        for i in range(len(lang.rpn)):
            print(i,end = '\t')
        print()
    except:
        print('Syntax error')
    try:
        sm = StackMachine(lang.rpn)
        sm.run()
        for var in sm.variables.items():
            print(var)
    except BaseException:
        pass
    cod = input('>>> ')
sys.exit(0)