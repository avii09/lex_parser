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

