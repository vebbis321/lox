from enum import Enum

keywords = {
    "and": " AND",
    "class": "CLASS",
    "else": "ELSE",
    "false": "FALSE",
    "for": "FOR",
    "fun": "FUN",
    "if": "IF",
    "nil": "NIL",
    "or": "OR",
    "print": "PRINT",
    "return": "RETURN",
    "super": "SUPER",
    "this": "THIS",
    "true": "TRUE",
    "var": "VAR",
    "while": "WHILE",
}

class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN = '('
    RIGHT_PAREN = ')'
    LEFT_BRACE = '['
    RIGHT_BRACE = ']'
    COMMA = ','
    DOT = '.'
    MINUS = '-'
    PLUS = '+'
    SEMICOLON = ';'
    SLASH = '/'
    STAR = '*'

    # one or two character tokens
    BANG = '!'
    BANG_EQUAL = '!='
    EQUAL = '='
    EQUAL_EQUAL = '=='
    GREATER = '>'
    GREATER_EQUAL = '>='
    LESS = '<'
    LESS_EQUAL = '<='

    # litterals
    IDENTIFIER = 'identifier'
    STRING = 'string'
    NUMBER = 'number'

    # keywords 
    AND = 'and'
    CLASS = 'class'
    ELSE = 'else'
    FALSE = 'false'
    FUN = 'fun'
    FOR = 'for'
    IF = 'if'
    NIL = 'nil'
    OR = 'or'
    PRINT = 'print'
    RETURN = 'return'
    SUPER = 'super'
    THIS = 'this'
    TRUE = 'true'
    VAR = 'var'
    WHILE = 'while'

    EOF = ''


