from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_f_call = """
    program ConError;
        main {
            ping()     
        } end
    """
    tree = parser.parse(test_f_call)

    print(tree.pretty())


if __name__ == "__main__":
    main()
