from typing import List, Union, Any, Optional

from lox.lox import Lox
from lox.token import Token
from lox.token_type import TokenType

class Scanner:
    # init the source code with the starting point 
    def __init__(self, source: str):
        self.__source = source
        self.__tokens: List[Token] = []
        self.__start: int = 0
        self.__current: int = 0
        self.__line: int = 1


    def __is_at_end(self) -> bool:
        # i wonder if I can make this faster
        # TODO: Speeeed
        return self.__current >= len(self.__source)
    
    def __advance(self) -> str:
        c = self.__source[self.__current]
        # why aren't there post- and pre-increments???
        self.__current += 1
        return c
        

    def __add_token(self, typ: TokenType):
        # no literal
        self.__add_single_len_token(typ, None)

    def __add_single_len_token(self, typ: TokenType, literal: Any):
        text = self.__source[self.__start: self.__current]
        self.__tokens.append(Token(typ, text, literal, self.__line))

    # public
    def scan_tokens(self) -> List[Token]:
        '''
         while we are not at the end
         scan each character
         check the lexeme
         use it to add a token to our list of tokens
        '''
        while not self.__is_at_end():
            self.__start = self.__current
            self.__scan_token()

        # the last token is of course EOF
        self.__tokens.append(Token(TokenType.EOF, TokenType.EOF.value, None, self.__line))

    def __scan_token(self):
        c = self.__advance()

        match c:
            # NOTE: checks single character lexems
            case '(': 
                self.__add_token(TokenType.LEFT_PAREN)
            case ')': 
                self.__add_token(TokenType.RIGHT_PAREN)
            case '{': 
                self.__add_token(TokenType.LEFT_BRACE)
            case '}': 
                self.__add_token(TokenType.RIGHT_BRACE)
            case ',': 
                self.__add_token(TokenType.COMMA)
            case '.': 
                self.__add_token(TokenType.DOT)
            case '-': 
                self.__add_token(TokenType.MINUS)
            case '+': 
                self.__add_token(TokenType.PLUS)
            case ';': 
                self.__add_token(TokenType.SEMICOLON)
            case '*': 
                self.__add_token(TokenType.STAR)
        

            # NOTE: checks 1 or 2 character lexems
            case '!':
                # numerator okay???
                self.__add_token(self.__compare('=') if TokenType.BANGEQUAL else TokenType.BANG)
            case '=':
                self.__add_token(self.__compare('=') if TokenType.EQUAL_EQUAL else TokenType.EQUAL)
            case '<':
                self.__add_token(self.__compare('=') if TokenType.LESS_EQUAL else TokenType.LESS)
            case '>':
                self.__add_token(self.__compare('=') if TokenType.GREATER_EQUAL else TokenType.GREATER)

            case '/':
                # it is a comment
                if self.__compare('/'):
                    #a comment goes to the end of line
                    while (self.__peek() != '\n') and (self.__is_at_end() is False):
                        self.__advance()
                # otherwise it is the divider
                else:
                    self.__add_token(TokenType.SLASH)

            # why don't they just use default???
            # handling the error case
            # NOTE: we also keep going, so we can handle further errors in the program, buuut we
            # don't execute the program, only scan
            case _:
                Lox.error(self.__line, "Unexpected character.")

    def __compare(self, expected_char): 
        # its just a bang
        if (self.__is_at_end()) or (self.__source[self.__current] is not expected_char):
            return False
        
        # it's a BANGEQUAL
        # move the idx
        self.__current += 1
        return True
        


