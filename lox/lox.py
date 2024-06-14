from posix import write
import sys
import os
from pathlib import Path

from lox.scanner import Scanner

COMMANDS = {
    'exit': exit,
    # 'credits': lox_credits,
    # 'copyright': lox_copyright,
    # 'license': lox_license,
}

class Lox:
    # i guess whis will be static
    # im a man of types
    had_error: bool = False


    @staticmethod 
    def usage(code: int) -> None:
        # I guess I could do the print but...
        sys.stdout.write("Usage: jlox [script]\n")

        # error: command line usage error
        sys.exit(code)

    @staticmethod    
    def run_file(filename) -> None:
        # get path of filename
        path = Path(filename).absolute()

        # reads the file and closes
        source = path.read_text(encoding='utf-8', errors='strict')
        
        # we have it, let's do some lexical analysis
        Lox.run(source)

        # indicate an error in the exit code
        if Lox.had_error:
            sys.exit(65)

    @staticmethod
    def run(source: str) -> None:
        # pass the source of the file to the lexer
        scanner = Scanner(source)

        # get the tokens from the lexer
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)

    @staticmethod
    def error(line: int, message: str) -> None:
        Lox.report(line, "", message)


    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        print(f'[line {line}] Error{where}: {message}')
        
        Lox.had_error = True

    @staticmethod
    def run_prompt() -> None:

        # REPL time
        while True:
            try:
                # a classic REPL prompt
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
                    Lox.had_error = False

            # nois
            except KeyboardInterrupt:
                print(' Error: KeyboardInterrupt')
                try:
                    sys.exit(130)
                except SystemExit:
                    os._exit(130)

            # End of file error...I guess it's when nothing is passed
            except EOFError:
                exit(0)





