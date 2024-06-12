from os import stat
import sys
from pathlib import Path

class Lox:
    @staticmethod 
    def usage():
        sys.stdout.write("Usage: jlox [script]")
        sys.exit(64)


    @staticmethod    
    def run_file(filename) -> None:
        path = Path(filename).absolute()
        source = path.read_text(encoding='utf-8', errors='strict')
        
        Lox.run(source)

    @staticmethod
    def run(source) -> None:
        pass








