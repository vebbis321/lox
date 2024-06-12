from pathlib import Path
from sys import version_info, platform

class Lox:
    @staticmethod
    def main(args):
        if (args.len > 1):
            sys.stdout.write("Usage: jlox [script]")
            sys.exit(64)
        elif (args.len == 1):
            



