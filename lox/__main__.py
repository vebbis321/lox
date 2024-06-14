import sys

from lox.lox import Lox

def main(args) -> None:
    if (len(args) > 1):
        # if the argument provided by the user is more than 1
        # return error 64 unix stuff
       Lox.usage(64)
    elif (len(args) == 1):
        # if the argument provided by the user is 1
        # we have most likely a file, so run it
        Lox.run_file(args[0])
    else:
        # if there isn't any argument, fire up the REPL
        Lox.run_prompt()

# python is strange
main(sys.argv[1:])
