from typing import List, Union, Any, Optional

from lox import token_type
from lox.token import Token
from lox.token_type import TokenType

class Scanner:
    def __init__(self, source: str):
        self.__source = source
        self.__tokens: List[Token]
        self.__start: int = 0
        self.__current: int = 0
        self.__line: int = 1

    def __is_at_end(self) -> bool:
        return self.__current >= len(self.__source)
    
    def __advance(self) -> str:
        x = self.__source[self.__current]
        self.__current += 1
        return x
        

    def __add_token(self, typ: TokenType):
        self.__add_token(typ, None)

    def __add_token(self, typ: TokenType, literal: Any):
        text = self.__source[self.__start: self.__current]
        self.__tokens.append(Token(typ, text, literal, self.__line))

    def __scan_token(self):
        c = self.__advance()

        match c:
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










        
    def scan_tokens(self) -> List[Token]:
        while not self.__is_at_end():
            self.__start = self.__current
            self.__scan_token()

        self.__tokens.append(Token(TokenType.EOF, TokenType.EOF.value, None, self.__line))

    
