import ply.lex as lex
import ply.yacc as yacc

#Lexical analysis

# define tokens for the lexer
tokens = (  
    'NUMBER',
    'STRING',
    'IDENTIFIER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'COLON',
    'EQUALS',
    'NEWLINE',
    'COMMA',
    'OPERATOR',
)

# Keywords
keywords = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'def': 'DEF',
    'return': 'RETURN',
}

tokens += tuple(keywords.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_EQUALS = r'='
t_COMMA = r','
t_OPERATOR = r'==|!=|<=|>=|<|>'

# Ignore spaces and tabs
t_ignore = ' \t'

def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'  
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


#Syntax analysis (parser)

# Precedence rules for arithmetic operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

variables = {}


# Grammar rules
def p_program(p):
    '''program : statement
               | statement program'''
    pass

def p_statement(p):
    '''statement : function_def
                 | if_statement
                 | expression_statement'''
    pass

def p_function_def(p):
    '''function_def : DEF IDENTIFIER LPAREN IDENTIFIER RPAREN COLON statement'''
    print(f"Function definition: {p[2]} with parameter {p[4]}")

def p_if_statement(p):
    '''if_statement : IF expression COLON statement ELSE COLON statement'''
    print("If-Else statement detected")

def p_expression_statement(p):
    '''expression_statement : expression NEWLINE'''
    print(f"Expression: {p[1]}")

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | NUMBER
                  | IDENTIFIER'''
    if len(p) == 2:  
        p[0] = p[1]
    else:  
        p[0] = (p[2], p[1], p[3])  
        print(f"Expression: {p[1]} {p[2]} {p[3]}")

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} ('{p.value}')")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()


# Input code snippet
input_code = """
def my_function(x):
    if x > 10:
        return x + 5
    else:
        return x - 5
"""

# Run the lexer
print("Tokens:")
lexer.input(input_code)
for token in lexer:
    print(token)

# Run the parser
print("\nParsing:")
parser.parse(input_code)