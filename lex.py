import sys
import re

exprs = [
    (r'[ \t\n]+', None, None),
    ('if','IF',None),
    ('else','ELSE',None),
    ('while','WHILE',None),
    ('LinkedList','LINKED_LIST',0),
    (';','CLOSE',None),
    ('(==)|(<=)|(>=)|(!=)|>|<', 'LOGICAL_OP',0),
    ('=', 'ASSIGN',0),
    (r'\(', 'LP',None),
    (r'\)', 'RP',None),
    ('{', 'LB',None),
    ('}', 'RB',None),
    (',', 'COMMA',None),
    (r'-?0|(-?[1-9][0-9]*)', 'NUM',None),
    ('[+]', 'PLUS',1),
    ('[-]', 'MINUS',1),
    ('[*]', 'MUL',2),
    ('[/]', 'DIV',2),
    (r'[A-Za-z_][A-Za-z0-9_]*', 'VAR',None)
]

def lex(characters):
    position, tokens = 0, []
    while position < len(characters):
        for expr in exprs:
            pattern, tag , priority = expr
            regex = re.compile(pattern)
            match = regex.match(characters, position)
            if match:
                text = match[0]
                if tag:
                    token = (text, tag, priority)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('unexpected symbol: %s\n' % characters[position])
            sys.exit(1)
        else:
            position = match.end()
    return tokens
