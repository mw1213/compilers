import build_in_functions
import keywords
import parser
import sys

if ".." not in sys.path: sys.path.insert(0,"..")
import pycparser.ply.lex as lex

def create_token(start, end, name):
    pass


tokens = (
    'STRING',
    'VAR'
)

def t_STRING(t):
     r'"([^"\n]|(\\"))*"'
     t.value = str(t.value)
     return t

def t_VAR(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   return t

t_ignore = ' \t\r\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = r'"nie" jest "Stringiem" nie jest varem'

print("Data: '%s'" % data)

lexer.input(data)

while True:
   tok = lexer.token()
   if not tok: break
   print(tok)