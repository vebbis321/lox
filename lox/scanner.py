from typing import List, Union, Any, Optional

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

    def __add_token(self, token_type: TokenType):
        self.__add_token(token_type, None)

    def __add_token(self, token_type: TokenType, literal: Any):
        text = self.source[self.__start: self.__current]
        self.__tokens.append(Token(token_type, text, literal, self.__line))

    def __scan_token(self):
        c = self.__advance()

    match c:
        case '(': __add_token()

        
    def scan_tokens(self) -> List[Token]:
        while not self.__is_at_end():
            self.__start = self.__current
            self.__scan_token()

        self.__tokens.append(Token(TokenType.EOF, TokenType.EOF.value, None, self.__line))

    
