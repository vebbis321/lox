from os import sync
from typing import List, Union, Any, Optional

from lox.token import Token
from lox.token_type import TokenType
from lox.keywords import keywords

class Scanner:
    # init the source code with the starting point 
    def __init__(self, source: str):
        self.__source: str = source
        self.__tokens: List[Token] = []

        # current char in the lexeme
        self.__start: int = 0
        # char being considered in the lexeme
        self.__current: int = 0

        self.__line: int = 1


    def __is_at_end(self) -> bool:
        # i wonder if I can make this faster
        # TODO: Speeeed
        return self.__current >= len(self.__source)
    
    def __advance(self, step: int = 1) -> str:
        current_char = self.__source[self.__current]
        # why aren't there post- and pre-increments???
        self.__current += step
        return current_char
        

    def __add_token_without_literal(self, typ: TokenType):
        # no literal
        self.__add_token(typ, None)

    def __add_token(self, typ: TokenType, literal: Any):
        text = self.__source[self.__start: self.__current]
        self.__tokens.append(Token(typ, text, literal, self.__line))

    # public
    def scan_tokens(self) -> List[Token]:

        # while we are not at the end
        # scan each character
        # check the lexeme
        # use it to add a token to our list of tokens
        while not self.__is_at_end():
            self.__start = self.__current
            self.__scan_token()

        # the last token is of course EOF
        self.__tokens.append(Token(TokenType.EOF, TokenType.EOF.value, None, self.__line))
        return self.__tokens

    def __scan_token(self):
        c = self.__advance()

        match c:
            # NOTE: checks single character lexems
            case '(': 
                self.__add_token_without_literal(TokenType.LEFT_PAREN)
            case ')': 
                self.__add_token_without_literal(TokenType.RIGHT_PAREN)
            case '{': 
                self.__add_token_without_literal(TokenType.LEFT_BRACE)
            case '}': 
                self.__add_token_without_literal(TokenType.RIGHT_BRACE)
            case ',': 
                self.__add_token_without_literal(TokenType.COMMA)
            case '.': 
                self.__add_token_without_literal(TokenType.DOT)
            case '-': 
                self.__add_token_without_literal(TokenType.MINUS)
            case '+': 
                self.__add_token_without_literal(TokenType.PLUS)
            case ';': 
                self.__add_token_without_literal(TokenType.SEMICOLON)
            case '*': 
                self.__add_token_without_literal(TokenType.STAR)
        

            # NOTE: checks 1 or 2 character lexems
            case '!':
                # numerator okay???
                self.__add_token_without_literal(TokenType.BANG_EQUAL if self.__compare('=') else TokenType.BANG)
            case '=':
                self.__add_token_without_literal(TokenType.EQUAL_EQUAL if self.__compare('=') else TokenType.EQUAL)
            case '<':                                                 
                self.__add_token_without_literal(TokenType.LESS_EQUAL if self.__compare('=') else TokenType.LESS)
            case '>':                                                 
                self.__add_token_without_literal(TokenType.GREATER_EQUAL if self.__compare('=') else TokenType.GREATER)

            case '/':
                # it is a comment
                if self.__compare('/'):
                    # a comment goes to the end of line
                    while (self.__peek() != '\n') and (not self.__is_at_end()):
                        self.__advance()

                # it is a multi line comment!
                elif self.__compare('*'):

                    self.__consume_text('*')
                    if self.__peek() == '*' and self.__peek_next() == "/":
                        self.__advance(2)
                    elif self.__peek() != '"':
                        raise SyntaxError(f'Character not enclosed at line: {self.__line}')
                        return

                # otherwise it is the divider
                else:
                    self.__add_token_without_literal(TokenType.SLASH)

            # TODO: I may have to get rid of match statements. It's supposed to be a fall through
            # here
            case ' ' | '\r' | '\t' : 
                return

            case '\n':
                self.__line += 1

            case '"':
                self.__str()


            case char:
                if char.isalpha():
                    self.__identifier()
                elif char.isnumeric():
                    self.__number()
                else:
                    raise SyntaxError(f'Unexpected character "{c}" at '
                                  f'line {self.__line}')

    def __identifier(self):
        while self.__peek().isalnum():
            self.__advance()

        text: str = self.__source[self.__start: self.__current]
        typ: TokenType = keywords.get(text, TokenType.IDENTIFIER)
        self.__add_token_without_literal(typ)

    def __consume_digits(self):
        while self.__peek().isdigit():
            self.__advance()

    def __consume_text(self, enclosing_char: str):
        # while current is not equal to the end of the str
        # and not at the end of source
        while (self.__peek() != enclosing_char) and (not self.__is_at_end()):
            if self.__peek() == '\n':
                self.__line +=1
            self.__advance()

    def __number(self):
        self.__consume_digits()

        # time to look for fractions
        if (self.__peek() == '.') and (self.__peek_next().isdigit()):

            # consume the .
            self.__advance()

            # keep consuming the next digits
            self.__consume_digits()

        int_to_float = self.__source[self.__start: self.__current]
        self.__add_token(
            TokenType.NUMBER,
            int_to_float
        )
    def __str(self):
        self.__consume_text('"')

        # we can't be at end before enclosing, raise error
        if self.__is_at_end():
            raise SyntaxError(f'Unterminated string at line: {self.__line}')
            return

        if self.__peek() != '"':
            raise SyntaxError(f'Character not enclosed at line: {self.__line}')
            return

        self.__advance() # the closing " or *

        # the +1 and -1 is because we strip of "", because they are tokens by themselves
        value: str = self.__source[(self.__start + 1): (self.__current - 1)]
        self.__add_token(
            TokenType.STRING,
            value
        )



    def __compare(self, expected_char): 
        # its just a bang
        if (self.__is_at_end()) or (self.__source[self.__current] is not expected_char):
            return False
        
        # it's a BANGEQUAL
        # move the idx
        self.__current += 1
        return True

    # peeking at the current char
    def __peek(self) -> str:
        if self.__is_at_end():
            # lol string and arrays in C
            # if we're at the end, add a enclosing char
            return '\0'
        return self.__source[self.__current]
         
    # peeking at the next char
    def __peek_next(self) -> str:
        # only peek if the next is not at the end
        if (self.__current + 1) >= len(self.__source):
            return '\0'
        return self.__source[self.__current + 1]
    
        


