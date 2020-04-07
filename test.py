import build_in_functions
import keywords
import parser

st = parser.expr('a + 5')
code = st.compile('file.py')
a = 5
eval(code)

def create_token(start, end, name):
    pass