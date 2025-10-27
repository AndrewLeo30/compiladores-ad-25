from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_expresion = """
        program Expr;
        main {
        y = (1 + 2) * (3 - 4) / (2 + -5);
        } end
    """
    tree = parser.parse(test_expresion)

    print(tree.pretty())


if __name__ == "__main__":
    main()
