from lox.Lox import Lox
import sys

def main(args):
    if (args.len > 1):
        sys.stdout.write("Usage: jlox [script]")
        sys.exit(64)
    elif (args.len == 1):
        Lox.run_file()
