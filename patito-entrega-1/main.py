from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_print = """
        program p;
        main { print(2.5); print("hello"); } end
    """
    tree = parser.parse(test_print)

    print(tree.pretty())


if __name__ == "__main__":
    main()
