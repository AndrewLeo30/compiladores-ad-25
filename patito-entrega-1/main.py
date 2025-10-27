from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_exp = """
        program Exp;
        main {
        y = (1 + 2) - (3 - 4);
        } end
    """
    tree = parser.parse(test_exp)

    print(tree.pretty())


if __name__ == "__main__":
    main()
