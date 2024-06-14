from lox.token_type import TokenType

from typing import Any
from dataclasses import dataclass

# I think this works
@dataclass
class Token:

    token_type: TokenType
    lexeme: str
    litteral: Any
    line: int
    
    def __str__(self) -> str:
        return f'{self.token_type} {self.lexeme} {self.litteral} {self.line}'
