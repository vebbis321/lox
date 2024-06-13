from os import stat
import sys
from pathlib import Path
from dataclasses import dataclass

COMMANDS = {
    'exit': exit,
    # 'credits': lox_credits,
    # 'copyright': lox_copyright,
    # 'license': lox_license,
}

@dataclass
class Token:
    token: str

class Scanner:
    def __init__(self, source: str) -> None:
        pass

class Lox:
    @staticmethod 
    def usage() -> None:
        sys.stdout.write("Usage: jlox [script]")

        # error: command line usage error
        sys.exit(64)

    @staticmethod    
    def run_file(filename) -> None:
        # get path of filename
        path = Path(filename).absolute()

        # reads the file and closes
        source = path.read_text(encoding='utf-8', errors='strict')
        
        Lox.run(source)

    @staticmethod
    def run(source: str) -> None:
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()


    @staticmethod
    def run_prompt() -> None:

        # repl: read, evaluate, print, loop
        while True:
            try:
                # a classic repl prompt
                print('>>> ', end='')

                # gets the user input
                expr = input()

                # split by spaces an gets the first input from the array
                first = expr.split(' ')[0]

                # command or expression
                if first in COMMANDS:
                    # example: if exit, exit will be run
                    COMMANDS[first]()
                else:
                    # else run dem expressions
                    Lox.run(expr)

            except KeyboardInterrupt as ki:
                print(f"KeyboardInterrupt deez nutz with err: ${ki}")

            # End of file error...I guess it's when nothing is passed
            except EOFError:
                exit(0)






