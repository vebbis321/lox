import sys

def main(args): 
    if len(args) > 2:
        sys.stdout.write("Usage: generate_ast <output directory>\n")
        sys.exit(64)
    output_dir = args[1]


    define_ast(output_dir, "Expr", [
            "Binary | left, operator, right",
            "Grouping | expression",
            "Literal | value",
            "Unary | operator, right",
    ])

def define_ast(output_dir: str, basename: str, types: [str]):
    pass

