import build_in_functions
import keywords
import parser
import sys

if ".." not in sys.path: sys.path.insert(0,"..")
import pycparser.ply.lex as lex


keyword_list = keywords.keywords_dictionary
build_ins = build_in_functions.build_in_functions
reserved_words = {**keyword_list, **build_ins}

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
    'NEWLINE'
]

tokens = tokens + list(reserved_words.values())

literals = [ '+','-','*','/','(',')','[', ']', '.', ',', ':', ';', '|', '&', '<', '>', '=', '%', '{', '}', '~', '^', '@', ]

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
    t.type = reserved_words.get(t.value,'ID')    # Check for reserved words
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
    if('\.' in t.value):
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

t_ignore = ' \t\r'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = r'wypisz("Witaj swiecie")    jesli(wartosc_bezwzgledna(1) == 1):    wypisz("Dziala") Falsz zaimportuj'

print("Data: '%s'" % data)

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: break
    print(tok)