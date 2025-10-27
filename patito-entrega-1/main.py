from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_term = """
        program TermTest;
        main {
        y = (1 + 2) * (3 - 4) / (5 - 1);
        } end
    """
    tree = parser.parse(test_term)

    print(tree.pretty())


if __name__ == "__main__":
    main()
