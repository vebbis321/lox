from typing import List, Union, Any, Optional

from lox.token import Token
from lox.token_type import TokenType
from lox.keywords import keywords

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
        return self.__tokens

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
                    while (self.__peek() != '\n') and (not self.__is_at_end()):
                        self.__advance()
                # otherwise it is the divider
                else:
                    self.__add_token(TokenType.SLASH)

            # TODO: I may have to get rid of match statements. It's supposed to be a fall through
            # here
            case ' ' | '\r' | '\t' : 
                return

            case '\n':
                self.__line += 1

            case '"':
                self.__string()

            case int():
                self.__number()

            case str():
                self.__identifier()

            # why don't they just use default???
            # handling the error case
            # NOTE: we also keep going, so we can handle further errors in the program, buuut we
            # don't execute the program, only scan
            case _:
                raise SyntaxError(f'Unexpected character "{c}" at '
                              f'line {self.__line}')

    def __identifier(self):
        while self.__peek().isalnum():
            self.__advance()

        text: str = self.__source[self.__start: self.__current]
        typ: TokenType = keywords.get(text, TokenType.IDENTIFIER)
        self.__add_token(typ)

    def __consume_digits(self):
        while self.__peek().isdigit():
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
        self.__add_single_len_token(
            TokenType.NUMBER,
            int_to_float
        )

    def __string(self):
        # while current is not equal to the end of the str
        # and not at the end of source
        while (self.__peek() != '"') and (not self.__is_at_end()):
            if self.__peek() == '\n':
                self.__line +=1
            self.__advance()

        # we can't be at end before enclosing, raise error
        if self.__is_at_end():
            raise SyntaxError(f'Unterminated string at line: {self.__line}')
            return
        
        self.__advance() # the closing "

        # the +1 and -1 is because we strip of "", because they are tokens by themselves
        value: str = self.__source[(self.__start + 1): (self.__current - 1)]
        self.__add_single_len_token(
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
    
        


