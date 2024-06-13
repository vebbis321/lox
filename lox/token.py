from lox.token_type import TokenType


class Token:

    # what the duck is an object in py
    def __init__(self, token_type: TokenType, lexeme: str, litteral, line: int) -> None:
        self.token_type = token_type
        self.lexeme = lexeme
        self.litteral = litteral
        self.line = line
    
    def __str__(self) -> str:
        return f'{self.token_type} {self.lexeme} {self.litteral} {self.line}'
