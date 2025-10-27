from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_factor = """
        program FactorTest;
        main { 
            x = (1 + 2 * 3); 
            y = (a); 
        } end
    """
    tree = parser.parse(test_factor)

    print(tree.pretty())


if __name__ == "__main__":
    main()
