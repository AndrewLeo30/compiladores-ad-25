from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_code = "program myprog; vars_declaration funcs_declaration main body_declaration end"
    tree = parser.parse(test_code)
    print(tree.pretty())


if __name__ == "__main__":
    main()
