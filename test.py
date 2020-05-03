import build_in_functions
import keywords
import parser
import sys

if ".." not in sys.path: sys.path.insert(0, "..")
import ply.lex as lex

keyword_list = keywords.keywords_dictionary
build_ins = build_in_functions.build_in_functions
reserved_words = {**keyword_list, **build_ins}
stack = [0]

tokens = [
    'STRING',
    'VAR',
    'NUMBER',
    'ID',
    'EQEQUAL',
    'NOTEQUAL',
    'LESSEQUAL',
    'GREATEREQUAL',
    'LEFTSHIFT',
    'RIGHTSHIFT',
    'DOUBLESTAR',
    'PLUSEQUAL',
    'MINEQUAL',
    'STAREQUAL',
    'SLASHEQUAL',
    'PERCENTEQUAL',
    'AMPEREQUAL',
    'VBAREQUAL',
    'CIRCUMFLEXEQUAL',
    'LEFTSHIFTEQUAL',
    'RIGHTSHIFTEQUAL',
    'DOUBLESTAREQUAL',
    'DOUBLESLASH',
    'DOUBLESLASHEQUAL',
    'ATEQUAL',
    'ELLIPSIS',
    'COLONEQUAL',
    'NEWLINE',
    'INDENT',
    'DEDENT'
]

tokens = tokens + list(reserved_words.values())

literals = ['+', '-', '*', '/', '(', ')', '[', ']', '.', ',', ':', ';', '|', '&', '<', '>', '=', '%', '{', '}', '~',
            '^', '@', ]

t_NEWLINE = r'\n'
t_EQEQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_LESSEQUAL = r'\<\='
t_GREATEREQUAL = r'\>\='
t_LEFTSHIFT = r'\<\<'
t_RIGHTSHIFT = r'\>\>'
t_DOUBLESTAR = r'\*\*'
t_PLUSEQUAL = r'\+\='
t_MINEQUAL = r'\-\='
t_STAREQUAL = r'\*\='
t_SLASHEQUAL = r'\/\='
t_PERCENTEQUAL = r'\%\='
t_AMPEREQUAL = r'\&\='
t_VBAREQUAL = r'\|\='
t_CIRCUMFLEXEQUAL = r'\^\='
t_LEFTSHIFTEQUAL = r'\<\<\='
t_RIGHTSHIFTEQUAL = r'\>\>\='
t_DOUBLESTAREQUAL = r'\*\*\='
t_DOUBLESLASH = r'\/\/'
t_DOUBLESLASHEQUAL = r'\/\/\='
t_ATEQUAL = r'\@\='
t_ELLIPSIS = r'\.\.\.'
t_COLONEQUAL = r'\:\='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value, 'ID')  # Check for reserved words
    return t


def t_STRING(t):
    r'"([^"\n]|(\\"))*"'
    t.value = str(t.value)
    return t


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t


def t_NUMBER(t):
    r'[0-9]+\.?[0-9]*'
    if '\.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t


def t_INDENT(t):
    r'\n[ ]*'
    ile = len(t.value) - 1
    if ile % 4 != 0:
        return None
    if ile == stack[-1] + 4:
        stack.append(ile)
        return t
    elif ile == stack[-1]:
        t.type = "NEWLINE"
        return t
    elif ile < stack[-1]:
        t.type = 'DEDENT'
        to_return = []
        while stack[-1] != ile:
            stack.pop()
            to_return.append(t)
        return tuple(to_return)


def t_DEDENT(t):
    r'\n$'
    ile = len(t.value) - 1
    while stack[-1] != ile:
        stack.pop()
    return t


t_ignore = ' \r'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex(optimize=1)

# data = r"""wypisz("Witaj swiecie")
# jesli(wartosc_bezwzgledna(143) == 1):
#     wypisz("Dziala")
# Falsz
#     zaimportuj"""
with open('test.plpy') as f:
    data = f.read()
#print("Data: '%s'" % repr(data))

lexer.input(data)

result = ""

while True:
    tok = lexer.token()
    if not tok:
        break
    # if isinstance(tok, tuple):
    #     for token in tok:
    #         print(token)
    # else:
    #     print(tok)
    if isinstance(tok, tuple):
        spaces = ""
        for i in range(len(stack)-1):
            spaces+= "    "
        result+="\n"+spaces
    else:
        if(tok.value in keyword_list or tok.value in build_ins):
            result += tok.type
        elif(tok.type == "NEWLINE"):
            result += tok.value
        else:
            result += str(tok.value)

print(result)
f = open("resultfile.py", "w")
f.write(result)
f.close()
