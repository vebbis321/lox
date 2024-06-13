from lox.lox import Lox
import sys

def main(args) -> None:
    if (len(args) > 1):
       Lox.usage(64)
    elif (len(args) == 1):
        Lox.run_file(args[0])
    else:
        Lox.run_prompt()

# python is strange
main(sys.argv[1:])
