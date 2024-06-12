import Lox
import sys

def main(args) -> None:
    if (args.len > 1):
        Lox.usage(64)
    elif (args.len == 1):
        Lox.run_file()
