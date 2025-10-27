from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_assign = """
    program demo2;
        var f:float;
        main { f = 3.14; } end
    """
    tree = parser.parse(test_assign)

    print(tree.pretty())


if __name__ == "__main__":
    main()
